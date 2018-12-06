from django.urls import path

from .views import index, index2, home

urlpatterns = [
    path('index', index, name='index'),
    path('index2', index2, name="index2"),
    path('home', home, name="home"),
]