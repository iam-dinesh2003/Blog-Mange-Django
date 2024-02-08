from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addblog/', views.addblog, name='addblog'),
    path('login/', views.loginn, name='login'),
    path('logout/', views.logoutt, name='logout'),
    path('register/', views.register, name='register'),
]