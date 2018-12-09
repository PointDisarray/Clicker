from django.urls import path

from .views import index, index2, home, incrementation

urlpatterns = [
    path('welcome', index, name='index'),
    path('about', index2, name="index2"),
    path('', home, name="home"),
    path('incrementation', incrementation, name="incrementation"),
]