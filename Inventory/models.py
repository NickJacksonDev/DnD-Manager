from django.db import models
from Character_Builder.models import Character
from django.contrib.auth.models import User

# Constants
MAX_LENGTH_ITEM_NAME = 255

# finds a default user
def defaultUser():
    default = User.objects.first()

    if default is None:
        default = User.objects.create_user('defaultUser', password='djangoproject')

    return default

# Keeps track of individual campaigns
class Item(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=defaultUser)
    itemID = models.AutoField(primary_key=True)
    itemName = models.CharField(max_length = MAX_LENGTH_ITEM_NAME)

    def __str__(self):
        return self.itemName