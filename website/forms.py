from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

# Setting up a sign up form class to inherit from UserCreationForm class; extending its functionality and customising it
class SignUpForm(UserCreationForm):
    eamil = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Email Address'}))
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(label="",max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Last Name'}))

    class Meta:
        model = User
        # Two passwords for typing and re-typing a password when signing up to prevent typos
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')