from django.contrib import admin
from ingredients.models import *


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ("ingredient_name", "category", "measurement", "quantity", "extra_notes")
    list_filter = ("category",)
    search_fields = ("ingredient_name",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("category_name",)


@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    list_display = ("symbol", "measurement_name")
