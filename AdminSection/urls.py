from django.urls import path
from . import views
from .views import FreeView, FreeEventDetailsView

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.login, name="login"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("free_event/", views.free, name="free_event"),
    path("paid_event/", views.paid, name="paid_event"),
    path("add_event/", views.create_free_event, name="create_free_event"),
    path("add_event/", views.create_paid_event, name="create_paid_event"),

    path("view_free_events/", FreeView.as_view(), name="free_events_page"),
    path("free-details-url/<int:pk>/", FreeEventDetailsView.as_view(), name="free_event_details_page"),

]
