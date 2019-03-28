from django.core.management.base import BaseCommand
from Character_Builder.models import (
  CharacterRace
)

# Run this with "python manage.py populate_race_db"
# This is an

class Command(BaseCommand):
  args = '<foo bar ...>'
  help = 'our help string comes here'

  def _create_races(self):
    human = Race(
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
    human.save()

    dwarf = Race(
      raceName='Dwarf',
      speed=25,
      size='Small',

      strengthBonus=0,
      dexterityBonus=0,
      constitutionBonus=2,
      intelligenceBonus=0,
      wisdomBonus=0,
      charismaBonus=0
    )
    dwarf.save()


    elf = Race(
      raceName='Elf',
      speed=30,
      size='Medium',

      strengthBonus=0,
      dexterityBonus=2,
      constitutionBonus=0,
      intelligenceBonus=0,
      wisdomBonus=0,
      charismaBonus=0
    )
    elf.save()

    gnome = Race(
      raceName='Gnome',
      speed=30,
      size='Medium',

      strengthBonus=0,
      dexterityBonus=0,
      constitutionBonus=0,
      intelligenceBonus=2,
      wisdomBonus=0,
      charismaBonus=0
    )
    gnome.save()

    halfling = Race(
      raceName='Halfling',
      speed=30, #Not sure if this is fully accurate
      size='Medium',

      strengthBonus=0,
      dexterityBonus=2,
      constitutionBonus=0,
      intelligenceBonus=0,
      wisdomBonus=0,
      charismaBonus=0
    )
    halfling.save()

    halfOrc = Race(
      raceName='Half-Orc',
      speed=30,
      size='Medium',

      strengthBonus=2,
      dexterityBonus=0,
      constitutionBonus=1,
      intelligenceBonus=0,
      wisdomBonus=0,
      charismaBonus=0
    )
    halfOrc.save()

    tiefling = Race(
      raceName='Tiefling',
      speed=30,
      size='Medium',

      strengthBonus=0,
      dexterityBonus=0,
      constitutionBonus=0,
      intelligenceBonus=1,
      wisdomBonus=0,
      charismaBonus=2
    )
    tiefling.save()


  def handle(self, *args, **options)
    self._create_races()