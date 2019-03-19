from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
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
	
# This is a class based view that uses django's built-in
# ListView view to display the characters
# It inherits from ListView
class CharacterListView(ListView): 
	model = Character
	template_name = 'CharacterBuilder/Character_builder-home.html'
	context_object_name = 'characters'


class CharacterDetailView(DetailView):
	model = Character
	# context_object_name = 'characters'

#def create_character(request):
