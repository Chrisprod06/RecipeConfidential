from django.db import models
from recipes.models import Recipe


class Category(models.Model):
    """
    Model to describe the category of which a step belongs
    Ex. preparation
    """
    category_name = models.CharField(max_length=255, blank=False, unique=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.category_name


class Step(models.Model):
    """
    Model to describe individual steps in a method of execution
    """
    order_number = models.SmallIntegerField(default=10, blank=False)
    category = models.ForeignKey(Category, on_delete=models.RESTRICT, blank=False)
    description = models.CharField(max_length=500, blank=False)
    extra_notes = models.CharField(max_length=255, blank=True)


class Method(models.Model):
    """
    Model to describe method of execution for a recipe
    """
    # recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    steps = models.ManyToManyField(Step)
