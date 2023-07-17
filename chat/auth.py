from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from .models import Profile
from itertools import chain



def signup(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        if password == password2:
            
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists')
                return redirect('signup')
            
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username is taken ')
                return redirect('signup')
            
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save
                
                # Logs a user in upon signup
                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)
                
                
                # Create a user profile which is redirected to the settings page
                return redirect('interface')
                
                
        else:
            messages.info(request, 'Passwords do not match')
            return redirect('signup')
        
    else:
        return render(request, 'signup.html')
    
    
def login(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login')
        
    else:
        return render(request, 'login.html')
    

@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('signin')