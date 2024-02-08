from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from blogs_app import models

def index(request):
    blogs = models.Blog.objects.all()
    return render(request, 'index.html', {'blogs':blogs})

def addblog(request):
    if request.method == 'POST':
        title = request.POST['title']
        b = models.Blog(title=title, user=request.user)
        b.save()
        return redirect("index")
    return render(request, 'addblog.html')

def loginn(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            print("Login failed")
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        u = User.objects.create_user(username=username, password=password)
        u.save()
        return redirect("login")
    return render(request, 'register.html')

def logoutt(request):
    logout(request)
    return redirect("login")