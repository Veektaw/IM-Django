from django.urls import path
from . import views, auth

urlpatterns = [
     path('', views.home, name='home'),
     path('signup/', auth.signup, name='signup'),
]