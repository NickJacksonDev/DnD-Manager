from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegistrationForm
from Campaign_Manager .models import Campaign
from Character_Builder.models import Character

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! Please log in')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'Users/register.html', {'form': form})

def profile(request):

    context ={

        'campaigns' : Campaign.objects.all(),
        'characters' : Character.objects.all(),
        'title' : 'Profile',

    }

    return render(request, 'Users/profile.html', context)
