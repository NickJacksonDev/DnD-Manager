from django.db import models
from Character_Builder.models import Character
from django.contrib.auth.models import User
from PIL import Image


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
    image = models.ImageField(default='default_campaign.jpg', upload_to='campaign_pics')
    #add Description field

    def __str__(self):
        return self.campaignName

    def save(self, **kwargs):
        super().save()

        image = Image.open(self.image.path)

        if image.width > 900 or image.height > 600:
            output_size = (900, 600)
            image.thumbnail(output_size)
            image.save(self.image.path)

# Keeps track of DMs
class CampaignDM(models.Model):
    campaignDMID = models.AutoField(primary_key=True)
    character = models.OneToOneField(Character, on_delete=models.CASCADE)
    campaign = models.OneToOneField(Campaign, on_delete=models.CASCADE)

    def __str__(self):
        return self.character.characterName


# used to allow parties to store mulitple party members
class PartyCharacter(models.Model):
    #party = models.ForeignKey(Party, on_delete=models.CASCADE)
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    approved = models.BooleanField(default = False, editable = True)



    def __str__(self):
        return self.character.characterName

# Keeps track of parties
class Party(models.Model):

    #Keeping this in for now in case the new method doesn't work
    partyID = models.AutoField(primary_key=True)
    #campaign = models.OneToOneField(Campaign, on_delete=models.CASCADE)
    campaign = models.ForeignKey(Campaign, related_name='campaign', on_delete=models.CASCADE)
    members = models.ManyToManyField(User)

    @classmethod
    def add_member(cls, campaign, new_member):
        party, created = cls.objects.get_or_create(
            campaign = campaign
        )
        party.members.add(new_member)

    @classmethod
    def remove_member(cls, campaign, new_member):
        party, created = cls.objects.get_or_create(
            campaign = campaign
        )
        party.members.remove(new_member)

    def __str__(self):
        return self.campaign.campaignName
