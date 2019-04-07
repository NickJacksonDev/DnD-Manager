from django import forms
from .models import Campaign, CampaignComment

class CreateCampaignForm(forms.ModelForm):
	class Meta:
		model = Campaign
		fields = ['campaignName']

class CreatePostForm(forms.ModelForm):

	image = forms.ImageField(required=False)

	class Meta:
		model = CampaignComment
		fields = ['title', 'content', 'image']


