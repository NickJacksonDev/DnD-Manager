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
from .models import (
	Character, 
	AbilityScoreSet,
	CharacterRace
)
from .forms import (
	CreateCharacterForm, 
	EditCharacterForm, 
	EditAbilityScoresForm 
)

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
	# template_name = 'CharacterBuilder/Character_builder-home.html'
	context_object_name = 'characters'


class CharacterDetailView(DetailView):
	model = Character
	# context_object_name = 'characters'

	def get_context_data(self, **kwargs):
		# Call the base implementation first to get a context
		context = super().get_context_data(**kwargs)
		# Add in the AbilityScore so it can print that as well
		# context['abilityScores'] = AbilityScoreSet.objects.get_object(character = character)
		
		return context


class CharacterCreateView(LoginRequiredMixin, CreateView):
	model = Character
	fields = ['characterName', 'level', 'xp', 'maxHP', 'currentHP', 'alignment', 'size']
	# exclude = []

	# Added for LoginRequiredMixin
	login_url = '/login/'

	# def __init__(self, *args, **kwargs):
	# 	form.instance.user = self.request.user

	def get_context_data(self, **kwargs):
		context = super(CharacterCreateView, self).get_context_data(**kwargs)
		form = CreateCharacterForm(self.request.POST or None)
		context['form1'] = form

		form2 = EditAbilityScoresForm(self.request.POST or None)
		context['form2'] = form2
		return context

	def form_valid(self, form):
		# Updates the author of the current form to be the current user
		form.instance.user = self.request.user 
		# context['form2'].instance.character = form.instance
		return super().form_valid(form)
	

	# TODO: Lookup how to manage this. Perhaps render a different context
	# Or a "Sorry, not able to login" screen
	def form_invalid(self, **kwargs):
		return self.render_to_response(self.get_context_data(**kwargs))



class CharacterEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Character
	fields = ['characterName', 'level', 'xp', 'maxHP', 'currentHP', 'alignment', 'size']
	# exclude = []

	login_url = '/login/'
	
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)
	
	# Tests to ensure the logged-in user is the owner of that character...
	def test_func(self):
		Character = self.get_object()
		if self.request.user == Character.user:
			return True
		return False
	

	def get_context_data(self, **kwargs):
		context = super(CharacterEditView, self).get_context_data(**kwargs)
		form = CreateCharacterForm(self.request.POST or None)
		context['form1'] = form

		form2 = EditAbilityScoresForm(self.request.POST or None)
		context['form2'] = form2
		return context

	# TODO: Lookup how to manage this. Perhaps render a different context
	# Or a "Sorry, not able to login" screen
	def form_invalid(self, **kwargs):
		return self.render_to_response(self.get_context_data(**kwargs))


class CharacterDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Character
	success_url = '/'
	login_url = '/login/'
	fail_url = '/login/' #Works?

	def test_func(self):
		Character = self.get_object()
		if self.request.user == Character.user:
			return True
		return False

def home_page(request):

    context = {
            'title' : 'Welcome to DnD Manager!',
    }

    return render(request, 'Character_Builder/home.html', context)


# This is a class based view that uses django's built-in
# ListView view to display the races
# It inherits from ListView
class CharacterRaceListView(ListView): 
	model = CharacterRace
	# template_name = 'CharacterBuilder/Character_builder-home.html'
	context_object_name = 'races'

