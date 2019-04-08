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
      className='Fighter',
      hitDice='d10'
    )
    fighter.save()

    barbarian = CharacterClass(
      className='Barbarian',
      hitDice='d12'
    )
    barbarian.save()

    bard = CharacterClass(
      className='Bard',
      hitDice='d8'
    )
    bard.save()

    cleric = CharacterClass(
      className='Cleric',
      hitDice='d8'
    )
    cleric.save()

    druid = CharacterClass(
      className='Druid',
      hitDice='d8'
    )
    druid.save()

    monk = CharacterClass(
      className='Monk',
      hitDice='d8'
    )
    monk.save()

    paladin = CharacterClass(
      className='Paladin',
      hitDice='d10'
    )
    paladin.save()

    ranger = CharacterClass(
      className='Ranger',
      hitDice='d10'
    )
    ranger.save()

    rogue = CharacterClass(
      className='Rogue',
      hitDice='d8'
    )
    rogue.save()

    sorcerer = CharacterClass(
      className='Sorcerer',
      hitDice='d6'
    )
    sorcerer.save()

    warlock = CharacterClass(
      className='Warlock',
      hitDice='d8'
    )
    warlock.save()

    wizard = CharacterClass(
      className='Wizard',
      hitDice='d6'
    )
    wizard.save()


  def handle(self, *args, **options):
    self._create_classes()