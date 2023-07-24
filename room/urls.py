from django.urls import path
from . import views

urlpatterns = [
    #  path('chatpage/', views.chatpage, name='chatpage'),
    path('rooms/', views.rooms, name='rooms'),
    path('<slug:slug>/', views.room, name='room'),
]