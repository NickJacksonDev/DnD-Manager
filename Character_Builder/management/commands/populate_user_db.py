from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

# Populates the user base with 2 simple default users
class Command(BaseCommand):
  # args = '<foo bar ...>'
  help = 'Populate the user base with two simple default users'

  def _create_users(self):
    defaultuser1 = User.objects.create_user(
      'defaultuser1',
      password='djangoproject'
    )
    defaultuser1.save()

    defaultuser2 = User.objects.create_user(
      'defaultuser2',
      password='djangoproject'
    )
    defaultuser2.save()


  def handle(self, *args, **options):
    self._create_users()