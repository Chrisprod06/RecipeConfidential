from django.db import models


class IngredientCategory(models.Model):
    """
    Model to describe categories of ingredients
    """

    ingredient_category_name = models.CharField(max_length=255, blank=True, unique=True)

    class Meta:
        verbose_name_plural = "Ingredient categories"

    def __str__(self):
        return self.ingredient_category_name


class MeasurementCategory(models.Model):
    """
        Model to describe category of measurements of ingredients

    """
    measurement_category_name = models.CharField(max_length=255, blank=True, unique=True)

    class Meta:
        verbose_name_plural = "Measurement categories"

    def __str__(self):
        return self.measurement_category_name


class Measurement(models.Model):
    """
    Model to describe type of measurements of ingredients
    """

    symbol = models.CharField(max_length=10)
    measurement_name = models.CharField(max_length=255)
    category = models.ForeignKey(MeasurementCategory, on_delete=models.RESTRICT)

    def __str__(self):
        return self.symbol


class Ingredient(models.Model):
    """
    Model to describe ingredients that will be used in the recipes
    """

    ingredient_name = models.CharField(max_length=255)
    category = models.ForeignKey(IngredientCategory, on_delete=models.RESTRICT)
    measurement = models.ForeignKey(Measurement, on_delete=models.RESTRICT)
    quantity = models.FloatField(blank=False)
    extra_notes = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.ingredient_name
