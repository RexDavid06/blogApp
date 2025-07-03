from django.urls import path
from authentication import views

app_name = 'authentication'
urlpatterns = [
    path('', views.RegisterView.as_view(), name='signup'),
    path('signin/', views.SignInView.as_view(), name='signin'),
    path('signout/', views.SignOutView.as_view(), name='signout')
]