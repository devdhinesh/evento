from email.mime import message
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django import forms
from django.contrib.auth.decorators import login_required

from rest_framework.response import Response
from rest_framework.decorators import api_view

import randomcharactergenerator
import datetime

from .forms import ApplicationForm,EventForm,CustomUserCreationForm
from .models import Event,Voulenteer,Task,Assignment
from .serializers import EventSerailizer,VoulenteerSerailizer

def home(request):
    if request.user.is_authenticated :
        return redirect('dashboard')
    return render(request,'event/home.html')

def signup(request):
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('login')

    return render(request,'event/signup.html',{'form':form})

def application(request,unique_id):
    
    form = ApplicationForm()
    event_req = Event.objects.get(unique_id=unique_id)
    form.fields["event"] = forms.ModelMultipleChoiceField(queryset=Event.objects.filter(unique_id=unique_id))
    
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        #form.fields["event"].queryset = Event.objects.filter(unique_id=unique_id)
        print("inside form")
        if form.is_valid():
            print("inside validation")

            form.save()
            
            messages.success(request ,'Form Submitted Successfully ! Wait for Email!')
            return redirect('home')
        else:
            print("Error form")
            messages.error(request ,'Something went wrong')
    
    return render(request, 'event/application.html',{'form':form,'event':event_req})

@login_required()
def dashboard(request):
    events = Event.objects.filter(created_by=request.user)
    return render(request, 'event/dashboard.html',{'events':events})

@login_required()
def createevent(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        image_url = request.POST.get('image_url')
        created_by = request.user
        unique_id = randomcharactergenerator.rand_code(7)        
        duration = datetime.timedelta(days=3)

        event = Event(name=name,description=description,image_url=image_url,created_by=created_by,unique_id=unique_id,duration=duration)
        event.save()

        return redirect('dashboard')
    
    return render(request, 'event/createevent.html')

@login_required()
def editevent(request,unique_id):
    event = Event.objects.get(unique_id=unique_id)
    form = EventForm(request.POST or None , instance=event)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    return render(request, 'event/editevent.html',{'form':form})

@login_required()
def deleteevent(request,unique_id):
    Event.objects.filter(unique_id=unique_id).delete()
    return redirect('dashboard')
    
@login_required()
def assignments(request,unique_id):   

    return render(request, 'event/assignment.html',{'unique_id':unique_id})



@api_view(['POST','GET'])
def assignments_api(request):

    unique_id = request.data['unique_id']
    
    
    print(unique_id)

    event = Event.objects.filter(unique_id=unique_id)
    volunteers = Voulenteer.objects.filter(event__unique_id = unique_id)
    tasks = Task.objects.filter(event__unique_id = unique_id)

    event_serailizer = EventSerailizer(data=event,many=True)
    volunteer_serailizer = VoulenteerSerailizer(data=volunteers,many=True)

    if event_serailizer.is_valid():
        current_event = event_serailizer.data
    else:
        current_event = event_serailizer.data
    
    if volunteer_serailizer.is_valid():
        current_volunteers = volunteer_serailizer.data
    else:
        current_volunteers = volunteer_serailizer.data

    return Response({'event':current_event,'volunteers':current_volunteers})





@api_view(['POST','GET'])
def assign_people(request):
    email =request.data['email']
    event_id =request.data['event_id']
    event = Event.objects.get(unique_id=event_id)
    try:
        applicant = Voulenteer.objects.get(email=email, event=event)
        assign=Assignment(event=event,volunteer=applicant)
        assign.save()
        Voulenteer.objects.filter(email=email, event =event).update(assigned=True)
        
        return Response({"Success":"The Data Received successfully"})
    except Exception as e:
        return Response({"Error":str(e)})


@api_view(['POST','GET'])
def delete_volunteer(request):
    email =request.data['email']
    event_id =request.data['event_id']
    event = Event.objects.get(unique_id=event_id)

    Voulenteer.objects.filter(email=email, event=event).delete()

    return Response({''})
    



        