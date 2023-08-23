from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.core.paginator import (
    Paginator, EmptyPage, PageNotAnInteger)
from .models import (
     MenProducts, WomanProducts, KidProducts, Accessories, Comment)
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import CommentForm
from django.contrib.contenttypes.models import ContentType
# Create your views here.

def men_products_view(request):
    """This function defines instructions of men products and how to show in templates"""
    products = MenProducts.objects.filter(approved="Approved")
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
    products = WomanProducts.objects.filter(approved="Approved")
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
    products = KidProducts.objects.filter(approved="Approved")
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
    products = Accessories.objects.filter(approved="Approved")
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
    """This function defines how to show products in single-product template"""
    if request.user.is_authenticated:
        if request.method == "GET":
            """This function used for connecting to the single-product with insertet name."""
            if kwargs.get('men_product') is not None:
                content_type = ContentType.objects.get_for_model(MenProducts)
                product = get_object_or_404(MenProducts, model_name = kwargs['men_product'], approved="Approved")
            if kwargs.get('women_product') is not None:
                content_type = ContentType.objects.get_for_model(WomanProducts)
                product = get_object_or_404(WomanProducts, model_name = kwargs['women_product'], approved="Approved")
            if kwargs.get('kids_product') is not None:
                content_type = ContentType.objects.get_for_model(KidProducts)
                product = get_object_or_404(KidProducts, model_name = kwargs['kids_product'], approved="Approved")
            if kwargs.get('accessory') is not None:
                content_type = ContentType.objects.get_for_model(Accessories)
                product = get_object_or_404(Accessories, model_name = kwargs['accessory'], approved="Approved")
            object_id = product.id
            comments = Comment.objects.filter(content_type=content_type, object_id=object_id, approved="Approved")
            product.counted_views += 1
            product.save()
            context = {"product":product, "comments":comments}
            return render(request, "products/single-product.html",context)
        if request.method == "POST":
            if kwargs.get('women_product') is not None:
                form = CommentForm(request.POST)
                if form.is_valid():
                    new_comment = Comment()
                    new_comment.email = form.cleaned_data['email']
                    new_comment.comment = form.cleaned_data['comment']
                    new_comment.content_type = ContentType.objects.get_for_model(WomanProducts)
                    new_comment.object_id = form.cleaned_data['object_id']
                    new_comment.save()
                    messages.success(request, "Your comment submitted successfully,it appears in a few minutes.")
                    return HttpResponseRedirect(request.POST.get('next'), {"form":CommentForm(request.POST)})
                else:
                    messages.error(request,"Your comment didn't submit.")
                    return HttpResponseRedirect(request.POST.get('next'),{"form":CommentForm()})
            if kwargs.get('men_product') is not None:
                form = CommentForm(request.POST)
                if form.is_valid():
                    new_comment = Comment()
                    new_comment.email = form.cleaned_data['email']
                    new_comment.comment = form.cleaned_data['comment']
                    new_comment.content_type = ContentType.objects.get_for_model(MenProducts)
                    new_comment.object_id = form.cleaned_data['object_id']
                    new_comment.save()
                    messages.success(request, "Your comment submitted successfully,it appears in a few minutes.")
                    return HttpResponseRedirect(request.POST.get('next'), {"form":CommentForm(request.POST)})
                else:
                    messages.error(request,"Your comment didn't submit.")
                    return HttpResponseRedirect(request.POST.get('next'),{"form":CommentForm()})
            if kwargs.get('kids_product') is not None:
                form = CommentForm(request.POST)
                if form.is_valid():
                    new_comment = Comment()
                    new_comment.email = form.cleaned_data['email']
                    new_comment.comment = form.cleaned_data['comment']
                    new_comment.content_type = ContentType.objects.get_for_model(KidProducts)
                    new_comment.object_id = form.cleaned_data['object_id']
                    new_comment.save()
                    messages.success(request, "Your comment submitted successfully,it appears in a few minutes.")
                    return HttpResponseRedirect(request.POST.get('next'), {"form":CommentForm(request.POST)})
                else:
                    messages.error(request,"Your comment didn't submit.")
                    return HttpResponseRedirect(request.POST.get('next'),{"form":CommentForm()})
            if kwargs.get('accessory') is not None:
                form = CommentForm(request.POST)
                if form.is_valid():
                    new_comment = Comment()
                    new_comment.email = form.cleaned_data['email']
                    new_comment.comment = form.cleaned_data['comment']
                    new_comment.content_type = ContentType.objects.get_for_model(Accessories)
                    new_comment.object_id = form.cleaned_data['object_id']
                    new_comment.save()
                    messages.success(request, "Your comment submitted successfully,it appears in a few minutes.")
                    return HttpResponseRedirect(request.POST.get('next'), {"form":CommentForm(request.POST)})
                else:
                    messages.error(request,"Your comment didn't submit.")
                    return HttpResponseRedirect(request.POST.get('next'),{"form":CommentForm()})
    messages.info(request, "You must login first to see products details.")
    return HttpResponseRedirect(reverse('accounts:login'))