from django.urls import path

from .views import index, index2, home, congrats

urlpatterns = [
    path('welcome', index, name='index'),
    path('about', index2, name="index2"),
    path('', home, name="home"),
    path('congrats', congrats, name="congrats"),
]