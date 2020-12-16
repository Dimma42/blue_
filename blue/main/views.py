from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.contrib.auth import login, logout
from django.contrib import messages
from .models import ticket
from .forms import UserRegisterForm, UserLoginForm


def index(request):
    tickets = ticket.objects.all()
    return render(request, 'main/index.html', {'title': 'Main Page', 'tickets': tickets})


def about(request):
    return render(request, 'main/about.html')


def create(request):
    return render(request, 'main/create.html')


def user_login(request):
    return render(request, 'main/register.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Success')
            return redirect('login')
        else:
            messages.error(request, 'Error')
    else:
        form = UserRegisterForm()
    return render(request, 'blue/register.html', {"form": form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect ('home')
    else:
        form = UserLoginForm()
    return render(request, 'blue/login.html', {"form": form})


def user_logout(request):
    logout(request)
    return redirect('login')
