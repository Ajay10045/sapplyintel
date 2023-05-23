from django.shortcuts import render

def team(request):
    return render(request, 'team/team.html')

def garden_view(request):
    return render(request, 'garden/garden.html')

def contact_view(request):
    return render(request, 'contact/contact.html')

def login_view(request):
    return render(request, 'login/coming_soon.html')

def home_view(request):
    return render(request, 'home/home.html')

def signup_view(request):
    return render(request, 'login/coming_soon.html')

