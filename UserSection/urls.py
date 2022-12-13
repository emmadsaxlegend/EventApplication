from django.urls import path, re_path
from . import views
from .views import EventView, EventDetailsView2, UserPaidEventView, UserFreeEventView, DateAccendView, DateDecendView

urlpatterns = [

    path("", EventView.as_view(), name="user_events_page"),
    path("free-details-url/<int:pk>/", EventDetailsView2.as_view(), name="free_event_details_page"),

    path("paid_event_page/", UserPaidEventView.as_view(), name="paid_event_page"),
    path("free_event_page/", UserFreeEventView.as_view(), name="free_event_page"),

    path("accend-date/", DateAccendView.as_view(), name="order_by_date_accend"),
    path("decend-date/", DateDecendView.as_view(), name="order_by_date_decend"),

    path("free/", views.Pay, name="pays"),

]
