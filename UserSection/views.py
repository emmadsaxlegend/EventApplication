from django.shortcuts import render, redirect
from AdminSection.models import Event
from django.views.generic import ListView, DetailView
from django.utils import timezone


# Create your views here.

class EventView(ListView):
    model = Event
    template_name = "all-events.html"

class EventDetailsView2(DetailView):
    # modal = Free
    queryset = Event.objects.all()
    template_name = "EventDetails2.html"


class UserFreeEventView(ListView):
    model = Event
    template_name = "user-free-event-page.html"

class UserPaidEventView(ListView):
    model = Event
    template_name = "user-paid-event-page.html"

class DateAccendView(ListView):
    model = Event
    template_name = "by_date_accending.html"
    ordering = 'event_date'

class DateDecendView(ListView):
    model = Event
    template_name = "by_date_decending.html"
    ordering = '-event_date'

def Pay(request):
    Event.objects.filter().update(slot_left=timezone.now())
    return redirect(request, "dashboard")
