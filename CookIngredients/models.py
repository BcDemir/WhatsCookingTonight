from django.db import models


# Create your models here.
# will create fridge table to store ingredient
# Recipe class for recipes
# Has to store all this data in a txt file

class Recipe(models.Model):
    name = models.CharField(max_length=200, primary_key=True)
    main_ingredient_1 = models.CharField(max_length="100", null=True)
    main_ingredient_2 = models.CharField(max_length="100", null=True)
    main_ingredient_3 = models.CharField(max_length="100", null=True)
    main_ingredient_4 = models.CharField(max_length="100", null=True)
    main_ingredient_5 = models.CharField(max_length="100", null=True)
    main_ingredient_6 = models.CharField(max_length="100", null=True)
    optional_ingredient_1 = models.CharField(max_length="100", null=True)
    optional_ingredient_2 = models.CharField(max_length="100", null=True)
    optional_ingredient_3 = models.CharField(max_length="100", null=True)
    optional_ingredient_4 = models.CharField(max_length="100", null=True)
    optional_ingredient_5 = models.CharField(max_length="100", null=True)
    optional_ingredient_6 = models.CharField(max_length="100", null=True)
    instruction = models.CharField(max_length="500")

    def __str__(self):
        return self.name, " Instructions:\n", self.instruction


class Ingredients(models.Model):
    units = [
        ("Kg", "Kilo"),
        ("pc", "Piece"),
        ("L", "Litre"),
    ]
    name = models.CharField(max_length=120, primary_key=True)
    quantity = models.IntegerField(default=0)
    unit = models.CharField(max_length="2", choices=units)

    def __str__(self):
        return "You have ", self.quantity, " ", self.unit, " of ", self.name, "/s"
