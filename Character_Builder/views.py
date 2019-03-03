from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    	
	return render(request, 'Character_Builder/character_builder-home.html', {'title': 'Home'})
