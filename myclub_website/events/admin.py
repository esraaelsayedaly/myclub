from django.contrib.admin import ModelAdmin
from django.contrib import admin
from django.contrib.auth.models import User

from .models import Venue
from .models import MyClubUser
from .models import Event

from django.db.models.functions import TruncDay
#from django.db.models.aggregates import
from django.db.models import Count
from django.core.serializers.json import DjangoJSONEncoder
import json

admin.site.site_header = "Our Network Admin"


@admin.register(MyClubUser)
class MyClubUser(admin.ModelAdmin):
    # resource = MyClubUserResource

    list_display = (
        'first_name', 'last_name', 'email', 'gender', 'financial_help', 'need_job', 'medical', 'single', 'volunteer',
        'phone', 'address', 'know_job', 'createdDate')

    ordering = ('first_name',)
    search_fields = ('first_name', 'last_name', 'phone', 'address', 'email')
    list_filter = ('gender', 'single', 'financial_help', 'need_job', 'medical',
                   'volunteer', 'need_training',
                   'know_job', 'driving', 'createdDate')

    pass

    def changelist_view(self, request, extra_context=None):
        # Aggregate new authors per day
        chart_data = (
            MyClubUser.object.annotate(date=TruncDay("createdDate"))
                .values("date")
                .annotate(y=Count("id"))
                .order_by("-date")
        )
        # Serialize and attach the chart data to the template context
        as_json = json.dumps(list(chart_data), cls=DjangoJSONEncoder)
        print("Json %s" % as_json)
        extra_context = extra_context or {"chart_data": as_json}
        # Call the superclass changelist_view to render the page

        return super().changelist_view(request, extra_context=extra_context)


# admin.site.register(MyClubUser)


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
