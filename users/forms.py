from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class RegisterUserForm(UserCreationForm):
    
    email = forms.EmailField()
    description = forms.CharField()

    class Meta:
        model = User
        fields = ['username','email','description','password1','password2']