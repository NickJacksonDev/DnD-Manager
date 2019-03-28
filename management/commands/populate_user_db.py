from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
  args = '<foo bar ...>'
  help = 'our help string comes here'

  def _create_users():
    defaultuser1 = User.objects.create_user(
      
    )
    defaultuser1.save()


def handle(self, *args, **options)
    self._create_users()