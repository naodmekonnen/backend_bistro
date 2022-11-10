from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views import View
from . models import Category,Cuisine,Menu_Items
from django.core.serializers import serialize
import json



def get_data(request):
    data = [
            i.json() for i in Menu_Items.objects.all()
        ]
    return HttpResponse(json.dumps(data), content_type='application/json')

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


 














#   data = []
#         items = list(Menu_Items.objects.values())
#         for item in items:
#             data.append({
#                 'entree':item.entree,
#                 'description':item.description,
#                 'price': item.price,
#                 'spice_level':item.spice_level,
#                 'cuisine':model_to_dict(cuisine.objects.get(id=cuisine_id)),
#                 'category':model_to_dict(category.objects.get(id=category_id)),
#             })