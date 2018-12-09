from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Sum
from .models import User
import requests

YOUTUBE_KEY = 'AIzaSyBkrqNMeyqNtray64ogoHuIuBzlG5WTJKw'
URL_YOUTUBE = "https://www.googleapis.com/youtube/v3/search?part=snippet&order=viewCount&key={}".format(YOUTUBE_KEY)


def index(request):
    return render(request, "index.html")


def home(request):
    username = request.POST.get('username', '')
    user = User()
    if not username:
        user = User.objects.get(name=request.session['name'])
    else:
        request.session['name'] = request.POST['username']
        # user = User.objects.get(name=request.POST['username'])

    if not user:
        user = User()
        user.name = request.POST['username']
        user.counter = 0
        user.save()
        request.session['name'] = user.name
    global_counter = User.objects.all().aggregate(Sum('counter'))
    resp = requests.get(URL_YOUTUBE)
    video_id = resp.json()['items'][0]['id']['videoId']

    return render(request, "home.html", {'user': user, 'videoId': video_id, 'global_counter': global_counter['counter__sum']})


def index2(request):
    return render(request, "index2.html")


@csrf_exempt
def incrementation(request):
    counter = request.POST["clickerNumber"]
    user = User.objects.get(name=request.POST['username'])
    user.counter = int(counter)
    user.save()
    return JsonResponse({'success': 'True'})


def global_getter(request):
    global_counter = User.objects.all().aggregate(Sum('counter'))
    return JsonResponse(global_counter)
