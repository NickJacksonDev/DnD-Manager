from django import forms
from .models import *

class CreateCampaignForm(forms.ModelForm):
	class Meta:
		model = Campaign
		fields = ['campaignName']

class selectDMForm(forms.ModelForm):
	class Meta:
		model = CampaignDM
		fields = ['character.characterName']