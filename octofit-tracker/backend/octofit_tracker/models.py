
from djongo import models
from django.contrib.auth.models import AbstractUser

# Custom user model (if needed, otherwise use default)
# class User(AbstractUser):
#     pass

class Team(models.Model):
	name = models.CharField(max_length=100, unique=True)
	def __str__(self):
		return self.name

class Activity(models.Model):
	user = models.CharField(max_length=100)
	activity_type = models.CharField(max_length=100)
	duration = models.IntegerField()
	team = models.CharField(max_length=100)
	def __str__(self):
		return f"{self.user} - {self.activity_type}"

class Leaderboard(models.Model):
	user = models.CharField(max_length=100)
	team = models.CharField(max_length=100)
	points = models.IntegerField()
	def __str__(self):
		return f"{self.user} - {self.points}"

class Workout(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField()
	suggested_for = models.CharField(max_length=100)
	def __str__(self):
		return self.name
