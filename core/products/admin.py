from django.contrib import admin
from .models import (
    MenProducts, WomanProducts, KidProducts,
    Accessories, Styles, Comment
    )
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.
@admin.register(MenProducts)
class MenProductsAdmin(SummernoteModelAdmin):
    date_hierarchy = "created_date"
    summernote_fields = ('introduction',)
    empty_value_display = "-empty-"
    list_display = ["model_name", "price", "discount_Percentage", "advertiser", "stock", "counted_views", "approved"]
    fields = ["model_name", "image", "introduction", "advertiser", "price",
               "discount_Percentage", "stock", "counted_views", "style", "approved", "published_date"]
    list_filter = ("style", "approved")
    search_fields = ["model_name", "advertiser", "style"]

@admin.register(WomanProducts)
class WomanProductsAdmin(SummernoteModelAdmin):
    date_hierarchy = "created_date"
    summernote_fields = ('introduction',)
    empty_value_display = "-empty-"
    list_display = ["model_name", "price", "discount_Percentage", "advertiser", "stock", "counted_views", "approved"]
    fields = ["model_name", "image", "introduction", "advertiser", "price",
               "discount_Percentage", "stock", "counted_views", "style", "approved", "published_date"]
    list_filter = ("style", "approved")
    search_fields = ["model_name", "advertiser", "style"]
    
@admin.register(KidProducts)
class KidProductsAdmin(SummernoteModelAdmin):
    date_hierarchy = "created_date"
    summernote_fields = ('introduction',)
    empty_value_display = "-empty-"
    list_display = ["model_name", "price", "discount_Percentage", "advertiser", "stock", "counted_views", "approved"]
    fields = ["model_name", "image", "introduction", "advertiser", "price",
               "discount_Percentage", "stock", "counted_views", "style", "approved", "published_date"]
    list_filter = ("style", "approved")
    search_fields = ["model_name", "advertiser", "style"]
    
@admin.register(Accessories)
class AccessoriesAdmin(SummernoteModelAdmin):
    date_hierarchy = "created_date"
    summernote_fields = ('introduction',)
    empty_value_display = "-empty-"
    list_display = ["model_name", "price", "discount_Percentage", "advertiser", "stock", "counted_views", "approved"]
    fields = ["model_name", "image", "introduction", "advertiser", "price",
               "discount_Percentage", "stock", "counted_views", "approved", "published_date"]
    list_filter = ("approved",)
    search_fields = ["model_name", "advertiser"]

admin.site.register(Styles)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('email','content_type','approved','created_date')
    list_filter = ('email','approved')
    search_fields = ('email','comment')









