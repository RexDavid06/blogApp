from django.shortcuts import render, redirect
from authentication import forms
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from authentication.forms import UserCreationForm, LoginForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin



# Created a restriction for already logged-in users 
class NotLoggedInUser(UserPassesTestMixin):
    def test_func(self):
        return not self.request.user.is_authenticated
    
    def handle_no_permission(self):
        return redirect('app:profile')

class RegisterView(NotLoggedInUser, CreateView):
    form_class = UserCreationForm
    template_name = 'auth/signup.html'
    success_url = reverse_lazy('authentication:signin')
  
    
class SignInView(NotLoggedInUser, LoginView):
    template_name = 'auth/signin.html'

   
class SignOutView(LogoutView):
    next_page = 'authentication:signin'




