from rest_framework import serializers

from fitapp.models import Ingredient, TrainingTask


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = [
            "id",
            "user",
            "title",
            "calories",
            "created_at",
        ]


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingTask
        fields = [
            "id",
            "user",
            "description",
            "date_from",
            "date_to",
        ]
