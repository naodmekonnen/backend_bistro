from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from . models import Category,Cuisine,Menu_Items


# self has to be passed in since it's class based
class DataView(View):
    def get(self, request):
        menu = Menu_Items.objects.all()
        return JsonResponse(menu, safe=false)
        