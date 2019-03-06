from django.shortcuts import render
from .models import Campaign
from Character_Builder.models import Character
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import CreateCampaignForm

# Create your views here.
def home(request):
    form = CreateCampaignForm(request.POST or None)

    if form.is_valid():
        form.save()

    context = {
            'campaigns' : Campaign.objects.all(),
            'title' : 'Campaigns',
            'characters' : Character.objects.all(),
            'form' : form,
    }

    return render(request, 'Campaign_Manager/campaign_manager-home.html', context)