from django.urls import path
from . import views
from .views import EventView, EventDetailsView,FreeEventView,PaidEventView, UpdateEventView, DeleteEventView

urlpatterns = [
    path("view_free_events/", views.home, name="home"),
    path("login/", views.login, name="login"),
    path("admin-dashboard/", views.dashboard, name="dashboard"),
    path("free_event/", views.free, name="free_event"),
    path("paid_event/", views.paid, name="paid_event"),
    path("add_event/", views.create_free_event, name="create_free_event"),
    path("create_event/", views.create_paid_event, name="create_paid_event"),

    path("", EventView.as_view(), name="free_events_page"),
    path("free-details-url/<int:pk>/", EventDetailsView.as_view(), name="free_event_details_page"),


    path("paid_event_page/", PaidEventView.as_view(), name="paid-event-page"),
    path("free_event_page/", FreeEventView.as_view(), name="free-event-page"),
    path('event/edit/<int:pk>/', UpdateEventView.as_view(), name= "update_event" ),
    path('event/<int:pk>/delete', DeleteEventView.as_view(), name= "delete_event" )

]
