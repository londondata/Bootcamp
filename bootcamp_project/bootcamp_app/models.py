from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

	def __str__(self):
		return self.user.username


class Character(models.Model):
	name = models.CharField(max_length=100, help_text="enter your Character Name - choose wisely!")
	age = models.IntegerField(max_length=5)
	energy = models.IntegerField(default = 100)
	mood = models.IntegerField(default = 100)
	knowledge = models.IntegerField(default = 0)
	profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null = True, blank = True, related_name='characters')


class Quiz(models.Model):
	question = models.CharField(max_length=500)
	answer = models.Boolean()
	difficulty = models.CharField(max_length=100)

class Final(models.Model):
	question = models.CharField(max_length=500)
	answer = models.Boolean()
	difficulty = models.CharField(max_length=100)


# Save User Profile on User create or save
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
