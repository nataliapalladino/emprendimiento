from django.urls import path
from .views import *

urlpatterns = [
    path('', listproducts.as_view(), name='lista_productos'),
    path("product/<int:pk>/", detailproduct.as_view(), name="detalle_producto"),
    path('create/', PijamaCreateView.as_view(), name='pijama_create'),
    path('product/<int:pk>/update/', PijamaUpdateView.as_view(), name='pijama_update'),
    path('product/<int:pk>/delete/', PijamaDeleteView.as_view(), name='pijama_delete'),
]