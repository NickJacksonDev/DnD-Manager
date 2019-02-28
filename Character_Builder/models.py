from django.db import models

# Create your models here.

# Notes (Django models)
# Each model acts more or less like a database table
# Each model's field acts like a column in said table
# Foreign Keys act as a thing that links a class
# to a parent class that uses it. 
#  eg: abilityScore's "characterID" is a foreign key


# Constants
# Should I capitalize this?
# Also should I move this next to the class that uses it?
max_length_character_name = 255
max_length_alignment = 255
max_length_size = 255

max_length_ability_name = 255

max_length_class_name = 255
max_length_hit_dice = 255


# Description of this model file
# Much of this will be based off of the database schemas

# As this is in the character builder folder, this will focus on
# the character information 

# This class is dynamic, the level, xp, hp, alignment, and (rarely) size may change
class Character(models.Model):
    characterID = models.IntegerField()
    raceID = models.IntegerField()
    classID = models.IntegerField()
    characterName = models.CharField(max_length = max_length_character_name) # Is this a consistent level of abstraction?
    abilityScoreSetID = models.IntegerField()
    level = models.IntegerField()
    xp = models.IntegerField()
    hp = models.IntegerField()
    alignment = models.CharField(max_length = max_length_alignment) # Use string or an enum?
    size = models.CharField(max_length = max_length_size) # Use string or enum?

# This class is dynamic, the abilityScoreValues may change
class AbilityScoreSet(models.Model):
    characterID = models.foreignKey()    # TODO: Need to research this
    abilityScoreID = models.IntegerField() # Acts as an enumeration
    abilityScoreValue = models.IntegerField() 

# This class is static, like a lookup table
class AbilityScore(models.Model):
    abilityScoreID = models.foreignKey()  # TODO: Again, need to research this
    abilityName = models.CharField(max_length = max_length_ability_name)

# This class is largely static, like a lookup table
class CharacterClass(models.Model):
    classID = models.foreignKey()   # TODO: Research this
    className = models.CharField(max_length = max_length_class_name)
    hitDice = models.CharField(max_length = max_length_hit_dice)

# This class is largely static, like a lookup table
class CharacterRace(models.Model):
    raceID = models.foreignKey()    # TODO: Research this
    raceName = models.CharField(max_length = max_length_race_name)
    abilityScoreBonusSetID = models.IntegerField()  # Same level of abstraction?
    speed = models.IntegerField()
    size = models.CharField(max_length_size)   # Okay to overload?


