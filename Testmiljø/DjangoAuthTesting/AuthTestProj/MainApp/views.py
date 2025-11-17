from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def custom(request):
    if request.user.is_staff:
        return render(request, 'custom.html')
    else:
        messages.error(request, 'You do not have permission to access this page')
        return redirect('home')

@login_required
def home(request):
    return render(request, 'home.html')
