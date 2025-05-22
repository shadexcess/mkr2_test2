from django.test import TestCase
from django.urls import reverse
from .models import Task

class TaskListViewTest(TestCase):
    def setUp(self):
        Task.objects.create(title='Test Task 1', description='First task', completed=False)
        Task.objects.create(title='Test Task 2', description='Second task', completed=True)

    def test_task_list_view_status_code(self):
        response = self.client.get(reverse('task_list'))
        self.assertEqual(response.status_code, 200)

    def test_task_list_view_uses_correct_template(self):
        response = self.client.get(reverse('task_list'))
        self.assertTemplateUsed(response, 'myapp/task_list.html')

    def test_task_list_view_displays_tasks(self):
        response = self.client.get(reverse('task_list'))
        self.assertContains(response, 'Test Task 1')
        self.assertContains(response, 'Test Task 2')