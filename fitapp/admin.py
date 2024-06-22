from django.contrib import admin
from fitapp.models import Ingredient, Profile


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ("title", "calories", "created_at", "user")


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("birth_date", "user")
