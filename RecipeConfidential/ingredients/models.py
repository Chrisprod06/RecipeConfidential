from django.db import models


class Category(models.Model):
    """
    Model to describe categories of ingredients
    """
    # Key
    key = models.CharField(max_length=30, blank=False, unique=True)
    # Description
    description = models.CharField(max_length=255, blank=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.key


class Measurement(models.Model):
    """
    Model to describe type of measurements of ingredients
    """
    # key
    key = models.CharField(max_length=10)
    # Name
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.key


class Ingredient(models.Model):
    """
    Model to describe ingredients that will be used in the recipes
    """
    # Name
    name = models.CharField(max_length=255)

    # Category
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)

    # Measurement
    measurement = models.ForeignKey(Measurement, on_delete=models.RESTRICT)

    # Quantity
    quantity = models.FloatField(blank=False)

    # Extra notes
    extra_notes = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.name
