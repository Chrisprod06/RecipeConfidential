from django.contrib import admin
from ingredients.models import *


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "measurement", "quantity", "extra_notes")
    list_filter = ("category",)
    search_fields = ("name",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("key", "description")


@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    list_display = ("key", "name")
