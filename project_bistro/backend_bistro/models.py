from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__ (self):
        return self.name

class Cuisine(models.Model):
    name = models.CharField(max_length=50)
    def __str__ (self):
        return self.name


class Menu_Items(models.Model):
    entree = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    spice_level = models.IntegerField(max_length=50)
    price = models.IntegerField(max_length=50)
    cuisine = models.ForeignKey(Cuisine, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__ (self):
        return self.entree + ' ' + self.description

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
  
  