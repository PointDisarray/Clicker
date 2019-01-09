import requests
from django.db.models import Sum
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import User

YOUTUBE_KEY = 'AIzaSyBkrqNMeyqNtray64ogoHuIuBzlG5WTJKw'
URL_YOUTUBE = "https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=50&key={}&q=".format(YOUTUBE_KEY)


def index(request):
    return render(request, "clickerRoot/index.html")


def home(request):
    username = request.POST.get('username', '')

    if not username:
        user = User.objects.get(name=request.session['name'])
    else:
        request.session['name'] = request.POST['username']
        user = User.objects.filter(name=request.POST['username']).first()

    if not user:
        user = User()
        user.name = request.POST['username']
        user.counter = 0
        user.save()
        request.session['name'] = user.name

    global_counter = User.objects.all().aggregate(Sum('counter'))

    return render(request, "clickerRoot/home.html", {'user_c': user, 'global_counter': global_counter['counter__sum']})


def index2(request):
    return render(request, "clickerRoot/index2.html")


def easySearch(request):
    return render(request, "clickerRoot/easySearch.html")


@csrf_exempt
def videoSearchTag(request):
    video_name = request.POST["videoTag"]

    video_name = video_name.replace(" ", "%20")
    resp = requests.get(URL_YOUTUBE + video_name)
    try:
        from random import randint
        rint = randint(0, 50)
        video_id = resp.json()['items'][rint]['id']['videoId']
    except Exception as e:
        video_id = resp.json()['items'][0]['id']['videoId']

    return JsonResponse({'videoId': str(video_id)})

# def init_socket(request):
#     socket_server_side.run()
#     return JsonResponse({'socket start': 'True'})


# @csrf_exempt
# def incrementation(request):
#     counter = request.POST["clickerNumber"]
#     user = User.objects.get(name=request.POST['username'])
#     user.counter = int(counter)
#     user.save()
#     return JsonResponse({'success': 'True'})


# def global_getter(request):
#     global_counter = User.objects.all().aggregate(Sum('counter'))
#     return JsonResponse(global_counter)
