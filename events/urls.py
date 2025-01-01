from django.urls import path
from . import views

app_name = 'events'

urlpatterns = [
    path('events/', views.EventList.as_view(), name='event-list'),
    path('events/upcoming/', views.UpcomingEventList.as_view(), name='upcoming-events'),
    path('events/<int:pk>/', views.EventDetail.as_view(), name='event-detail'),
    path('events/<int:pk>/register/', views.EventRegistrationView.as_view(), name='event-register'),
]
