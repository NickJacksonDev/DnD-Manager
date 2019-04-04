from django import forms
from .models import Campaign, CampaignComment

class CreateCampaignForm(forms.ModelForm):
	class Meta:
		model = Campaign
		fields = ['campaignName']

class CreatePostForm(forms.ModelForm):

	class Meta:
		model = CampaignComment
		fields = ['title', 'content']


