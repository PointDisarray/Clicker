from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, "index.html")


def reee(request):
    return render(request, "index.html", {"var": "var"})


def index2(request):
    return render(request, "index2.html")
