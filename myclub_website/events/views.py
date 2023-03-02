from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from django.http import HttpResponseRedirect
from .models import Event
from .forms import VenueForm
from .forms import MyClubUserForm


def add_myclubuser(request):
    submitted = False
    if request.method == "POST":
        form = MyClubUserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_myclubuser?submitted=True')
    else:
        form = MyClubUserForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'events/add_myclubuser.html', {'form': form, 'submitted': submitted})


def add_venue(request):
    submitted = False
    if request.method == "POST":
        form = VenueForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_venue?submitted=True')
    else:
        form = VenueForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'events/add_venue.html', {'form': form, 'submitted': submitted})


def all_events(request):
    event_list = Event.objects.all()
    return render(request, 'events/event_list.html',
                  {'event_list': event_list})


def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    name = "Esraa!"
    month = month.title()
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)

    cal = HTMLCalendar().formatmonth(year, month_number)

    now = datetime.now()
    current_year = now.year
    time = now.strftime('%I:%M:%S %p')

    return render(request,
                  'events/home.html', {
                      "first_name": name,
                      "year": year,
                      "month": month,
                      "month_number": month_number,
                      "cal": cal,
                      "current_year": current_year,
                      "time": time,
                  })

# Create your views here.
