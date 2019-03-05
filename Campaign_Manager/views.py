from django.shortcuts import render
from .models import Campaign
from Character_Builder.models import Character
from django.http import HttpResponse



# Create your views here.
def home(request):

    context = {
            'campaigns' : Campaign.objects.all(),
            'title' : 'Campaigns',
            'characters' : Character.objects.all(),
    }

    return render(request, 'Campaign_Manager/campaign_manager-home.html', context)
