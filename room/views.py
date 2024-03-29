from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Room, Message


@login_required(login_url='login')
def rooms(request):
    rooms = Room.objects.all()
    
    return render (request, 'rooms.html', {'rooms': rooms})

@login_required(login_url='login')
def room(request, slug) :
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter (room=room)[0: 30]
    
    return render (request, 'chat.html', {'room': room, 'messages': messages})
