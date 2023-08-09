from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import (
     MenProducts, WomanProducts, KidProducts, Accessories)

# Create your views here.

def men_products_view(request):
    """This function defines instructions of men products and how to show in templates"""
    products = MenProducts.objects.filter(approved=True)
    context = {"products":products}
    return render(request, "products/men-products.html",context)


def women_products_view(request):
    """This function defines instructions of women products and how to show in templates"""
    products = WomanProducts.objects.filter(approved=True)
    context = {"products":products}
    return render(request, "products/women-products.html",context)


def kids_products_view(request):
    """This function defines instructions of kids products and how to show in templates"""
    products = KidProducts.objects.filter(approved=True)
    context = {"products":products}
    return render(request, "products/kids-products.html",context)


def accessories_view(request):
    """This function defines instructions of accessories and how to show in templates"""
    products = Accessories.objects.filter(approved=True)
    context = {"products":products}
    return render(request, "products/accessories.html",context)


def single_men_product(request,name):
    """This function used for connecting men_products_view to single-product"""
    product = get_object_or_404(MenProducts, model_name = name, approved=True)
    product.counted_views += 1
    product.save()
    context = {"product":product}
    return render(request, "products/single-product.html",context)

def single_women_product(request,name):
    """This function used for connecting women_products_view to single-product"""
    product = get_object_or_404(WomanProducts, model_name = name, approved=True)
    product.counted_views += 1
    product.save()
    context = {"product":product}
    return render(request, "products/single-product.html",context)

def single_kids_product(request,name):
    """This function used for connecting kids_products_view to single-product"""
    product = get_object_or_404(KidProducts, model_name = name, approved=True)
    product.counted_views += 1
    product.save()
    context = {"product":product}
    return render(request, "products/single-product.html",context)

def single_accessory_product(request,name):
    """This function used for connecting accessories_view to single-product"""
    product = get_object_or_404(Accessories, model_name = name, approved=True)
    product.counted_views += 1
    product.save()
    context = {"product":product}
    return render(request, "products/single-product.html",context)