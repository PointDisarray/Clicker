from django.urls import path

from .views import index, index2, home, easySearch, videoSearchTag, logout

urlpatterns = [
    path('welcome', index, name='index'),
    path('about', index2, name="index2"),
    path('', home, name="home"),
    path('easySearch', easySearch, name="easySearch"),
    path('videoSearch', videoSearchTag, name="videoSearchTag"),
    path('logout', logout, name="logout"),
]