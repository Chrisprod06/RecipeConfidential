from django.contrib import admin
from methods.models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("category_name",)


@admin.register(Step)
class StepAdmin(admin.ModelAdmin):
    list_display = ("order_number", "category", "description",)

