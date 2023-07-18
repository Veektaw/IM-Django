from django.shortcuts import render

# Create your views here.


def home(request):
    return render (request, 'index.html')

def chatpage(request):
    return render (request, 'interface.html')

def search(request):
    return render (request, 'search.html')