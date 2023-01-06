from django.shortcuts import render, redirect
from AdminSection.models import Event, Customer
from django.views.generic import ListView, DetailView
from django.utils import timezone
from django.http import HttpResponse
from django.db import models


# Create your views here.

class EventView(ListView):
    model = Event
    template_name = "all-events.html"

class EventDetailsView2(DetailView):
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



def register(request,pk):
    poll=Event.objects.get(pk=pk)
    if request.method == 'POST':
        sel_opt=request.POST['poll']
       

        if sel_opt == 'option1' :
            poll.bookings += 1
            poll.slot_left = poll.space_capacity - poll.bookings
            
            email = request.POST["email"]
            phone = request.POST["phone"]
            event_id=poll

            b = Customer(
                email=email,
                phone=phone,
                event_id = event_id 
            )
            b.save()
        
        else :
            return HttpResponse(400,'Invalid vote form')
        poll.save()  
        return redirect('user_events_page')          
       
    context={
        'poll':poll
    }

    return render(request,'vote.html',context)


