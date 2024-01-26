from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CreateAccount(ModelForm):
    class Meta:
        model = Account
        fields = ['user', 'name', 'phone_number', 'profile_pic']

class AddProperty(ModelForm):
    class Meta:
        model = Properties
        fields = ['user_props','prop_name', 'price', 'address', 'state', 'city', 'zip_code', 'size', 'available', 'picture','desc']
