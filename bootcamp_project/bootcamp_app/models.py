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
	age = models.IntegerField()
	energy = models.IntegerField(default = 100)
	mood = models.IntegerField(default = 100)
	knowledge = models.IntegerField(default = 0)
	profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null = True, blank = True, related_name='characters')
	is_completed = models.BooleanField(default=False)
	event_one = models.IntegerField(null = True, blank = True)
	event_two = models.IntegerField(null = True, blank = True)
	event_three = models.IntegerField(null = True, blank = True)
	quiz_one = models.CharField(max_length=100, null = True, blank = True)
	quiz_two = models.CharField(max_length=100, null = True, blank = True)
	finals_questions = models.IntegerField(null = True, blank = True)


	# Model vars to return
	es = ''
	ms = ''
	ks = ''
	statuses = []

	# Set energy status message
	def energy_status(self):
		if self.energy < 33:
			self.es = "You are exhausted."
		if self.energy >= 33 and self.energy < 66:
			self.es = "You feel a little tired, but nothing that a little rest won't cure."
		if self.energy >=66 and self.energy < 100:
			self.es = "You feel pretty rested. You're ready to go kick some ass in class"
		if self.energy >= 100:
			self.es = "ZOMG! You are feeling super energetic! Who needs coffee?!?!!?"
		return self.es

	# Set mood status message
	def mood_status(self):
		if self.mood < 33:
			self.ms = "You feel oh so sad today. The world sucks."
		if self.mood >= 33 and self.mood < 66:
			self.ms = "You feel a little bummed, but tomorrow is another day."
		if self.mood >= 66 and self.mood < 100:
			self.ms = "You feel pretty great today."
		if self.mood >= 100:
			self.ms = "You are positively bursting with confidence!"
		return self.ms

	# Set knowledge status message
	def knowledge_status(self):
		if self.knowledge < 33:
			self.ks = "You feel deeply ignorant."
		if self.knowledge >= 33 and self.knowledge < 66:
			self.ks = "You feel like you know....something.... (...right?)...."
		if self.knowledge >= 66 and self.knowlege < 100:
			self.ks = "You feel like you're learning a lot."
		if self.knowledge >= 100:
			self.ks = "Amazing! You feel like a Python and Django expert!"
		return self.ks

	# Retrieve status messages for all stats
	def user_stats(self):
		self.statuses.clear()
		self.statuses.append(self.energy_status())
		self.statuses.append(self.mood_status())
		self.statuses.append(self.knowledge_status())
		return self.statuses

	# Update user stat values based on choice
	def update_stats(self, energy, mood, knowledge):
		self.energy += energy
		self.mood += mood
		self.knowledge += knowledge
		return self

	def __str(self):
		return self.name

class Quiz(models.Model):
	question = models.CharField(max_length=500)
	answer = models.BooleanField()
	difficulty = models.CharField(max_length=100)

	def __str(self):
		return self.question

class Final(models.Model):
	question = models.CharField(max_length=500)
	answer = models.BooleanField()
	difficulty = models.CharField(max_length=100)

	def __str(self):
		return self.question


# Save User Profile on User create or save
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
	instance.profile.save()
