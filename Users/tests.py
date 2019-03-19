from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile

class ProfileCreationTestCase(TestCase):

	def test_profile_created_upon_user_creation(self):

		User.objects.create_user('TestCaseUser', email='test@email.com', password='testpassword')
		user = User.objects.get(username='TestCaseUser')
		try:
			Profile.objects.get(user = user)
		except Profile.DoesNotExist as e:
			self.fail('Profile was not created when User was created:', e)

	def test_each_user_has_a_profile(self):

		user_list = User.objects.all()
		for user in user_list:
			try:
				Profile.objects.get(user = user)
			except Profile.DoesNotExist as e:
				self.fail('User does not have a Profile:', e)

