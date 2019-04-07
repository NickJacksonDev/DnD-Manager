from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

# Populates the user base with 2 simple default users
class Command(BaseCommand):
  # args = '<foo bar ...>'
  help = 'Populate the Class data base'

  def _create_classes(self):




  def handle(self, *args, **options):
    self._create_classes()