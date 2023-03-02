from django.db import models
from django.contrib.auth.models import User



# class Register(models.Model):
#   username = models.CharField(max_length=30)
#   first_name = models.CharField(max_length=30)
#   last_name = models.CharField(max_length=30)
#    email = models.EmailField(max_length=60)


#    address = models.CharField(max_length=100)
#    need_job = models.BooleanField('Need Job', default='No')



# phone = models.CharField(max_length=30)

# financial_help = models.CharField('You Need Financial Help', max_length=10, choices=Case_CHOICES)

#
# need_training = models.CharField('You Need Training', max_length=10, choices=Case_CHOICES)

# know_job = models.CharField('You Know a Job Vacancy', max_length=10, choices=Case_CHOICES)
# driving = models.CharField('You Have Driving Licence', max_length=10, choices=Case_CHOICES)
# medical = models.CharField('You Need Medical Insurance', max_length=10, choices=Case_CHOICES)
# single = models.CharField('You are Single', max_length=10, choices=Case_CHOICES)
# volunteer = models.CharField('You Can be Volunteer', max_length=10, choices=Case_CHOICES)
# password1 = models.CharField('Password', max_length=20)
# password2 = models.CharField('Password Confirmation', max_length=20)

def __str__(self):
    return self.first_name + ' ' + self.last_name


def save(self, *args, **kwargs):
    super().save(*args, **kwargs)
