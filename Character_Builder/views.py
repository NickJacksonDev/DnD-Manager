from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
	ListView, 
	DetailView,
	CreateView,
	UpdateView,
	DeleteView
)

from django.http import HttpResponseRedirect
from .models import Character
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


class CharacterCreateView(LoginRequiredMixin, CreateView):
	model = Character

	def form_valid(self, form):
		# Updates the author of the current form to be the current user
		form.instance.author = self.request.user 
		return super().form_valid(form)

class CharacterEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Character
	
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)
	
	# Tests to ensure the logged-in user is the owner of that character...
	def test_func(self):
		post = self.get_object()
		if self.request.user == Character.user:
			return True
		return False


class CharacterDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Character

#def create_character(request):
