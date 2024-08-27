from django.urls import path, include
from rest_framework.routers import DefaultRouter

from fitapp.views import IngredientViewSet, TaskViewSet

router = DefaultRouter()
router.register(r"ingredients", IngredientViewSet)
router.register(r"tasks", TaskViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
]
