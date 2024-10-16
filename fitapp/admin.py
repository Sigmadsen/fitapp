from django.contrib import admin
from fitapp.models import Ingredient


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ("title", "calories", "created_at", "user")
