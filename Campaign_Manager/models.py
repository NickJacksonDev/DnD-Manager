from django.db import models
from Character_Builder.models import Character
from django.contrib.auth.models import User

# Constants
MAX_LENGTH_CAMPAIGN_NAME = 255

# finds a default user
def defaultUser():
    default = User.objects.first()

    if default is None:
        default = User.objects.create_user('defaultUser', password='djangoproject')

    return default

# Keeps track of individual campaigns
class Campaign(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, default=defaultUser)
    campaignID = models.AutoField(primary_key=True)
    campaignName = models.CharField(max_length = MAX_LENGTH_CAMPAIGN_NAME)

    def __str__(self):
        return self.campaignName

# Keeps track of DMs
class CampaignDM(models.Model):
    campaignDMID = models.AutoField(primary_key=True)
    character = models.OneToOneField(Character, on_delete=models.CASCADE)
    campaign = models.OneToOneField(Campaign, on_delete=models.CASCADE)

    def __str__(self):
        return self.character.characterName

# Keeps track of parties
class Party(models.Model):
    partyID = models.AutoField(primary_key=True)
    campaign = models.OneToOneField(Campaign, on_delete=models.CASCADE)

    def __str__(self):
        return self.campaign.campaignName

# used to allow parties to store mulitple party members
class PartyCharacter(models.Model):
    party = models.ForeignKey(Party, on_delete=models.CASCADE)
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    approved = models.BooleanField(default = False, editable = True)

    def __str__(self):
        return self.character.characterName
