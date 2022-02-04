from dataclasses import fields
from rest_framework import serializers
from .models import Event,Voulenteer


class EventSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields=('name','created_by','unique_id')

class VoulenteerSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Voulenteer
        fields=('name','email','event','assigned')
