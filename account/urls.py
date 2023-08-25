from django.contrib import admin
from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    path('register',views.Register, name='register'),
    path('login', views.CustomerLogin, name='login'),
    path('profile', views.ProfileView.as_view(), name='profile'),
]
