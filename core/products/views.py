from django.shortcuts import render

# Create your views here.

def products_view(request):
    return render(request, "products/products.html")

def single_product(request):
    return render(request, "products/single-product.html")