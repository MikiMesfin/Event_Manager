from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.utils import timezone
from django_filters import rest_framework as filters
from .models import Event, EventRegistration
from .serializers import EventSerializer
from .permissions import IsOrganizerOrReadOnly
from django.db import transaction

class EventList(generics.ListCreateAPIView):
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ['location']
    
    def get_queryset(self):
        return Event.objects.filter(date_time__gte=timezone.now())
    
    def perform_create(self, serializer):
        serializer.save(organizer=self.request.user)

class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated, IsOrganizerOrReadOnly]

class UpcomingEventList(generics.ListAPIView):
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Event.objects.filter(
            date_time__gte=timezone.now()
        ).order_by('date_time')

class EventRegistrationView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]

    @transaction.atomic
    def post(self, request, pk):
        try:
            event = Event.objects.select_for_update().get(pk=pk)
        except Event.DoesNotExist:
            return Response(
                {'error': 'Event not found'}, 
                status=status.HTTP_404_NOT_FOUND
            )

        if event.date_time < timezone.now():
            return Response(
                {'error': 'Cannot register for past events'},
                status=status.HTTP_400_BAD_REQUEST
            )

        if EventRegistration.objects.filter(event=event, user=request.user).exists():
            return Response(
                {'error': 'Already registered for this event'},
                status=status.HTTP_400_BAD_REQUEST
            )

        registered_count = event.registrations.filter(is_waitlisted=False).count()
        is_waitlisted = registered_count >= event.capacity

        EventRegistration.objects.create(
            event=event,
            user=request.user,
            is_waitlisted=is_waitlisted
        )

        message = 'Added to waitlist' if is_waitlisted else 'Successfully registered'
        return Response(
            {'message': message},
            status=status.HTTP_201_CREATED
        )