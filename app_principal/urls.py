from django.urls import path # type: ignore
from .views import agregar_producto, lista_productos, buscar_producto

urlpatterns = [
    path('agregar-producto/', agregar_producto, name='agregar_producto'),
    path('lista-productos/', lista_productos, name='lista_productos'),
    path('buscar-producto/', buscar_producto, name='buscar_producto'),
]
