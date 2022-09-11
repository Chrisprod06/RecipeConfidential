from django.contrib import admin
from recipes.models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("category_name",)

    def __str__(self):
        return self.category_name


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ("recipe_name", "category", "difficulty", "time_needed", "serves")
