from django.urls import path
from . import views, auth
from room.views import rooms

urlpatterns = [
     path('', views.home, name='home'),
     path('signup/', auth.signup, name='signup'),
     path('login/', auth.login, name='login'),
     path('logout/', auth.logout, name='logout'),
     path('chatpage/', views.chatpage, name='chatpage'),
     path('my_view/', views.my_view, name='my_view'),
]