from django.core.management.base import BaseCommand
from Character_Builder.models import (
  CharacterClass
)

# Populates the user base with 2 simple default users
class Command(BaseCommand):
  # args = '<foo bar ...>'
  help = 'Populate the Class data base'

  def _create_classes(self):
    fighter = CharacterClass(
      characterName='Fighter',
      hitDice='d10'
    )
    fighter.save()

    barbarian = CharacterClass(
      characterName='Barbarian',
      hitDice='d12'
    )
    barbarian.save()

    bard = CharacterClass(
      characterName='Bard',
      hitDice='d8'
    )
    bard.save()

    cleric = CharacterClass(
      characterName='Cleric',
      hitDice='d8'
    )
    cleric.save()

    druid = CharacterClass(
      characterName='Druid',
      hitDice='d8'
    )
    druid.save()

    monk = CharacterClass(
      characterName='Monk',
      hitDice='d8'
    )
    monk.save()

    paladin = CharacterClass(
      characterName='Paladin',
      hitDice='d10'
    )
    paladin.save()

    ranger = CharacterClass(
      characterName='Ranger',
      hitDice='d10'
    )
    ranger.save()

    rogue = CharacterClass(
      characterName='Rogue',
      hitDice='d8'
    )
    rogue.save()

    sorcerer = CharacterClass(
      characterName='Sorcerer',
      hitDice='d6'
    )
    sorcerer.save()

    warlock = CharacterClass(
      characterName='Warlock',
      hitDice='d8'
    )
    warlock.save()

    wizard = CharacterClass(
      characterName='Wizard',
      hitDice='d6'
    )
    wizard.save()
    

  def handle(self, *args, **options):
    self._create_classes()