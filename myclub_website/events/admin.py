from django.contrib import admin
from django.contrib.auth.models import User
# Register your models here

from .models import Venue
from .models import MyClubUser
from .models import Event

# admin.site.register(Venue, VenuAdmin)
#admin.site.register(MyClubUser)


# admin.site.register(Event)

admin.site.site_header = "Our Network Admin"


@admin.register(MyClubUser)
class MyClubUser(admin.ModelAdmin):
    list_display = ('first_name', 'email', 'need_job', 'medical', 'single', 'volunteer')
    ordering = ('first_name',)
    search_fields = ('first_name', 'last_name', 'phone', 'address', 'email')
    list_filter = ('single', 'need_job', 'medical', 'volunteer', 'financial_help',
                   'need_training', 'know_job', 'driving', 'email', 'first_name')


@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone')
    ordering = ('name',)
    search_fields = ('name', 'address')


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    fields = (('name', 'venue'), 'event_date', 'description', 'manager')
    list_display = ('name', 'event_date', 'venue')
    list_filter = ('event_date', 'venue')
    ordering = ('event_date',)

