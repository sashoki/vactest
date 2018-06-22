# -*- coding: utf-8 -*

from django import  forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    phone = forms.CharField(max_length=10, help_text='Phone number')
    first_name = forms.CharField(max_length=30, help_text='First name')
    last_name = forms.CharField(max_length=30, help_text='Last name')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'phone', 'password1', 'password2')


