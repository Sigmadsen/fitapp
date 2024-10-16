from django.core.exceptions import ValidationError
from django.test import TransactionTestCase
from fitapp.models import Ingredient, TrainingTask, User


class IngredientModelTest(TransactionTestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.ingredient = Ingredient.objects.create(
            user=self.user, title="This is a test ingredient.", calories=250
        )

    def test_create_ingredient(self):
        second_ingredient = Ingredient.objects.create(
            user=self.user, title="New Ingredient", calories=200
        )

        self.assertEqual(Ingredient.objects.count(), 2)

        self.assertEqual(second_ingredient.title, "New Ingredient")
        self.assertEqual(second_ingredient.calories, 200)
        self.assertEqual(second_ingredient.user.username, "testuser")

    def test_read_ingredient(self):
        ingredient = Ingredient.objects.get(id=self.ingredient.id)
        self.assertEqual(ingredient.title, "This is a test ingredient.")
        self.assertEqual(ingredient.calories, 250)
        self.assertEqual(ingredient.user.username, "testuser")

    def test_update_ingredient(self):
        ingredient = Ingredient.objects.get(id=self.ingredient.id)
        ingredient.title = "Updated Ingredient"
        ingredient.calories = 350
        ingredient.save()

        updated_ingredient = Ingredient.objects.get(id=self.ingredient.id)
        self.assertEqual(updated_ingredient.title, "Updated Ingredient")
        self.assertEqual(updated_ingredient.calories, 350)
        self.assertEqual(ingredient.user.username, "testuser")

    def test_delete_ingredient(self):
        ingredient = Ingredient.objects.get(id=self.ingredient.id)
        ingredient.delete()

        self.assertEqual(Ingredient.objects.count(), 0)

    def test_ingredient_str(self):
        self.assertEqual(str(self.ingredient), "This is a test ingredient")

    def test_ingredient_auto_now_add(self):
        self.assertIsNotNone(self.ingredient.created_at)


class TrainingTaskModelTest(TransactionTestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.task = TrainingTask.objects.create(
            user=self.user,
            description="Initial Task",
        )

    def test_create_task(self):
        task = TrainingTask.objects.create(
            user=self.user, description="New Task", status=True, repeat=True
        )
        self.assertEqual(TrainingTask.objects.count(), 2)
        self.assertEqual(task.description, "New Task")
        self.assertTrue(task.status)
        self.assertTrue(task.repeat)

    def test_read_task(self):
        task = TrainingTask.objects.get(id=self.task.id)
        self.assertEqual(task.description, "Initial Task")
        self.assertFalse(task.status)
        self.assertFalse(task.repeat)

    def test_update_task(self):
        task = TrainingTask.objects.get(id=self.task.id)
        task.description = "Updated Task"
        task.status = True
        task.repeat = True
        task.save()

        updated_task = TrainingTask.objects.get(id=self.task.id)
        self.assertEqual(updated_task.description, "Updated Task")
        self.assertTrue(updated_task.status)
        self.assertTrue(updated_task.repeat)

    def test_delete_task(self):
        task = TrainingTask.objects.get(id=self.task.id)
        task.delete()

        self.assertEqual(TrainingTask.objects.count(), 0)

    def test_create_task_with_repeat_false(self):
        task = TrainingTask.objects.create(
            user=self.user, description="Task 1", repeat=False
        )
        self.assertEqual(TrainingTask.objects.count(), 2)
        self.assertFalse(task.repeat)

    def test_create_task_with_repeat_true(self):
        """
        Creating task with repeat=True should be successfully done if task with this exact description for this user
        does not exist.
        """
        task = TrainingTask.objects.create(
            user=self.user, description="Task 1", repeat=True
        )
        self.assertEqual(TrainingTask.objects.count(), 2)
        self.assertTrue(task.repeat)

    def test_create_task_with_repeat_true_fails_if_exists(self):
        TrainingTask.objects.create(user=self.user, description="Task 1", repeat=True)

        # Create TrainingTask object but don't save it to database
        new_task = TrainingTask(user=self.user, description="Task 1", repeat=True)

        # Check how the validation method `clean()` works manually
        with self.assertRaises(ValidationError):
            new_task.clean()

    def test_create_task_with_same_description_and_repeat_false(self):
        TrainingTask.objects.create(user=self.user, description="Task 1", repeat=True)

        task = TrainingTask.objects.create(
            user=self.user, description="Task 1", repeat=False
        )
        self.assertEqual(TrainingTask.objects.count(), 3)
        self.assertFalse(task.repeat)
