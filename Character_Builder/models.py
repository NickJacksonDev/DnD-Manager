from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

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

# finds a default user
def defaultUser():
    default = User.objects.first()

    if default is None:
        default = User.objects.create_user('defaultUser', password='djangoproject')

    return default

# This class is dynamic, the level, xp, hp, alignment, and (rarely) size may change
class Character(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=defaultUser, null=True, blank=True)
    characterID = models.AutoField(primary_key=True) # Note that Django has a built-in primary key
    characterName = models.CharField(max_length = MAX_LENGTH_CHARACTER_NAME) # Is this a consistent level of abstraction?
    level = models.IntegerField(default=DEFAULT_LEVEL) # may have to split this up into a list as you may have multiple classes...
    xp = models.IntegerField(default=DEFAULT_XP)
    maxHP = models.IntegerField(default=DEFAULT_HP)
    currentHP = models.IntegerField(default=DEFAULT_HP)
    alignment = models.CharField(max_length = MAX_LENGTH_ALIGNMENT) # Use string or an enum?
    size = models.CharField(max_length = MAX_LENGTH_SIZE) # Use string or enum?
    public = models.BooleanField(default=True)

    # Outdated variables
    #raceID = models.IntegerField()
    #classID = models.IntegerField()
    #abilityScoreSetID = models.AutoField(primary_key=True)


    # This method returns a string that represents this class.
    # Similar to toString() from java
    def __str__(self):
        return self.characterName


    # Should associate a user with the character when initialized
    def save_model(self, request, obj, form, change):
        if obj.user == defaultUser:
            # Only set user during the first save.
            obj.user = request.user
        #super().save_model(request, obj, form, change)
    

    # When you create/update a character, this is where the 
    # page goes to after you save the character
    def get_absolute_url(self):
        return reverse('character-detail', kwargs={'pk': self.pk})


# This class is static, like a lookup table
class AbilityScore(models.Model):
    abilityName = models.CharField(max_length = MAX_LENGTH_ABILITY_NAME)
   
# This class is dynamic, the abilityScoreValues may change
class AbilityScoreSet(models.Model):
    abilityScoreSetID = models.AutoField(primary_key=True)
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
    characterID = models.AutoField(primary_key=True)
    className = models.CharField(max_length = MAX_LENGTH_CLASS_NAME)
    hitDice = models.CharField(max_length = MAX_LENGTH_HIT_DICE)


# This class is largely static, like a lookup table
class CharacterRace(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    raceID = models.AutoField(primary_key=True)
    raceName = models.CharField(max_length = MAX_LENGTH_RACE_NAME)
    abilityScoreBonusSetID = models.IntegerField()  # Same level of abstraction?
    speed = models.IntegerField()
    size = models.CharField(max_length = MAX_LENGTH_SIZE)   # Okay to overload?

