from django.db import models

# Create your models here.

# Notes (Django models)
# Each model acts more or less like a database table
# Each model's field acts like a column in said table
# Foreign Keys act as a thing that links a class
# to a parent class that uses it. 
#  eg: abilityScore's "characterID" is a foreign key


# Constants
max_length_name = 255
max_length_alignment = 255
max_length_size = 255


# Description of this model file
# Much of this will be based off of the database schemas

# As this is in the character builder folder, this will focus on
# the character information 

class Character(models.Model):
    characterID = models.IntegerField()
    raceID = models.IntegerField()
    classID = models.IntegerField()
    name = models.CharField(max_length = max_length_name)
    abilityScoreSetID = models.IntegerField()
    level = models.IntegerField()
    xp = models.IntegerField()
    hp = models.IntegerField()
    alignment = models.CharField(max_length = max_length_alignment) # Use string or an enum?
    size = models.CharField(max_length = max_length_size) # Use string or enum?

class AbilityScoreSet(models.Model):
    characterID = models.foreignKey()    # Need to research this
    abilityScoreID = models.IntegerField() # Acts as an enumeration
    abilityScoreValue = models.IntegerField() 

class AbilityScore(models.Model):
    abilityScoreID = models.foreignKey()  # Again, need to research this
    name = models.CharField(max_length = max_length_name)  # Okay to overload name?    


