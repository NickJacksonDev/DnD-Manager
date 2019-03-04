from django.db import models
from Character_Builder.models import Character

# Constants
MAX_LENGTH_CAMPAIGN_NAME = 255

# Keeps track of individual campaigns
class Campaign(models.Model):
    campaignID = models.IntegerField(unique=True)
    campaignName = models.CharField(max_length = MAX_LENGTH_CAMPAIGN_NAME)

    def __str__(self):
        return self.campaignName

# Keeps track of DMs
class CampaignDM(models.Model):
    campaignDMID = models.IntegerField(unique=True)
    character = models.OneToOneField(Character, on_delete=models.CASCADE)
    campaign = models.OneToOneField(Campaign, on_delete=models.CASCADE)

    def __str__(self):
        return self.character.characterName

# Keeps track of parties
class Party(models.Model):
    partyID = models.IntegerField(unique=True)
    campaign = models.OneToOneField(Campaign, on_delete=models.CASCADE)

    def __str__(self):
        return self.campaign.campaignName

# used to allow parties to store mulitple party members
class PartyCharacter(models.Model):
    party = models.ForeignKey(Party, on_delete=models.CASCADE)
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
