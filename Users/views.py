from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User
from django.contrib import messages
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm
from Campaign_Manager .models import Campaign, Party, PartyCharacter
from Character_Builder.models import Character
from .models import Friend

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

def profile(request, pk=None ):

    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user

    myCharacters = Character.objects.filter(user=user)
    allCampaigns = Campaign.objects.all()
    myCampaigns = Campaign.objects.filter(creator=user)

    characterCampaigns = None
    for mc in myCharacters:
        if characterCampaigns==None:
            characterCampaigns = PartyCharacter.objects.filter(character=mc)
        else:
            characterCampaigns |= PartyCharacter.objects.filter(character=mc)

    if characterCampaigns != None:
        for cc in characterCampaigns:
            primaryKey=cc.party.campaign.pk
            myCampaigns |= Campaign.objects.filter(pk=primaryKey)

    for camp in allCampaigns:
        parties = Party.objects.filter(campaign=camp)

        for party in parties:
            for mem in party.members.all():
                for char in myCharacters:
                    if mem == char:
                        campSet = Campaign.objects.filter(pk=camp.pk)
                        myCampaigns |= campSet


    context ={

        'user' : user,
        'users' : User.objects.exclude(id=request.user.id),
        'campaigns' : myCampaigns,
        'characters' : myCharacters,
        'title' : 'Profile',

    }

    return render(request, 'Users/profile.html', context)

def friends(request):

    user = User.objects.exclude(id=request.user.id)
    friend, created = Friend.objects.get_or_create(current_user=request.user)
    friends = friend.users.all()

    context = {
        'title' : 'Friends List',
        'users' : user,
        'friends': friends,
    }

    return render(request, 'Users/friends.html', context)

def edit_profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()

            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'Users/edit_profile.html', context)

def update_friends(request, operation, pk):
    friend = User.objects.get(pk=pk)
    if operation == 'add':
        Friend.make_friend(request.user, friend)
    elif operation == 'remove':
        Friend.unfriend(request.user, friend)
    return redirect('friends')
