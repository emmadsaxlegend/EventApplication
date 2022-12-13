from django.shortcuts import render
from AdminSection.models import Event
from django.views.generic import ListView, DetailView

# Create your views here.

class EventView(ListView):
    model = Event
    template_name = "all-events.html"

class EventDetailsView(DetailView):
    # modal = Free
    queryset = Event.objects.all()
    template_name = "EventDetails.html"

class UserFreeEventView(ListView):
    model = Event
    template_name = "user-free-event-page.html"

class UserPaidEventView(ListView):
    model = Event
    template_name = "user-paid-event-page.html"