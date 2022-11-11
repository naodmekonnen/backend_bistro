from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views import View
from . models import Category,Cuisine,MenuItem
from django.core.serializers import serialize
import json
import csv


# fetch and return json serialized data from API
def get_data(request):
    data = [
            i.json() for i in MenuItem.objects.all()
        ]
    return HttpResponse(json.dumps(data), content_type='application/json')


def indian(request):
    indian = list(MenuItem.objects.filter(cuisine=3).values())
    return JsonResponse(indian, safe=False)

def american(request):
    american = list(MenuItem.objects.filter(cuisine=1).values())
    return JsonResponse(american, safe=False)

def italian(request):
    italian = list(MenuItem.objects.filter(cuisine=2).values())
    return JsonResponse(italian, safe=False)

def mediterranean(request):
    mediterranean = list(MenuItem.objects.filter(cuisine=5).values())
    return JsonResponse(mediterranean, safe=False)


def export_to_csv(request):
    items = MenuItem.objects.all()
    response = HttpResponse(content_type='text/csv')
    writer = csv.writer(response)
    writer.writerow(['entree','description','spice_level','price','cuisine','category'])
    item_fields= items.values_list('entree','description','spice_level','price','cuisine','category')

    for item in item_fields:
        writer.writerow(item)

    return response


# class DataView(View):
#      def get(self, request):
        # menu =  json.loads(serialize("json", Menu_Items.objects.all()))
        # return JsonResponse(menu, safe=False)
        
        # data = list(Menu_Items.objects.values())
        # return JsonResponse(data, safe=False)

        # data = [
        #     i.json() for i in Menu_Items.objects.all()
        # ]

        # return
        # HttpResponse(json.dumps(data), content_type='application/json')


 













