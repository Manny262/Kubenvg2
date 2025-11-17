from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        username = request.POST['username']
        if password1 == password2:
            user = User.objects.create_user(email=email, username=username, password=password1)
            user.save()
            print('user created')
            return redirect('index')
        
    return render(request, 'register.html')

def index(request):
    return render(request, 'index.html')

def loginView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
       
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            
            return redirect('custom')
        else:
            messages.error(request, 'Invalid username or password')
            return render(request, 'login.html')
    
    return render(request, 'login.html')
@login_required 
def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect('index')
