from dataclasses import field
from email.mime import audio
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CreateUserForm( UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
