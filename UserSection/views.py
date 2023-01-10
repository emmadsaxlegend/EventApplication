from django.shortcuts import render, redirect, get_object_or_404
from AdminSection.models import Event, Customer
from django.views.generic import ListView, DetailView
from django.utils import timezone
from django.http import HttpResponse
from django.db import models
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.http.request import HttpRequest


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
            
            subject = "Event registration"
            message = "You have registered for event " + str(poll.event_name) + " which will be holding on the " + str(poll.event_date) + " \n Kindly show this message on getting to the venue. Thank You."
            message_from = "Event XYZ"
            email = request.POST["email"]
            phone = request.POST["phone"]
            event_id=poll.id
            price = poll.price

            b = Customer(
                email=email,
                phone=phone,
                event_id = event_id,
                amount = price
            )
            if Customer.objects.filter(email=email, phone=phone, event_id=event_id).exists():
                messages.error(request, "You have already registered for this event")
                print("You have already registered for this event")
            else:
                send_mail(subject, message, message_from,[email])
                b.save()
                return render(request, 'make_payment.html', {'customer':b, 'paystack_public_key':settings.PAYSTACK_PUBLIC_KEY})

        
        else :
            return HttpResponse(400,'Invalid vote form')
        poll.save()  
        return redirect('user_events_page')        
       
    context={
        'poll':poll
    }

    return render(request,'vote.html',context)


# def verify_payment(request:HttpRequest, ref:str) -> HttpResponse:
#     payment = get_object_or_404(Customer, ref=ref)
#     verified = payment.verify_payment()
#     if verified:
#         messages.success(request, "Verification successfully")
#     else:
#         messages.error(request, "Verification Failled")
#     return redirect('user_events_page')
