from django.urls import path

from .views import index, index2, home, incrementation, global_getter, init_socket

urlpatterns = [
    path('welcome', index, name='index'),
    path('about', index2, name="index2"),
    path('', home, name="home"),
    path('incrementation', incrementation, name="incrementation"),
    path('global_getter', global_getter, name="global_getter"),
    path('init_socket', init_socket, name="init_socket"),
]