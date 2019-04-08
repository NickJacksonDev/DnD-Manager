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

DEFAULT_ABILITY_SCORE = 10
DEFAULT_ABILITY_SCORE_BONUS = 0


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

# Sets default race to human
def defaultRace():
    default = CharacterRace.objects.first()

    if default is None:
        default = CharacterRace(
            raceName='Human',
            speed=30,
            size='Medium',

            strengthBonus=1,
            dexterityBonus=1,
            constitutionBonus=1,
            intelligenceBonus=1,
            wisdomBonus=1,
            charismaBonus=1
        )
        default.save()

    # Returns the primary key, not the race itself
    return default.raceID


# This class is largely static, like a lookup table
# Note: because the character has a key to this, it must
#   be above the Character class
class CharacterRace(models.Model):
    raceID = models.AutoField(primary_key=True)
    raceName = models.CharField(max_length = MAX_LENGTH_RACE_NAME)
    speed = models.IntegerField()
    size = models.CharField(max_length = MAX_LENGTH_SIZE)   # Okay to overload?

    # Welp, I'm going to make this simpler and just hard-code
    # the 6 most essential stats
    strengthBonus = models.IntegerField(default=DEFAULT_ABILITY_SCORE_BONUS)
    dexterityBonus = models.IntegerField(default=DEFAULT_ABILITY_SCORE_BONUS)
    constitutionBonus = models.IntegerField(default=DEFAULT_ABILITY_SCORE_BONUS)
    intelligenceBonus = models.IntegerField(default=DEFAULT_ABILITY_SCORE_BONUS)
    wisdomBonus = models.IntegerField(default=DEFAULT_ABILITY_SCORE_BONUS)
    charismaBonus = models.IntegerField(default=DEFAULT_ABILITY_SCORE_BONUS)

    # Outdated code
    # abilityScoreBonusSetID = models.IntegerField()  # Same level of abstraction?
    # character = models.ForeignKey(Character, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.raceName


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

    # blank=true, null=true means that it's optional
    race = models.ForeignKey(CharacterRace, on_delete=models.CASCADE, default=defaultRace, null=True, blank=True)

    # Outdated variables
    #raceID = models.IntegerField()
    #classID = models.IntegerField()
    #abilityScoreSetID = models.AutoField(primary_key=True)

    strength = models.IntegerField(default=DEFAULT_ABILITY_SCORE)
    dexterity = models.IntegerField(default=DEFAULT_ABILITY_SCORE)
    constitution = models.IntegerField(default=DEFAULT_ABILITY_SCORE)
    intelligence = models.IntegerField(default=DEFAULT_ABILITY_SCORE)
    wisdom = models.IntegerField(default=DEFAULT_ABILITY_SCORE)
    charisma = models.IntegerField(default=DEFAULT_ABILITY_SCORE)


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
# Now outdated, refactored so that we don't have to access another form
# from within a form (there were 2 forms on a page, and you had to access it again)
class AbilityScoreSet(models.Model):
    abilityScoreSetID = models.AutoField(primary_key=True)
    character = models.ForeignKey(Character, on_delete=models.CASCADE)#, default=defaultCharacter)

    # One set has many ability scores.
    # However, each ability score may go to multiple sets (like an enumeration)
    # Thus a manyToMany relationship is used
    # Note: only one of the two classes should have a manyToMany Field
    # abilityScores = models.ManyToManyField(AbilityScore)
    # abilityScoreValue = models.IntegerField()

    strength = models.IntegerField(default=DEFAULT_ABILITY_SCORE)
    dexterity = models.IntegerField(default=DEFAULT_ABILITY_SCORE)
    constitution = models.IntegerField(default=DEFAULT_ABILITY_SCORE)
    intelligence = models.IntegerField(default=DEFAULT_ABILITY_SCORE)
    wisdom = models.IntegerField(default=DEFAULT_ABILITY_SCORE)
    charisma = models.IntegerField(default=DEFAULT_ABILITY_SCORE)

    # Needed to save model
    def save_model(self, request, obj, form, change):
        # Updates the character to be the one it's associated with
        # if obj.character = defaultCharacter :

        super().save_model(request, obj, form, change)



# This class is largely static, like a lookup table
class CharacterClass(models.Model):
    # TODO: Maybe use ManyToMany relationship, as one character may have multiple
    # classes... Oh wait. That's actually something to consider...
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    characterID = models.AutoField(primary_key=True)
    className = models.CharField(max_length = MAX_LENGTH_CLASS_NAME)
    hitDice = models.CharField(max_length = MAX_LENGTH_HIT_DICE)
