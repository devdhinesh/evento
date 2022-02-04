from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    image_url = models.URLField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="event")
    unique_id = models.CharField(max_length=10)
    created_on = models.DateTimeField(auto_now_add=True)
    duration = models.DurationField(blank=True, null=True)

    def __str__(self):
        return self.name

class Task(models.Model):
    taskname = models.CharField(max_length=255)
    task_description = models.TextField(blank=True,null=True)
    event = models.ForeignKey(Event,on_delete=models.CASCADE,related_name='tasks')

    def __str__(self):
        return self.taskname +"-"+self.event.name

class Voulenteer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255,unique=True)
    notes = models.TextField(blank=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE,related_name='volunteer')
    assigned = models.BooleanField(default=False)

    def __str__(self):
        return self.name +"-"+self.event.name


class Assignment(models.Model):
    volunteer = models.ForeignKey(Voulenteer,on_delete=models.CASCADE,related_name='assignment')
    event = models.ForeignKey(Event, on_delete=models.CASCADE,related_name='assignment')
    task = models.ForeignKey(Task, on_delete=models.CASCADE,null=True,blank=True, related_name='assignment')

    def __str__(self):
        return self.volunteer.name +"-"+self.event.name

    
