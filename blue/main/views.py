from django.shortcuts import render
from .models import ticket


def index(request):
    tickets = ticket.objects.all()
    return render(request, 'main/index.html', {'title': 'Main Page', 'tickets': tickets})


def about(request):
    return render(request, 'main/about.html')


def create(request):
    return render(request, 'main/create.html')