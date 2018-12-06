from django.shortcuts import render
from .models import User
import requests

Global_counter = 0
YOUTUBE_KEY = 'AIzaSyBkrqNMeyqNtray64ogoHuIuBzlG5WTJKw'
URL_YOUTUBE = "https://www.googleapis.com/youtube/v3/search?part=snippet&order=viewCount&key={}".format(YOUTUBE_KEY)


def index(request):
    return render(request, "index.html")


def home(request):
    user = User.objects.filter(name=request.POST['username'])
    if not user:
        user = User()
        user.name = request.POST['username']
        user.counter = 0
        user.save()

    resp = requests.get(URL_YOUTUBE)
    video_id = resp.json()['items'][0]['id']['videoId']

    return render(request, "home.html", {'user': user, 'videoId': video_id})


def index2(request):
    return render(request, "index2.html")
