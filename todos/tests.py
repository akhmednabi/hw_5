from django.test import TestCase
from .models import Todo
from django.contrib.auth.models import User
from django.utils import timezone

class TodoModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.todo = Todo.objects.create(
            title='Test Todo',
            description='This is a test todo item.',
            due_date=timezone.now().date(),
            status=False,
            user=self.user
        )

    def test_todo_creation(self):
        self.assertEqual(self.todo.title, 'Test Todo')
        self.assertEqual(self.todo.description, 'This is a test todo item.')
        self.assertFalse(self.todo.status)
        self.assertEqual(self.todo.user.username, 'testuser')

    def test_todo_str(self):
        self.assertEqual(str(self.todo), 'Test Todo')  # Assuming __str__ method is defined in the model

    def test_todo_due_date(self):
        self.assertEqual(self.todo.due_date, timezone.now().date())  # Check if due_date is set correctly

    def test_todo_status(self):
        self.todo.status = True
        self.todo.save()
        self.assertTrue(self.todo.status)  # Check if status can be updated