from django.contrib import admin
from . models import Category,Cuisine,Menu_Items

# Register your models here.

admin.site.register(Menu_Items)
admin.site.register(Category)
admin.site.register(Cuisine)