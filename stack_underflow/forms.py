from django import forms
from django.contrib.auth.models import User
from rango.models import UserProfile

class Sign_Up_Form(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password')
