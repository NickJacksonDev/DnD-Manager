from django.shortcuts import render
from .models import *
from Character_Builder.models import Character
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import *
from django.views.generic import CreateView

# Home view
def home(request):
    campaignForm = CreateCampaignForm(request.POST or None)

    if campaignForm.is_valid():
        campaignForm.save()

    context = {
            'title' : 'Campaigns',
            'campaigns' : Campaign.objects.all(),
            'characters' : Character.objects.all(),
            'partys' : Party.objects.all(),
            'partyCharacters' : PartyCharacter.objects.all(),
            'campaignDMs' : CampaignDM.objects.all(),
            'campaignform' : campaignForm,
            'dmform' : dmForm,
    }

    return render(request, 'Campaign_Manager/campaign_manager-home.html', context)

# Creation form view
class CampaignCreateView(CreateView):
    model = Campaign
    fields = ['campaignName']

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

        
