
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from .models import Team, Activity, Leaderboard, Workout

User = get_user_model()

class APIRootTest(APITestCase):
	def test_api_root(self):
		response = self.client.get(reverse('api-root'))
		self.assertEqual(response.status_code, status.HTTP_200_OK)

class UserTests(APITestCase):
	def test_list_users(self):
		User.objects.create_user(username='testuser', email='test@example.com', password='testpass')
		response = self.client.get(reverse('user-list'))
		self.assertEqual(response.status_code, status.HTTP_200_OK)

class TeamTests(APITestCase):
	def test_list_teams(self):
		Team.objects.create(name='Test Team')
		response = self.client.get(reverse('team-list'))
		self.assertEqual(response.status_code, status.HTTP_200_OK)

class ActivityTests(APITestCase):
	def test_list_activities(self):
		Activity.objects.create(user='testuser', activity_type='Run', duration=10, team='Test Team')
		response = self.client.get(reverse('activity-list'))
		self.assertEqual(response.status_code, status.HTTP_200_OK)

class LeaderboardTests(APITestCase):
	def test_list_leaderboard(self):
		Leaderboard.objects.create(user='testuser', team='Test Team', points=50)
		response = self.client.get(reverse('leaderboard-list'))
		self.assertEqual(response.status_code, status.HTTP_200_OK)

class WorkoutTests(APITestCase):
	def test_list_workouts(self):
		Workout.objects.create(name='Test Workout', description='desc', suggested_for='Test Team')
		response = self.client.get(reverse('workout-list'))
		self.assertEqual(response.status_code, status.HTTP_200_OK)
