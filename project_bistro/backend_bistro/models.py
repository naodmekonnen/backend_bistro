from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__ (self):
        return self.name

class Cuisine(models.Model):
    name = models.CharField(max_length=50)
    def __str__ (self):
        return self.name



class MenuItem(models.Model):
    entree = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    spice_level = models.IntegerField(max_length=50)
    price = models.IntegerField(max_length=50)
    cuisine = models.ForeignKey(Cuisine, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, null=True)

    def __str__ (self):
        return self.entree + ' ' + self.description

    def save(self, *args, **kwargs):
        # self.slug = slugify(self.entree)
        super().save(*args, **kwargs)
        if self.slug is None:
            self.slug = slugify(self.entree)
            self.save()

    def json(self):
        return{
            'entree': self.entree,
            'description':self.description,
            'price':self.price,
            'category':
             {
                'title':self.category.name
                },
                
            'cuisine':
            {
                'title':self.cuisine.name
                }
        }
  
  