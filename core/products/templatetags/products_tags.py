from django import template
from products.models import (
    MenProducts, WomanProducts, KidProducts, Accessories)
from decimal import Decimal

register = template.Library()

@register.simple_tag()
def popular_men_products():
    """In this function we obtained most popular men's products"""
    products = MenProducts.objects.filter(approved = True)
    products = sorted(products, key=lambda x:x.counted_views, reverse=True)[:3]
    return products

@register.simple_tag()
def popular_women_products():
    """In this function we obtained most popular women's products"""
    products = WomanProducts.objects.filter(approved = True)
    products = sorted(products, key=lambda x:x.counted_views, reverse=True)[:3]
    return products

@register.simple_tag()
def popular_kids_products():
    """In this function we obtained most popular kids products"""
    products = KidProducts.objects.filter(approved = True)
    products = sorted(products, key=lambda x:x.counted_views, reverse=True)[:3]
    return products

@register.simple_tag()
def popular_accessories():
    """In this function we obtained most popular accessories"""
    products = Accessories.objects.filter(approved = True)
    products = sorted(products, key=lambda x:x.counted_views, reverse=True)[:3]
    return products


@register.simple_tag(name="calculated_price")
def function(price, discount):
    """This function calculates discounted price"""
    try:
        percentage_discount = discount * Decimal("0.01")
        discounted_price =  price - (price * percentage_discount)
        assert 0 <= discounted_price <= price
        return int(discounted_price)
    except AssertionError:
        return price