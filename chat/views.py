from django.shortcuts import render
from .models import Profile
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required


# Create your views here.


def home(request):
    return render (request, 'index.html')


@login_required(login_url='login')
def my_view(request):
    current_user = request.user.username
    return render(request, 'chat.html', {'current_user': current_user})


def chatpage(request):
    return render (request, 'chat.html')


# @login_required(login_url='login')
# def search(request):
#     current_user = request.user.username
#     user_profile = None
#     users_profile_list = []
#     searched_username = ''

#     if request.method == 'POST':
#         searched_username = request.POST.get('username', '').strip()

#         if searched_username:
#             username_profiles = Profile.objects.filter(user__username__icontains=searched_username)
#             users_profile_list = list(username_profiles)

#     return render(request, 'search.html', {'current_user': current_user,
#                                            'user_profile': user_profile,
#                                            'users_profile_list': users_profile_list,
#                                            'searched_username': searched_username})
    