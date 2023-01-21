import genericpath
from django.shortcuts import redirect, render
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib import messages
from datetime import datetime, date
from .models import Event, Customer
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.
def home(request):
    return render(request, "login.html")


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            if user.is_superuser:
                return redirect("dashboard")
            elif user.is_cashier:
                return redirect("dashboard")
            else:
                return redirect("login")
        else:
            messages.error(request, "Wrong Username or Password")
            return redirect("home")


def dashboard(request):
    return render(request, "home.html")


def free(request):
    return render(request, "add_free_events.html")

def paid(request):
    return render(request, "add_paid_events.html")


def create_free_event(request):
    if request.method == "POST" and request.FILES['header_images']:
        event_name = request.POST["event_name"]
        location = request.POST["location"]
        description = request.POST["description"]
        event_date = request.POST["event_date"]
        header_images = request.FILES["header_images"]

        a = Event(
            event_name=event_name,
            location=location,
            description=description,
            event_date=event_date,
            header_images=header_images,
        )
        a.save()
        messages.success(request, "Event Registered Successfully")
        return redirect("dashboard")

def create_paid_event(request):
    if request.method == "POST" and request.FILES['header_images']:
        event_name = request.POST["event_name"]
        location = request.POST["location"]
        price = request.POST["price"]
        space_capacity = request.POST["space_capacity"]
        event_end_date = request.POST["event_end_date"]
        description = request.POST["description"]
        event_date = request.POST["event_date"]
        header_images = request.FILES["header_images"]

        a = Event(
            event_name=event_name,
            location=location,
            description=description,
            event_date=event_date,
            header_images=header_images,
            event_end_date=event_end_date,
            space_capacity=space_capacity,
            price=price
        )

        a.save()

        messages.success(request, "Event Registered Successfully")
        return redirect("dashboard")




class EventView(ListView):
    model = Event
    template_name = "events_page.html"


class EventDetailsView(DetailView):
    # modal = Free
    queryset = Event.objects.all()
    template_name = "EventDetails.html"

class FreeEventView(ListView):
    model = Event
    template_name = "free-event-page.html"

class PaidEventView(ListView):
    model = Event
    template_name = "paid-event-page.html"


class UpdateEventView(SuccessMessageMixin, UpdateView):
    model = Event
    template_name = 'update-event.html'
    fields = ['event_name', 'location', 'price', 'space_capacity', 'description', 'event_date', 'event_end_date']
    success_message = 'Item Updated successfully!!'



class DeleteEventView(SuccessMessageMixin, DeleteView):
    model = Event
    template_name = 'delete_post.html'
    success_url = reverse_lazy('free_events_page')
    success_message = 'Item deleted successfully!!'

def Cancel(request, pk):
    poll=Event.objects.get(pk=pk)
    eventId = poll.bookings
    if eventId == 0:
        Event.objects.filter(id=pk).update(is_cancelled="True")
        messages.success(request, "Event has been Cancelled Successfully")
        return redirect("free_events_page")
    else:
        messages.success(request, "Event cannot be  Cancelled")
        return redirect("free_events_page")

class CancelledView(ListView):
    model = Event
    template_name = "cancelled.html"

def UndoCancel(request, pk):
    Event.objects.filter(id=pk).update(is_cancelled="False")
    messages.success(request, "Event has been Restored Successfully")
    return redirect("free_events_page")


def view_details(request, pk):
    poll=Event.objects.get(pk=pk)
    eventId = poll.id
    #print(poll.id)
    
    paid_candidates = Customer.objects.filter(event_id=eventId, verified=True)
    reg_candidates = Customer.objects.filter(event_id=eventId)
    booking = Customer.objects.filter(event_id=eventId, verified=True)

    context={
        'paid_candidate_count': paid_candidates.count(),
        'reg_candidate_count': reg_candidates.count(),
        'candidate': booking,
    }
    return render(request, "admin.html", context)