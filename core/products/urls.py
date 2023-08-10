from django.urls import path
from .views import (
    men_products_view, women_products_view, 
    kids_products_view, accessories_view, single_product,
    )

app_name = "products"

urlpatterns = [
    path('men-products/', men_products_view, name = "men-products"),
    path('men-products/<str:men_product>', single_product, name = "men-single"),
    path('women-products/', women_products_view, name = "women-products"),
    path('women-products/<str:women_product>', single_product, name = "women-single"),
    path('kids-products/', kids_products_view, name = "kids-products"),
    path('kids-products/<str:kids_product>',single_product, name = "kids-single"),
    path('accessories/', accessories_view, name = "accessories"),
    path('accessories/<str:accessory>', single_product, name = "accessories-single"),
]