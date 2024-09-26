from django.shortcuts import render, redirect # type: ignore
from .forms import ProductoForm, CategoriaForm, ClienteForm
from .models import Producto

def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm()
    return render(request, 'agregar_producto.html', {'form': form})

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'lista_productos.html', {'productos': productos})

def buscar_producto(request):
    query = request.GET.get('q')

    if query: 
        resultados = Producto.objects.filter(nombre__icontains=query)
    else:
        resultados = [] 

    return render(request, 'buscar_producto.html', {'resultados': resultados, 'query': query})

def agregar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = CategoriaForm()
    return render(request, 'app_principal/agregar_categoria.html', {'form': form})
