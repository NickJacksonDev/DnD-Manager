from django.core.management.base import BaseCommand
from Character_Builder.models import (
  CharacterRace
)

# Run this with "python manage.py populate_race_db"
# This is an

class Command(BaseCommand)
  args = '<foo bar ...>'
  help = 'our help string comes here'

  def _create_races(self):
    human = Race(

    )
    human.save()


  def handle(self, *args, **options)
    self._create_races()