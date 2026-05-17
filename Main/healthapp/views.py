from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, "index.html", {})

def heartApp(request):
    return render(request, "heart.html", {})

def diabetesApp(request):
    return render(request, "diabetesapp.html", {})

def lungsApp(request):
    return render(request, "lungsapp.html", {})

def about(request):
    return render(request, "about.html", {})
