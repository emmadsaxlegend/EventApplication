from django.urls import path
from . import views
from .views import EventView, EventDetailsView, UserPaidEventView, UserFreeEventView, DateEventView

urlpatterns = [

    path("", EventView.as_view(), name="user_events_page"),
    path("free-details-url/<int:pk>/", EventDetailsView.as_view(), name="free_event_details_page"),

    path("paid_event_page/", UserPaidEventView.as_view(), name="paid_event_page"),
    path("free_event_page/", UserFreeEventView.as_view(), name="free_event_page"),

    path("order-by-date/", DateEventView.as_view(), name="order_by_date"),


]
