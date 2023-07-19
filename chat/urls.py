from django.urls import path
from . import views, auth

urlpatterns = [
     path('', views.home, name='home'),
     path('signup/', auth.signup, name='signup'),
     path('login/', auth.login, name='login'),
     path('chatpage/', views.chatpage, name='chatpage'),
     path('search/', views.search, name='search'),
]