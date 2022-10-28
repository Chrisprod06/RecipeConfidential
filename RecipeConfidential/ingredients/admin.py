from django.contrib import admin
from ingredients.models import *


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ("ingredient_name", "category", "measurement", "quantity", "extra_notes")
    list_filter = ("category",)
    search_fields = ("ingredient_name",)


@admin.register(IngredientCategory)
class IngredientCategoryAdmin(admin.ModelAdmin):
    list_display = ("ingredient_category_name",)


@admin.register(MeasurementCategory)
class MeasurementCategoryAdmin(admin.ModelAdmin):
    list_display = ("measurement_category_name",)


@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    list_display = ("symbol", "measurement_name", "category")
