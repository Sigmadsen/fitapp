from rest_framework import viewsets

from fitapp.models import Ingredient, TrainingTask
from fitapp.serializers import IngredientSerializer, TaskSerializer


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class TaskViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TrainingTask.objects.all()
    serializer_class = TaskSerializer
