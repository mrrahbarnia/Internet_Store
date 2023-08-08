from django.contrib import admin
from .models import (
    MenProducts, WomanProducts, KidProducts,
    Accessories, Styles, Comment
    )
# Register your models here.
@admin.register(MenProducts)
class MenProductsAdmin(admin.ModelAdmin):
    date_hierarchy = "created_date"
    empty_value_display = "-empty-"
    list_display = ["model_name", "price", "discount", "advertiser", "stock"]
    fields = ["model_name", "image", "introduction", "advertiser", "price",
               "discount", "stock", "style", "approved", "published_date"]
    list_filter = ("style", "approved")
    search_fields = ["model_name", "advertiser", "style"]

@admin.register(WomanProducts)
class WomanProductsAdmin(admin.ModelAdmin):
    date_hierarchy = "created_date"
    empty_value_display = "-empty-"
    list_display = ["model_name", "price", "discount", "advertiser", "stock"]
    fields = ["model_name", "image", "introduction", "advertiser", "price",
               "discount", "stock", "style", "approved", "published_date"]
    list_filter = ("style", "approved")
    search_fields = ["model_name", "advertiser", "style"]
    
@admin.register(KidProducts)
class KidProductsAdmin(admin.ModelAdmin):
    date_hierarchy = "created_date"
    empty_value_display = "-empty-"
    list_display = ["model_name", "price", "discount", "advertiser", "stock"]
    fields = ["model_name", "image", "introduction", "advertiser", "price",
               "discount", "stock", "style", "approved", "published_date"]
    list_filter = ("style", "approved")
    search_fields = ["model_name", "advertiser", "style"]
    
@admin.register(Accessories)
class AccessoriesAdmin(admin.ModelAdmin):
    date_hierarchy = "created_date"
    empty_value_display = "-empty-"
    list_display = ["accessory_name", "price", "discount", "advertiser", "stock"]
    fields = ["accessory_name", "image", "introduction", "advertiser", "price",
               "discount", "stock", "approved", "published_date"]
    list_filter = ("approved",)
    search_fields = ["accessory_name", "advertiser"]

admin.site.register(Styles)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('email','content_type','approved','created_date')
    list_filter = ('email','approved')
    search_fields = ('email','comment')









