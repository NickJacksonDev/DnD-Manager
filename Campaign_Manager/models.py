from django.db import models
from Character_Builder.models import Character
from django.contrib.auth.models import User

# Constants
MAX_LENGTH_CAMPAIGN_NAME = 255

# Automatically creates CampaignIDs
def newCampaignID():
    previousCampaign = Campaign.objects.last()
    if not previousCampaign is None:
        newID = previousCampaign.campaignID + 1
    else:
        newID = 0

    return newID

# finds a default user
def defaultUser():
    default = User.objects.first()

    if default is None:
        default = User.objects.create_user('defaultUser', password='djangoproject')

    return default

# Keeps track of individual campaigns
class Campaign(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, default=defaultUser)
    campaignID = models.IntegerField(unique=True, default=newCampaignID, editable=False)
    campaignName = models.CharField(max_length = MAX_LENGTH_CAMPAIGN_NAME)

    def __str__(self):
        return self.campaignName

# Automatically creates CampaignDMIDs
def newCampaignDMID():
    previousCampaignDM = CampaignDM.objects.last()
    if not previousCampaignDM is None:
        newID = previousCampaignDM.campaignDMID + 1
    else:
        newID = 0

    return newID

# Keeps track of DMs
class CampaignDM(models.Model):
    campaignDMID = models.IntegerField(unique=True, default=newCampaignDMID, editable=False)
    character = models.OneToOneField(Character, on_delete=models.CASCADE)
    campaign = models.OneToOneField(Campaign, on_delete=models.CASCADE)

    def __str__(self):
        return self.character.characterName

# Automatically creates PartyIDs
def newPartyID():
    previousParty = Party.objects.last()
    if not previousParty is None:
        newID = previousParty.partyID + 1
    else:
        newID = 0

    return newID

# Keeps track of parties
class Party(models.Model):
    partyID = models.IntegerField(unique=True, default=newPartyID, editable=False)
    campaign = models.OneToOneField(Campaign, on_delete=models.CASCADE)

    def __str__(self):
        return self.campaign.campaignName

# used to allow parties to store mulitple party members
class PartyCharacter(models.Model):
    party = models.ForeignKey(Party, on_delete=models.CASCADE)
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.character.characterName
