from django.urls import path
from .views import (
    products_view, single_product
    )

app_name = "products"

urlpatterns = [
    path('', products_view, name = "products"),
    path('single/', single_product, name = "single")
]