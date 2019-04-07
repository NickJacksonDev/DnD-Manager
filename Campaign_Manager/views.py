from django.shortcuts import render, redirect
from .models import *
from Character_Builder.models import Character
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import CreateCampaignForm
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from Users.models import *

# Home view
def home(request):
    form = CreateCampaignForm(request.POST or None)

    if form.is_valid():
        form.save()
        

    context = {
            'title' : 'Campaigns',
            'campaigns' : Campaign.objects.all(),
            'characters' : Character.objects.all(),
            'partys' : Party.objects.all(),
            'partyCharacters' : PartyCharacter.objects.all(),
            'campaignDMs' : CampaignDM.objects.all(),
            'form' : form,
    }

    return render(request, 'Campaign_Manager/campaign_manager-home.html', context)

def overview(request, pk=None ):

    #hazy on this. I want to set the campaign to the campaign ref'd by the pk
    campaign = Campaign.objects.get(pk=pk)
    party, created = Party.objects.get_or_create(campaign = campaign)
    members = party.members.all()
    friend, created = Friend.objects.get_or_create(current_user=request.user)
    friends = friend.users.all()


    context ={

        'campaign' : campaign,
        #'users' : User.objects.exclude(id=request.user.id),
        'campaigns' : Campaign.objects.all(),
        'characters' : Character.objects.all(),
        'title' : 'Overview',
        'members' : members,
        'friends' : friends,

    }

    return render(request, 'Campaign_Manager/overview.html', context)

def update_party(request, operation, pk, id):
    new_member = User.objects.get(pk=pk)
    campaign = Campaign.objects.get(pk=id)
    if operation == 'add':
        Party.add_member(campaign, new_member)
    elif operation == 'remove':
        Party.remove_member(campaign, new_member)
    return redirect('overview_with_pk', pk=campaign.pk)


class CampaignListView(ListView):
    model = Campaign

    context_object_name = 'campaigns'

class CampaignDetailView(DetailView):
    model = Campaign

# Creation form view
class CampaignCreateView(CreateView):
    model = Campaign
    fields = ['campaignName']

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)
