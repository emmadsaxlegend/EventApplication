from django.shortcuts import render
from AdminSection.models import Event
from django.views.generic import ListView, DetailView

# Create your views here.

class FreeView(ListView):
    model = Event
    template_name = "all-events.html"

class FreeEventDetailsView(DetailView):
    # modal = Free
    queryset = Event.objects.all()
    template_name = "EventDetails.html"