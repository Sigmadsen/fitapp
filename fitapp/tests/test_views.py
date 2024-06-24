from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TransactionTestCase
from rest_framework import status
from rest_framework.test import APIClient

from fitapp.models import Ingredient


class IngredientViewSetTestCase(TransactionTestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.list_url = reverse("ingredient-list")
        self.ingredient = Ingredient.objects.create(
            user=self.user, title="Apple", calories=52
        )

    def test_list_ingredients(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_retrieve_ingredient(self):
        detail_url = reverse("ingredient-detail", args=[self.ingredient.pk])
        response = self.client.get(detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Apple")

    def test_create_ingredient(self):
        new_ingredient_data = {"user": self.user.id, "title": "Banana", "calories": 89}
        response = self.client.post(self.list_url, new_ingredient_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Ingredient.objects.count(), 2)

    def test_update_ingredient(self):
        detail_url = reverse("ingredient-detail", args=[self.ingredient.pk])
        updated_data = {"user": self.user.id, "title": "Orange", "calories": 47}
        response = self.client.put(detail_url, updated_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.ingredient.refresh_from_db()
        self.assertEqual(self.ingredient.title, "Orange")

    def test_delete_ingredient(self):
        detail_url = reverse("ingredient-detail", args=[self.ingredient.pk])
        response = self.client.delete(detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Ingredient.objects.count(), 0)
