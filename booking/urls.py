from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about_us/", views.about_us, name="about_us"),
    path("services/", views.services, name="services"),
    path("appointments/", views.appointments, name="appointments"),
    
]
