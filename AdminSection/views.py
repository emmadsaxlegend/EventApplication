import genericpath
from django.shortcuts import redirect, render
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib import messages
from datetime import datetime, date
from .models import Event
from django.views.generic import ListView, DetailView

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
    return render(request, "base.html")


def free(request):
    return render(request, "add_free_events.html")

def paid(request):
    return render(request, "add_paid_events.html")


def create_free_event(request):
    if request.method == "POST":
        event_name = request.POST["event_name"]
        location = request.POST["location"]
        description = request.POST["description"]
        event_date = request.POST["event_date"]
        header_image = request.POST["header_image"]

        a = Event(
            event_name=event_name,
            location=location,
            description=description,
            event_date=event_date,
            header_image=header_image,
        )
        a.save()
        messages.success(request, "Event Registered Successfully")
        return redirect("dashboard")

def create_paid_event(request):
    if request.method == "POST":
        event_name = request.POST["event_name"]
        location = request.POST["location"]
        price = request.POST["price"]
        space_capacity = request.POST["space_capacity"]
        event_end_date = request.POST["event_end_date"]
        description = request.POST["description"]
        event_date = request.POST["event_date"]
        header_image = request.POST["header_image"]

        a = Event(
            event_name=event_name,
            location=location,
            description=description,
            event_date=event_date,
            header_image=header_image,
            event_end_date=event_end_date,
            space_capacity=space_capacity,
            price=price
        )
        a.save()
        messages.success(request, "Event Registered Successfully")
        return redirect("dashboard")




class FreeView(ListView):
    model = Event
    template_name = "free_events_page.html"


class FreeEventDetailsView(DetailView):
    # modal = Free
    queryset = Event.objects.all()
    template_name = "FreeEventDetails.html"



