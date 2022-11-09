from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)

class Cuisine(models.Model):
    name = models.CharField(max_length=50)


class Menu_Items(models.Model):
    entree = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    spice_level = models.IntegerField(max_length=50)
    price = models.IntegerField(max_length=50)
    cuisine = models.ForeignKey(Cuisine)
    category = models.ForeignKey(Category)