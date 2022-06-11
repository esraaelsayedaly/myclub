from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Venue(models.Model):
    name = models.CharField('Venue Name', max_length=120)
    address = models.CharField(max_length=300)
    zip_code = models.CharField('Zip Code', max_length=15)
    phone = models.CharField('Contact Phone', max_length=25, blank=True)
    web = models.URLField('Website Address', blank=True)
    email_address = models.EmailField('Email Address', blank=True)

    def __str__(self):
        return self.name


class MyClubUser(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField('User Email', max_length=100)
    phone = models.CharField('Your phone', max_length=100, default='')
    address = models.CharField('Your Address', max_length=100, default='')

    financial_help = models.BooleanField('Need Finance Help', default=False)
    need_job = models.BooleanField('Need Job', default=False)
    need_training = models.BooleanField('Need Training/Monitering', default=False)
    know_job = models.BooleanField('Know a job opening in your team/company/business', default=False)
    driving = models.BooleanField('Do you have a driving License', default=False)
    medical = models.BooleanField('Need medical help', default=False)
    single = models.BooleanField('Single', default=False)
    volunteer = models.BooleanField('Willing to volunteer', default=False)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Event(models.Model):
    name = models.CharField('Event Name', max_length=120)
    event_date = models.DateTimeField('Event Date')
    venue = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE)
    # venue = models.CharField(max_length=120)
    manager = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    description = models.TextField(blank=True)
    attendees = models.ManyToManyField(MyClubUser, blank=True)

    def __str__(self):
        return self.name
