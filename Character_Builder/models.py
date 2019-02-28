from django.db import models

# Create your models here.

# Notes (Django models)
# Each model acts more or less like a database table
# Each model's field acts like a column in said table
# Foreign Keys act as a thing that links a class
# to a parent class that uses it. 
#  eg: abilityScore's "characterID" is a foreign key
# https://docs.djangoproject.com/en/2.1/topics/db/models/
# can do   fieldName = ___Field(blank = true)  to make this field optional
# can do   fieldName = ___Field(choices = LIST)  to make it have a dropdown to the choices given


# Constants
# Also should I move this next to the class that uses it?
MAX_LENGTH_CHARACTER_NAME = 255
MAX_LENGTH_ALIGNMENT = 255
MAX_LENGTH_SIZE = 255

MAX_LENGTH_ABILITY_NAME = 255

MAX_LENGTH_CLASS_NAME = 255
MAX_LENGTH_HIT_DICE = 255

MAX_LENGTH_RACE_NAME = 255


# Description of this model file
# Much of this will be based off of the database schemas

# As this is in the character builder folder, this will focus on
# the character information 

# This class is dynamic, the level, xp, hp, alignment, and (rarely) size may change
class Character(models.Model):
    characterID = models.IntegerField(unique=True)
    raceID = models.IntegerField()
    classID = models.IntegerField()
    characterName = models.CharField(max_length = MAX_LENGTH_CHARACTER_NAME) # Is this a consistent level of abstraction?
    abilityScoreSetID = models.IntegerField()
    level = models.IntegerField()
    xp = models.IntegerField()
    hp = models.IntegerField()
    alignment = models.CharField(max_length = MAX_LENGTH_ALIGNMENT) # Use string or an enum?
    size = models.CharField(max_length = MAX_LENGTH_SIZE) # Use string or enum?

# This class is dynamic, the abilityScoreValues may change
class AbilityScoreSet(models.Model):
    characterID = models.ForeignKey(unique=True)    # TODO: Need to research this
    abilityScoreID = models.IntegerField() # Acts as an enumeration
    abilityScoreValue = models.IntegerField() 

# This class is static, like a lookup table
class AbilityScore(models.Model):
    abilityScoreID = models.foreignKey(unique=True)  # TODO: Again, need to research this
    abilityName = models.CharField(max_length = MAX_LENGTH_ABILITY_NAME)

# This class is largely static, like a lookup table
class CharacterClass(models.Model):
    classID = models.ForeignKey(unique=True)   # TODO: Research this. Maybe use ManyToMany relationship
    className = models.CharField(max_length = MAX_LENGTH_CLASS_NAME)
    hitDice = models.CharField(max_length = MAX_LENGTH_HIT_DICE)

# This class is largely static, like a lookup table
class CharacterRace(models.Model):
    raceID = models.ForeignKey(unique=True)    # TODO: Research this
    raceName = models.CharField(max_length = MAX_LENGTH_RACE_NAME)
    abilityScoreBonusSetID = models.IntegerField()  # Same level of abstraction?
    speed = models.IntegerField()
    size = models.CharField(max_length_size)   # Okay to overload?


