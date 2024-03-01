from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import patient
from .forms import AppointmentsForm
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'booking/index.html')

def about_us(request):
    return render(request, "booking/about_us.html")

def services(request):
    return render(request, "booking/services.html")


def appointments(request):

    if request.method == 'POST':
        form = AppointmentsForm(request.POST)
        if form.is_valid():
            full_name = form.cleaned_data['full_name']
            phone_number = form.cleaned_data['phone_number']
            message = form.cleaned_data['message']
            datetime = form.cleaned_data['datetime_field']
            

            new_patient = patient(full_name=full_name, number=phone_number, description=message, datetime= datetime)
            new_patient.save()
            
            return HttpResponseRedirect(reverse("index"))
    else:
        form = AppointmentsForm()
        
      


    return render(request, "booking/appointments.html", {'form': form})