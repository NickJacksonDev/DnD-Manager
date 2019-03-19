from django.db import models
from Character_Builder.models import Character
from django.contrib.auth.models import User

# Constants
MAX_LENGTH_ITEM_NAME = 255

# Creates a default character
def defaultCharacter():
    default = Character.objects.first()
    return default

# Keeps track of inventories
class Inventory(models.Model):
    inventoryID = models.AutoField(primary_key=True)
    character = models.ForeignKey(Character, on_delete=models.CASCADE, default=defaultCharacter)

    def __str__(self):
        return self.character.characterName

# Creates default inventory
def defaultInventory():
    default = Inventory.objects.first()
    return default

# Keeps track of individual items
class Item(models.Model):
    itemID = models.AutoField(primary_key=True)
    itemName = models.CharField(max_length = MAX_LENGTH_ITEM_NAME)
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE, default=defaultInventory)

    def __str__(self):
        return self.itemName