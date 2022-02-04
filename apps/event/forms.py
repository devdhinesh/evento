from pyexpat import model
from django import forms
from .models import Voulenteer,Event
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Voulenteer
        fields = ('__all__')
        exclude = ('assigned',)

        
    
class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('name','description','image_url')

class CustomUserCreationForm(UserCreationForm):
   
    class Meta:
        model = User
        fields = ('username','email','password1','password2')
        
       
