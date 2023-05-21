from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    context = {
        'title': 'Welcome to SapplyIntel',
        'message': 'This is the home page of SapplyIntel application.',
    }
    return render(request, 'home/home.html', context)
