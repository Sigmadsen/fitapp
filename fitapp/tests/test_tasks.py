from django.test import TransactionTestCase
from django.contrib.auth.models import User
from fitapp.models import TrainingTask
from fitapp.tasks import my_daily_training, my_daily_training_for_user
from unittest.mock import patch


class CeleryTasksTransactionTestCase(TransactionTestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username="user1", password="password")
        self.user2 = User.objects.create_user(username="user2", password="password")

        self.task1 = TrainingTask.objects.create(
            description="Task 1", repeat=True, user=self.user1
        )
        self.task2 = TrainingTask.objects.create(
            description="Task 2", repeat=True, user=self.user2
        )

    @patch("fitapp.tasks.my_daily_training_for_user.delay")
    def test_my_daily_training(self, mock_my_daily_training_for_user):
        # Run task
        my_daily_training()

        # We check that the task `my_daily_training_for_user` was called for each user
        self.assertEqual(
            mock_my_daily_training_for_user.call_count, User.objects.count()
        )
        mock_my_daily_training_for_user.assert_any_call(self.user1.id)
        mock_my_daily_training_for_user.assert_any_call(self.user2.id)

    @patch("fitapp.models.TrainingTask.objects.create")
    def test_my_daily_training_for_user(self, mock_create_task):
        # Run task by user_id
        my_daily_training_for_user(self.user1.id)

        # Get the number of repeating tasks for a user
        repeat_tasks_count = TrainingTask.objects.filter(
            repeat=True, user=self.user1
        ).count()

        # Check that the create method was called the correct number of times
        self.assertEqual(mock_create_task.call_count, repeat_tasks_count)

        # We check that at least one call was made with the correct parameters.
        mock_create_task.assert_any_call(
            user=self.user1, description=self.task1.description
        )
