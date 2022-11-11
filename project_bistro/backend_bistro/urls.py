from django.urls import path
from . import views

urlpatterns = [
    path('menu/', views.get_data),
    path('csv/', views.export_to_csv),
    path('indian/', views.indian),
    path('american/', views.american),
    path('italian/', views.italian),
    path('mediterranean/', views.mediterranean)



]