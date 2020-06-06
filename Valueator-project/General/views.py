from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from .forms import RegisterForm

def homepage(request):
    return render(request, "General/homepage.html")

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect("General:homepage")
        else:
            return render(request, "General/login.html", {'error': "Invalid Login"})
    else:
        return render(request, "General/login.html")

def logout(request):
    if request.method == 'POST':
        auth_logout(request)
        return redirect("General:homepage")

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password1']
            form.save()
            user = authenticate(request, username=username, password=password)
            auth_login(request, user)
            return redirect("General:homepage")
        else:
            return render(request, "General/register.html", {'form': form })
    else:
        form = RegisterForm()
        return render(request, "General/register.html", {'form': form })