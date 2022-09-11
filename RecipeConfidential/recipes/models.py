from django.db import models
from ingredients.models import Ingredient
from methods.models import Method


class Category(models.Model):
    """
    Model to describe categories of recipes
    """
    category_name = models.CharField(max_length=255, blank=False, unique=True)

    def __str__(self):
        return self.category_name


class Recipe(models.Model):
    """
    Model to describe recipes
    """
    difficulty_choices = (
        ("BEGINNER", "Beginner"),
        ("INTERMEDIATE", "Intermediate"),
        ("EXPERT", "EXPERT")
    )

    recipe_name = models.CharField(max_length=255, blank=False, unique=True)
    category = models.CharField(max_length=255, blank=False, unique=True)
    difficulty = models.CharField(max_length=20,choices=difficulty_choices, blank=False)
    time_needed = models.FloatField(help_text="Time is measured in hours", blank=False)
    serves = models.IntegerField(default=2, blank=False)
    ingredients = models.ManyToManyField(Ingredient, blank=False)
    method = models.ForeignKey(Method, blank=False, on_delete=models.RESTRICT)

    def __str__(self):
        return self.recipe_name
