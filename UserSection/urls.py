from django.urls import path
from . import views
from .views import FreeView, FreeEventDetailsView

urlpatterns = [

    path("", FreeView.as_view(), name="user_events_page"),
    path("free-details-url/<int:pk>/", FreeEventDetailsView.as_view(), name="free_event_details_page"),

]
