from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views import View
from django.contrib.auth.models import User
from app.models import BlogPost
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# Create your views here.

class Home(ListView):
    queryset = BlogPost.objects.all()
    template_name = 'app/home.html'
    context_object_name = 'posts'


class PostDetailView(LoginRequiredMixin, DetailView):
    model = BlogPost
    template_name = 'app/detail.html'
    context_object_name = 'post'
    login_url = '/signin/'


class ProfileView(LoginRequiredMixin, View):
    template_name = 'app/profile.html'
    login_url = '/signin/'

    def get(self, request, *args, **kwargs):
        user = request.user
        profile = user.profile
        return render(request, self.template_name, {
            "user":user,
            "profile": profile
        })
  

