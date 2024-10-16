from fitapp.models import User
from django.test import TransactionTestCase

from fitapp.models import Ingredient
from fitapp.serializers import IngredientSerializer


class IngredientSerializerTest(TransactionTestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="12345")

    def test_create_valid_ingredient(self):
        ingredient_data = {"user": self.user.id, "title": "Apple", "calories": 52}
        serializer = IngredientSerializer(data=ingredient_data)
        self.assertTrue(serializer.is_valid())
        ingredient = serializer.save()

        self.assertEqual(Ingredient.objects.count(), 1)
        self.assertEqual(ingredient.title, "Apple")
        self.assertEqual(ingredient.calories, 52)

    def test_create_invalid_ingredient(self):
        invalid_data = {"user": self.user.id, "title": "", "calories": "invalid"}
        serializer = IngredientSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())

        self.assertEqual(Ingredient.objects.count(), 0)
