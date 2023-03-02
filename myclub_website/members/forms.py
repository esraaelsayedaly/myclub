from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'        # CHOICES = [('Yes', 'Yes'),
        #          ('No', 'No'),
        #    ]
        # email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
        # first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
        # last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
        # address = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
        # need_job = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(attrs={'class': 'disabled'}))

    # address = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # phone = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))

    # need_job = forms.ChoiceField(choices=Choices, initial="N", widget=forms.RadioSelect)

    # financial_help = forms.CharField(widget=forms.Select(choices=Case_CHOICES))
    # need_job = forms.CharField(widget=forms.Select(choices=Case_CHOICES))
    # need_training = forms.CharField(widget=forms.Select(choices=Case_CHOICES))
    # know_job = forms.CharField(widget=forms.Select(choices=Case_CHOICES))
    # driving = forms.CharField(widget=forms.Select(choices=Case_CHOICES))
    # medical = forms.CharField(widget=forms.Select(choices=Case_CHOICES))
    # single = forms.CharField(widget=forms.Select(choices=Case_CHOICES))
    # Volunteer = forms.CharField(widget=forms.Select(choices=Case_CHOICES))
    # password1 = forms.CharField(max_length=30, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    # password2 = forms.CharField(max_length=30, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
