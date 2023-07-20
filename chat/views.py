from django.shortcuts import render
from .models import Profile
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required


# Create your views here.


def home(request):
    return render (request, 'index.html')

def chatpage(request):
    return render (request, 'chat.html')


@login_required(login_url='login')
def search(request):
    
    
    print("Search view called!")
    current_user = User.objects.filter(username=request.user.username).first()
    if not current_user:
        print("Current User does not exist")
        return render(request, 'search.html', {'user_profile': None, 'users_profile_list': [], 'searched_username': ''})

    user_profile = Profile.objects.filter(user=current_user).first()
    users_profile_list = []
    searched_username = ''

    if request.method == 'POST':
        searched_username = request.POST.get('username', '').strip()

        if searched_username:
            username_profiles = Profile.objects.filter(user__username__icontains=searched_username)
            users_profile_list = list(username_profiles)

    print("Current User:", current_user)
    print("User Profile:", user_profile)
    print("Users Profile List:", users_profile_list)
    print("Searched Username:", searched_username)

    return render(request, 'search.html', {'user_profile': user_profile, 'users_profile_list': users_profile_list, 'searched_username': searched_username})