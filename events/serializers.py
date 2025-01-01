from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Event, EventRegistration

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')
        extra_kwargs = {'password': {'write_only': True}}

class EventRegistrationSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    event = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = EventRegistration
        fields = ['id', 'event', 'user', 'registration_date', 'is_waitlisted']
        read_only_fields = ['registration_date', 'is_waitlisted'] 

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'title', 'description', 'date', 'location', 'created_at', 'updated_at']