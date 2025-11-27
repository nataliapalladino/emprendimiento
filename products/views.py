from django.shortcuts import render
from django.views.generic import ListView as listView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
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
    

class PijamaCreateView(CreateView):
    model = Pijama
    template_name = 'create_product.html'
    success_url = reverse_lazy('lista_productos')  # Ajusta este nombre de URL
    fields = [
        'nombre', 
        'descripcion', 
        'precio', 
        'imagen', 
        
    ]
    
class PijamaUpdateView(UpdateView):
    model = Pijama
    template_name = 'create_product.html'
    success_url = reverse_lazy('lista_productos')  # Ajusta este nombre de URL
    fields = [
        'nombre', 
        'descripcion', 
        'precio', 
        'imagen', 
        
        'disponible'
    ]
    
class PijamaDeleteView(DeleteView):
    model = Pijama
    template_name = 'delete_product.html'
    success_url = reverse_lazy('lista_productos')
