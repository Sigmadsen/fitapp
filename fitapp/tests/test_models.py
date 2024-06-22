from django.test import TestCase
from django.contrib.auth.models import User
from fitapp.models import Ingredient


class IngredientModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.ingredient = Ingredient.objects.create(
            user=self.user, title="This is a test ingredient.", calories=250
        )

    def test_ingredient_creation(self):
        self.assertEqual(self.ingredient.title, "This is a test ingredient.")
        self.assertEqual(self.ingredient.calories, 250)
        self.assertEqual(self.ingredient.user.username, "testuser")

    def test_ingredient_str(self):
        self.assertEqual(str(self.ingredient), "This is a test ingredient")

    def test_ingredient_auto_now_add(self):
        self.assertIsNotNone(self.ingredient.created_at)
