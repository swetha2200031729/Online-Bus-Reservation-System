from django.shortcuts import render, redirect

from .models import *


# Create your views here.
def home(request):
    locations1 = Location.objects.all()
    return render(request,'home.html',{"locations":locations1})
def signup(request):
    return render(request,'signup.html')
def bus_details(request):
    bus_list = BusDetails.objects.all()
    return render(request,'bus_details.html',{'bus_details_list':bus_list})
def ticket_form(request,bus_id):
    if request.method == 'POST':
        number_of_seats = request.POST.get('no_of_seats')
        bus_stop_id = request.POST.get('bus_stop')
        bus_stop = BusStop.objects.get(id = int(bus_stop_id))
        ticket = Ticket(no_of_seats = number_of_seats,bus_stop = bus_stop,user = request.user)
        ticket.save()
        return redirect('home')

    bus = BusDetails.objects.get(id = bus_id)
    bus_stops = BusStop.objects.filter(bus_details = bus)
    return render(request,'ticket_form.html',{'bus_stops':bus_stops})
def aboutus(request):
    return render(request,'aboutus.html')
