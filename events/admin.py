from django.contrib import admin
from .models import Event, EventRegistration

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_time', 'location', 'organizer', 'capacity')
    search_fields = ('title', 'description', 'location')
    list_filter = ('date_time', 'created_date')

@admin.register(EventRegistration)
class EventRegistrationAdmin(admin.ModelAdmin):
    list_display = ('event', 'user', 'registration_date', 'is_waitlisted')
    list_filter = ('is_waitlisted', 'registration_date')