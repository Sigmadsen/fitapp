from rest_framework import serializers

from fitapp.models import Ingredient


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ["id", "user", "title", "calories", "created_at"]
