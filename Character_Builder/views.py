from django.shortcuts import render
from django.http import HttpResponse
from .models import Character
from django.http import HttpResponseRedirect
from .forms import CreateCharacterForm

def home(request):
	form = CreateCharacterForm(request.POST or None)

	if form.is_valid():
		form.save()

	context = {
			'title': 'Home',
			'form': form,
			'characters' : Character.objects.all(),

	}
    	
	return render(request, 'Character_Builder/character_builder-home.html', context)
	
	

#def create_character(request):
