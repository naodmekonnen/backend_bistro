from django.contrib import admin
from . models import Category,Cuisine,MenuItem

# Register your models here.

admin.site.register(MenuItem)
admin.site.register(Category)
admin.site.register(Cuisine)