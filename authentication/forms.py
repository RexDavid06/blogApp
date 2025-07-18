from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields  = ['username', 'email', 'password1', 'password2']


class LoginForm(forms.Form):
    class Meta:
        username = forms.CharField(max_length=255)
        password = forms.CharField(max_length=255, widget=forms.PasswordInput)
