from django.shortcuts import render, HttpResponse

def admin_home(request):
    return HttpResponse("<p>this is home from blogs_project</p>")