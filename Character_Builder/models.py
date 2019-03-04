from django.db import models

# Constants
MAX_LENGTH_CHARACTER_NAME = 255
MAX_LENGTH_ALIGNMENT = 255
MAX_LENGTH_SIZE = 255
MAX_LENGTH_ABILITY_NAME = 255
MAX_LENGTH_CLASS_NAME = 255
MAX_LENGTH_HIT_DICE = 255
MAX_LENGTH_RACE_NAME = 255

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

    # This method returns the ID that represents the character
    def __str__(self):
        return self.characterName


# This class is static, like a lookup table
class AbilityScore(models.Model):
    # abilityScoreID = models.foreignKey(unique=True)  # TODO: Again, need to research this
    abilityName = models.CharField(max_length = MAX_LENGTH_ABILITY_NAME)

# This class is dynamic, the abilityScoreValues may change
class AbilityScoreSet(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE) 
    # I have no idea what on_delete=models.CASCADE does    

    # One set has many ability scores. 
    # However, each ability score may go to multiple sets (like an enumeration)
    # Thus a manyToMany relationship is used
    # Note: only one of the two classes should have a manyToMany Field
    abilityScores = models.ManyToManyField(AbilityScore) 
    # abilityScoreID = models.IntegerField() # Acts as an enumeration

    abilityScoreValue = models.IntegerField() 


# This class is largely static, like a lookup table
class CharacterClass(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)   # TODO: Research this. Maybe use ManyToMany relationship
    className = models.CharField(max_length = MAX_LENGTH_CLASS_NAME)
    hitDice = models.CharField(max_length = MAX_LENGTH_HIT_DICE)


# This class is largely static, like a lookup table
class CharacterRace(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    # raceID = models.ForeignKey(unique=True)    # TODO: Research this
    raceName = models.CharField(max_length = MAX_LENGTH_RACE_NAME)
    abilityScoreBonusSetID = models.IntegerField()  # Same level of abstraction?
    speed = models.IntegerField()
    size = models.CharField(max_length = MAX_LENGTH_SIZE)   # Okay to overload?