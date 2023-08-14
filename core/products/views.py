from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.core.paginator import (
    Paginator, EmptyPage, PageNotAnInteger)
from .models import (
     MenProducts, WomanProducts, KidProducts, Accessories)
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
# Create your views here.

def men_products_view(request):
    """This function defines instructions of men products and how to show in templates"""
    products = MenProducts.objects.filter(approved=True)
    products = Paginator(products, 3)
    page_number = request.GET.get("page")
    try:
        products = products.get_page(page_number)
    except PageNotAnInteger:
        products = products.get_page(1)
    except EmptyPage:
        products = products.get_page(products.num_pages)
    context = {"products":products}
    return render(request, "products/men-products.html",context)


def women_products_view(request):
    """This function defines instructions of women products and how to show in templates"""
    products = WomanProducts.objects.filter(approved=True)
    products = Paginator(products, 3)
    page_number = request.GET.get("page")
    try:
        products = products.get_page(page_number)
    except PageNotAnInteger:
        products = products.get_page(1)
    except EmptyPage:
        products = products.get_page(products.num_pages)
    context = {"products":products}
    return render(request, "products/women-products.html",context)


def kids_products_view(request):
    """This function defines instructions of kids products and how to show in templates"""
    products = KidProducts.objects.filter(approved=True)
    products = Paginator(products, 3)
    page_number = request.GET.get("page")
    try:
        products = products.get_page(page_number)
    except PageNotAnInteger:
        products = products.get_page(1)
    except EmptyPage:
        products = products.get_page(products.num_pages)
    context = {"products":products}
    return render(request, "products/kids-products.html",context)


def accessories_view(request):
    """This function defines instructions of accessories and how to show in templates"""
    products = Accessories.objects.filter(approved=True)
    products = Paginator(products, 3)
    page_number = request.GET.get("page")
    try:
        products = products.get_page(page_number)
    except PageNotAnInteger:
        products = products.get_page(1)
    except EmptyPage:
        products = products.get_page(products.num_pages)
    context = {"products":products}
    return render(request, "products/accessories.html",context)


def single_product(request, **kwargs):
    if request.user.is_authenticated:
        """This function used for connecting to the single-product with insertet name."""
        if kwargs.get('men_product') is not None:
            product = get_object_or_404(MenProducts, model_name = kwargs['men_product'], approved=True)
        if kwargs.get('women_product') is not None:
            product = get_object_or_404(WomanProducts, model_name = kwargs['women_product'], approved=True)
        if kwargs.get('kids_product') is not None:
            product = get_object_or_404(KidProducts, model_name = kwargs['kids_product'], approved=True)
        if kwargs.get('accessory') is not None:
            product = get_object_or_404(Accessories, model_name = kwargs['accessory'], approved=True)
        product.counted_views += 1
        product.save()
        context = {"product":product}
        return render(request, "products/single-product.html",context)
    messages.info(request, "You must login first to see products details.")
    return HttpResponseRedirect(reverse('accounts:login'))