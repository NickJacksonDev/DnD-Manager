from django.db import models

# Create your models here.

#
class Campaign(models.Model):
    CampaignID = models.IntegerField(unique=True)
    CampaignDMID = models.IntegerField()
    PartyID = models.IntegerField()

#
class CampaignDM(models.Model):
    CampaignDMID = models.IntegerField(unique=True)
    CharacterID = models.IntegerField()

#
class Party(models.Model):
    PartyID = models.IntegerField(unique=True)
    PartyCharactersID = models.IntegerField()

#
class PartyCharacters(models.Model):
    PartyID = models.IntegerField()
    CharacterID = models.IntegerField()

