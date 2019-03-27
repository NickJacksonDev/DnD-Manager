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
	# template_name = 'CharacterBuilder/Character_builder-home.html'
	context_object_name = 'characters'


class CharacterDetailView(DetailView):
	model = Character
	# context_object_name = 'characters'


# You no longer need to be logged in to create a character because we can't
# associate the user with the character just yet
class CharacterCreateView(LoginRequiredMixin, CreateView):
# class CharacterCreateView(CreateView):
	model = Character
	fields = ['characterName', 'level', 'xp', 'maxHP', 'currentHP', 'alignment', 'size']
	# exclude = []

	login_url = '/login/'

	# def __init__(self, *args, **kwargs):
	# 	form.instance.user = self.request.user

	def form_valid(self, form):
		# Updates the author of the current form to be the current user
		form.instance.user = self.request.user 
		return super().form_valid(form)


# Currently commented out the requirement that you are the proper user to edit a character...
class CharacterEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
# class CharacterEditView(UpdateView):
	model = Character
	fields = ['characterName', 'level', 'xp', 'maxHP', 'currentHP', 'alignment', 'size']
	# exclude = []

	login_url = '/login/'
	
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)
	
	# Tests to ensure the logged-in user is the owner of that character...
	def test_func(self):
		post = self.get_object()
		if self.request.user == Character.user:
			return True
		return False


# Currently commented out the part where it requires you to be logged into
# the correct account to delete characters
class CharacterDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
# class CharacterDeleteView(DeleteView):
	model = Character
	success_url = '/'
	login_url = '/login/'
	fail_url = '/login/' #Works?

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.user:
			return True
		return False

def home_page(request):

    context = {
            'title' : 'Welcome to DnD Manager!',
    }

    return render(request, 'Character_Builder/home.html', context)
