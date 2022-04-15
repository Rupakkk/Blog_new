
from django import forms
from django.contrib.auth.models import User
from django.core import validators




class UserRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email','username','first_name','last_name','password')

class UserLogin(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','password')

