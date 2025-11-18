from django.shortcuts import render
from django.views.generic import ListView as listView, DetailView
from .models import Pijama


# Create your views here.

class listproducts(listView):
    model = Pijama
    template_name = 'home.html'
    context_object_name = 'productos'
    
class detailproduct(DetailView):
    model = Pijama
    template_name = 'detail_product.html'
    context_object_name = 'producto'
    


