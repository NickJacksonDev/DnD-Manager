from django.db import models
from Character_Builder.models import Character
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify
from django.urls import reverse
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

    def __str__(self):
        return self.campaignName

    # When you create/update a campaign, this is where the 
    # page goes to after you save the campaign
    def get_absolute_url(self):
        return reverse('campaign-detail', kwargs={'pk': self.pk})
    
    
# Keeps track of DMs
class CampaignDM(models.Model):
    campaignDMID = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=defaultUser)
    campaign = models.OneToOneField(Campaign, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

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

class CampaignComment(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=defaultUser)
    date = models.DateTimeField(default=timezone.now)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    image = models.ImageField(null=True, upload_to='comment_pics')
    slug = models.SlugField(default=slugify("Default Slug"))

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title + '' + str(self.date))
        super(CampaignComment, self).save(*args, **kwargs)

        if self.image != None:
            image = Image.open(self.image.path)

            if image.width > 500 or image.height > 500:
                output_size = (500, 500)
                image.thumbnail(output_size)
                image.save(self.image.path)

    def __str__(self):
        return self.slug