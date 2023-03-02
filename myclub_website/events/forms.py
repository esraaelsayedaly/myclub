from django import forms
from django.forms import ModelForm
from .models import Venue
from .models import MyClubUser


# from localflavor.fr.forms import USStateField

class VenueForm(ModelForm):
    class Meta:
        model = Venue
        fields = ('name', 'address', 'zip_code', 'phone', 'web', 'email_address')


class MyClubUserForm(ModelForm):
    class Meta:
        model = MyClubUser
        fields = ('first_name', 'last_name', 'email', 'phone', 'address', 'gender', 'financial_help', 'need_job', 'need_training'
                  , 'know_job', 'driving', 'medical', 'single', 'volunteer')

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            # 'State': forms.USStateField(attrs={'class': 'form-control'}),
            # 'financial_help': forms.RadioSelect(attrs={'class': 'form-check-input'}),
            # 'need_job': forms.RadioSelect(attrs={'class': 'form-check-input'}),
            # 'need_training': forms.RadioSelect(attrs={'class': 'form-check-input'}),
            # 'know_job': forms.RadioSelect(attrs={'class': 'form-check-input'}),
            # 'driving': forms.RadioSelect(attrs={'class': 'form-check-input'}),
            # 'medical': forms.RadioSelect(attrs={'class': 'form-check-input'}),
            # 'single': forms.RadioSelect(attrs={'class': 'form-check-input'}),
            # 'volunteer': forms.RadioSelect(attrs={'class': 'form-check-input'}),
        }
        gender = forms.ChoiceField(widget=forms.ChoiceField)
        #birthdate = forms.DateTimeField()
        need_job = forms.BooleanField(widget=forms.RadioSelect)

        financial_help = forms.BooleanField(widget=forms.RadioSelect)
        need_training = forms.BooleanField(widget=forms.RadioSelect)
        know_job = forms.BooleanField(widget=forms.RadioSelect)
        driving = forms.BooleanField(widget=forms.RadioSelect)
        medical = forms.BooleanField(widget=forms.RadioSelect)
        single = forms.BooleanField(widget=forms.RadioSelect)

        Volunteer = forms.BooleanField(widget=forms.RadioSelect)

    # Volunteer = forms.forms.ChoiceField(choices=Case_CHOICES, widget=forms.RadioSelect(attrs={'class': 'disabled'}))
