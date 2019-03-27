from django.db import models
from django.contrib.auth.models import User
from PIL import Image

def defaultUser():
    default = User.objects.first()

    if default is None:
        default = User.objects.create_user('defaultUser', password='djangoproject')

    return default

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='default.png', upload_to='profile_pics')

	def __str__(self):
		return f'{self.user.username} Profile'

	def save(self, **kwargs):
		super().save()

		image = Image.open(self.image.path)

		if image.width > 300 or image.height > 300:
			output_size = (300, 300)
			image.thumbnail(output_size)
			image.save(self.image.path)

class FriendsList(models.Model):
	owner = models.OneToOneField(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.owner.username

class Friend(models.Model):

	users = models.ManyToManyField(User, default=defaultUser)

	#NEEDS REVIEW, not sure how to handle on_delete
	current_user = models.ForeignKey(User, related_name='owner', null=True, on_delete=models.CASCADE)


	@classmethod
	def make_friend(cls, current_user, new_friend):
		friend, created = cls.objects.get_or_create(
			current_user = current_user
		)
		friend.users.add(new_friend)

	@classmethod
	def unfriend(cls, current_user, new_friend):
		friend, created = cls.objects.get_or_create(
			current_user = current_user
		)
		friend.users.remove(new_friend)
