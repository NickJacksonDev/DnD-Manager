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
# can do   fieldName = ___Field(choices = LIST_NAME)  to make it have a dropdown to the choices given
# can do   from geography.models import ZipCode

# Constants
# Should I move this next to the class that uses it?
MAX_LENGTH_CHARACTER_NAME = 255
MAX_LENGTH_ALIGNMENT = 255
MAX_LENGTH_SIZE = 255
DEFAULT_LEVEL = 0
DEFAULT_XP = 0
DEFAULT_HP = 6

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
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    characterID = models.IntegerField(unique=True) # Note that Django has a built-in primary key
    #raceID = models.IntegerField()
    #classID = models.IntegerField()
    characterName = models.CharField(max_length = MAX_LENGTH_CHARACTER_NAME) # Is this a consistent level of abstraction?
    abilityScoreSetID = models.IntegerField()
    level = models.IntegerField(default=DEFAULT_LEVEL) # may have to split this up into a list as you may have multiple classes...
    xp = models.IntegerField(default=DEFAULT_XP)
    maxHP = models.IntegerField(default=DEFAULT_HP)
    currentHP = models.IntegerField(default=DEFAULT_HP)
    alignment = models.CharField(max_length = MAX_LENGTH_ALIGNMENT) # Use string or an enum?
    size = models.CharField(max_length = MAX_LENGTH_SIZE) # Use string or enum?

    # This method returns a string that represents this class.
    # Similar to toString() from java
    def __str__(self):
        return (self.characterID, self.characterName)


# This class is static, like a lookup table
class AbilityScore(models.Model):
    abilityName = models.CharField(max_length = MAX_LENGTH_ABILITY_NAME)

# This class is dynamic, the abilityScoreValues may change
class AbilityScoreSet(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)  

    # One set has many ability scores. 
    # However, each ability score may go to multiple sets (like an enumeration)
    # Thus a manyToMany relationship is used
    # Note: only one of the two classes should have a manyToMany Field
    abilityScores = models.ManyToManyField(AbilityScore) 
    # abilityScoreID = models.IntegerField() # Acts as an enumeration

    abilityScoreValue = models.IntegerField() 


# This class is largely static, like a lookup table
class CharacterClass(models.Model):
    # TODO: Maybe use ManyToMany relationship, as one character may have multiple 
    # classes... Oh wait. That's actually something to consider...
    character = models.ForeignKey(Character, on_delete=models.CASCADE)   
    className = models.CharField(max_length = MAX_LENGTH_CLASS_NAME)
    hitDice = models.CharField(max_length = MAX_LENGTH_HIT_DICE)


# This class is largely static, like a lookup table
class CharacterRace(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    # raceID = models.ForeignKey(unique=True)
    raceName = models.CharField(max_length = MAX_LENGTH_RACE_NAME)
    abilityScoreBonusSetID = models.IntegerField()  # Same level of abstraction?
    speed = models.IntegerField()
    size = models.CharField(max_length = MAX_LENGTH_SIZE)   # Okay to overload?


