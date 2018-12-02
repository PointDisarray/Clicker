from django.shortcuts import render
from django.http import HttpResponse
from .models import User


def index(request):
    user = User.objects.all().first()
    if not user:
        return render(request, "index.html")
    else:
        return render(request, "index.html", {'counter': user.counter})


def reee(request):
    return render(request, "index.html", {"var": "var"})


def index2(request):
    return render(request, "index2.html")
