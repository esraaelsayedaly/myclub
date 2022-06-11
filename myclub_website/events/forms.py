from django import forms
from django.forms import ModelForm
from .models import Venue
from .models import MyClubUser


class VenueForm(ModelForm):
    class Meta:
        model = Venue
        fields = ('name', 'address', 'zip_code', 'phone', 'web', 'email_address')


class MyClubUserForm(ModelForm):
    class Meta:
        model = MyClubUser
        fields = (
            'first_name', 'last_name', 'email', 'phone', 'address', 'financial_help', 'need_job', 'need_training',
            'know_job', 'driving',
            'medical', 'single', 'volunteer')

        # CHOICES = [('Yes', 'Yes'), ('No', 'No')]

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),

            'financial_help': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'need_job': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'need_training': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'know_job': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'driving': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'medical': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'single': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'volunteer': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
