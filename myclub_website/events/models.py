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
    # Case_CHOICES = (
    #   ('Yes', 'Yes'),
    #   ('No', 'No')
    # )

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField('User Email', max_length=100)
    phone = models.CharField('Your phone', max_length=100, default='')
    address = models.CharField('Your Address', max_length=100, default='')
    #state = models.USStateField('Your State', default=''),

    Gender_CHOICES = (
        ('male', 'MALE'),
        ('Female', 'Female'),
    )

    gender = models.CharField(max_length=6, choices=Gender_CHOICES, default='Male')
    #birthdate = models.DateTimeField('Birth date', blank=True, null=True)
    need_job = models.BooleanField('Need Job', default='')

    financial_help = models.BooleanField('Need Financial Help', default='')

    # need_job = models.BooleanField('You Need Job', choices=Case_CHOICES, default='No')
    need_training = models.BooleanField('Need Training', default='')
    know_job = models.BooleanField('You Know a Job Vacancy', default='')
    driving = models.BooleanField('Have Driving Licence', default='')
    medical = models.BooleanField('Need Medical Insurance', default='')
    single = models.BooleanField('Single', default='')
    volunteer = models.BooleanField('Can be Volunteer', default='')

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
