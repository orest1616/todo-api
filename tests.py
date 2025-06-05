from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from tasks.models import Task
from rest_framework_simplejwt.tokens import RefreshToken

class TaskAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='admin', password='admin')
        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {str(refresh.access_token)}')

    def test_create_task(self):
        data = {
            "title": "Check API",
            "description": "This is a test task",
            "due_date": "2025-12-31",
            "status": "pending"
        }
        response = self.client.post('/api/tasks/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_tasks(self):
        Task.objects.create(title="Test 1", user=self.user)
        Task.objects.create(title="Test 2", user=self.user)
        response = self.client.get('/api/tasks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_update_task(self):
        task = Task.objects.create(title="Test", user=self.user)
        data = {"title": "Updated", "status": "completed"}
        response = self.client.put(f'/api/tasks/{task.id}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Updated")

    def test_delete_task(self):
        task = Task.objects.create(title="To be deleted", user=self.user)
        response = self.client.delete(f'/api/tasks/{task.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
