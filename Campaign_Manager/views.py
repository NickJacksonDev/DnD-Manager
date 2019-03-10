from django.shortcuts import render
from .models import *
from Character_Builder.models import Character
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import CreateCampaignForm
from django.views.generic import CreateView

# def organizeCampaigns():
#     campaignList = Campaign.objects.all()

#     for pc in PartyCharacter.objects.all():
#         pc = 

#     return campaignList

# Create your views here.
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

class CampaignCreateView(CreateView):
    model = Campaign
    fields = ['campaignName']

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

        
