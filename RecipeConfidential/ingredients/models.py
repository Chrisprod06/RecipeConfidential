from django.db import models


class Category(models.Model):
    """
    Model to describe categories of ingredients
    """

    category_name = models.CharField(max_length=255, blank=True, unique=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class Measurement(models.Model):
    """
    Model to describe type of measurements of ingredients
    """

    symbol = models.CharField(max_length=10)
    measurement_name = models.CharField(max_length=255)

    def __str__(self):
        return self.symbol


class Ingredient(models.Model):
    """
    Model to describe ingredients that will be used in the recipes
    """

    ingredient_name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    measurement = models.ForeignKey(Measurement, on_delete=models.RESTRICT)
    quantity = models.FloatField(blank=False)
    extra_notes = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.ingredient_name
