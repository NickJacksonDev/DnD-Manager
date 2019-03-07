from django.shortcuts import render
from django.http import HttpResponse

def home(request):

	return render(request, 'Character_Builder/character_builder-home.html', {'title': 'Home'})

def home_page(request):

    context = {
            'title' : 'Welcome to DnD Manager!',
    }

    return render(request, 'Character_Builder/home.html', context)
