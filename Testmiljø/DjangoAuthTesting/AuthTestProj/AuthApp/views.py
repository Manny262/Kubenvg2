from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        # Add your registration logic here
        pass
    return render(request, 'register.html')

def custom(request):
    return render(request, 'custom.html')

def home(request):
    return render(request, 'home.html')
