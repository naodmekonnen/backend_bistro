from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from . models import Category,Cuisine,Menu_Items
from django.core.serializers import serialize
import json

class DataView(View):
    def get(self, request):
        menu =  json.loads(serialize("json", Menu_Items.objects.all()))
        return JsonResponse(menu, safe=False)
        

