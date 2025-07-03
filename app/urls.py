from django.urls import path
from app import views

app_name = 'app'
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('detail/<int:pk>/', views.PostDetailView.as_view(), name='detail'),
]