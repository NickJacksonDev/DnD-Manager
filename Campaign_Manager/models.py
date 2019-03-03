from django.db import models
from Character_Builder.models import Character

# Constants
MAX_LENGTH_CAMPAIGN_NAME = 255

# Keeps track of individual campaigns
class Campaign(models.Model):
    CampaignID = models.IntegerField(unique=True)
    CampaignName = models.CharField(max_length = MAX_LENGTH_CAMPAIGN_NAME)
    CampaignDM = models.OneToOneField(CampaignDM, on_delete=models.CASCADE)
    Party = models.OneToOneField(Party, on_delete=models.CASCADE)

# Keeps track of DMs
class CampaignDM(models.Model):
    CampaignDMID = models.IntegerField(unique=True)
    Character = models.OneToOneField(Character, on_delete=models.CASCADE)

# Keeps track of parties
class Party(models.Model):
    PartyID = models.IntegerField(unique=True)

# used to allow parties to store mulitple party members
class PartyCharacter(models.Model):
    Party = models.ForeignKey(Party, on_delete=models.CASCADE)
    Character = models.ForeignKey(Character, on_delete=models.CASCADE)

