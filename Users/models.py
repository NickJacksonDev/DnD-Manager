from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='default.png', upload_to='profile_pics')

	def __str__(self):
		return f'{self.user.username} Profile'

	def save(self):
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
	FriendsList = models.ForeignKey(FriendsList, on_delete=models.CASCADE)
	friend = models.OneToOneField(User, on_delete=models.CASCADE)
