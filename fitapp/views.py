from rest_framework import viewsets

from fitapp.models import Ingredient
from fitapp.serializers import IngredientSerializer


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
