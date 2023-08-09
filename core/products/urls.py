from django.urls import path
from .views import (
    men_products_view, women_products_view, 
    kids_products_view, accessories_view, single_men_product,
    single_women_product, single_kids_product,single_accessory_product,
    )

app_name = "products"

urlpatterns = [
    path('men-products/', men_products_view, name = "men-products"),
    path('men-products/<str:name>', single_men_product, name = "men-single"),
    path('women-products/', women_products_view, name = "women-products"),
    path('women-products/<str:name>', single_women_product, name = "women-single"),
    path('kids-products/', kids_products_view, name = "kids-products"),
    path('kids-products/<str:name>',single_kids_product, name = "kids-single"),
    path('accessories/', accessories_view, name = "accessories"),
    path('accessories/<str:name>', single_accessory_product, name = "accessories-single"),
]