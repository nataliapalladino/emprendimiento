from django.urls import path
from .views import *

urlpatterns = [
    path('', listproducts.as_view(), name='lista_productos'),
    path("product/<int:pk>/", detailproduct.as_view(), name="detalle_producto"),
]