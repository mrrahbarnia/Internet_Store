from django.contrib import admin
from .models import (
    MenProducts, WomanProducts, KidProducts,
    Accessories, Styles, Comment
    )
from django_summernote.admin import SummernoteModelAdmin
from django.utils.html import format_html
# Register your models here.

# ================= This class specifies how to show attributes of men products in admin panel ================= #
@admin.register(MenProducts)
class MenProductsAdmin(SummernoteModelAdmin):
    date_hierarchy = "created_date"
    summernote_fields = ('introduction',)
    empty_value_display = "-empty-"
    list_display = ["model_name", "price", "discount_Percentage", "advertiser", "stock", "counted_views", "status", "_"]
    fields = ["model_name", "image", "introduction", "advertiser", "price",
               "discount_Percentage", "stock", "counted_views", "style", "approved", "published_date"]
    list_filter = ("style", "approved")
    search_fields = ["model_name", "advertiser", "style"]
    list_par_page = 10
    # Furnction to change the icons of approved field
    def _(self, obj):
        if obj.approved == 'Approved':
            return True
        elif obj.approved == 'Pending':
            return None
        else:
            return False
    _.boolean = True
    # Function to color the text of approved field
    def status(self, obj):
        if obj.approved == "Approved":
            color = '#28a745'
        elif obj.approved == "Pending":
            color = '#fea95e'
        else:
            color = 'red'
        return format_html('<strong><p style="color:{}">{}</p></strong>'.format(color,obj.approved))
    status.allow_tags=True

    
# ================= This class specifies how to show attributes of woman products in admin panel ================= #
@admin.register(WomanProducts)
class WomanProductsAdmin(SummernoteModelAdmin):
    date_hierarchy = "created_date"
    summernote_fields = ('introduction',)
    empty_value_display = "-empty-"
    list_display = ["model_name", "price", "discount_Percentage", "advertiser", "stock", "counted_views", "status", "_"]
    fields = ["model_name", "image", "introduction", "advertiser", "price",
               "discount_Percentage", "stock", "counted_views", "style", "approved", "published_date"]
    list_filter = ("style", "approved")
    search_fields = ["model_name", "advertiser", "style"]
    list_par_page = 10
    # Furnction to change the icons of approved field
    def _(self, obj):
        if obj.approved == 'Approved':
            return True
        elif obj.approved == 'Pending':
            return None
        else:
            return False
    _.boolean = True
    # Function to color the text of approved field
    def status(self, obj):
        if obj.approved == "Approved":
            color = '#28a745'
        elif obj.approved == "Pending":
            color = '#fea95e'
        else:
            color = 'red'
        return format_html('<strong><p style="color:{}">{}</p></strong>'.format(color,obj.approved))
    status.allow_tags=True

# ================= This class specifies how to show attributes of kids products in admin panel ================= #
@admin.register(KidProducts)
class KidProductsAdmin(SummernoteModelAdmin):
    date_hierarchy = "created_date"
    summernote_fields = ('introduction',)
    empty_value_display = "-empty-"
    list_display = ["model_name", "price", "discount_Percentage", "advertiser", "stock", "counted_views", "status", "_"]
    fields = ["model_name", "image", "introduction", "advertiser", "price",
               "discount_Percentage", "stock", "counted_views", "style", "approved", "published_date"]
    list_filter = ("style", "approved")
    search_fields = ["model_name", "advertiser", "style"]
    list_par_page = 10
    # Furnction to change the icons of approved field
    def _(self, obj):
        if obj.approved == 'Approved':
            return True
        elif obj.approved == 'Pending':
            return None
        else:
            return False
    _.boolean = True
    # Function to color the text of approved field
    def status(self, obj):
        if obj.approved == "Approved":
            color = '#28a745'
        elif obj.approved == "Pending":
            color = '#fea95e'
        else:
            color = 'red'
        return format_html('<strong><p style="color:{}">{}</p></strong>'.format(color,obj.approved))
    status.allow_tags=True
    

# ================= This class specifies how to show attributes of accessories in admin panel ================= #
@admin.register(Accessories)
class AccessoriesAdmin(SummernoteModelAdmin):
    date_hierarchy = "created_date"
    summernote_fields = ('introduction',)
    empty_value_display = "-empty-"
    list_display = ["model_name", "price", "discount_Percentage", "advertiser", "stock", "counted_views", "status", "_"]
    fields = ["model_name", "image", "introduction", "advertiser", "price",
               "discount_Percentage", "stock", "counted_views", "approved", "published_date"]
    list_filter = ("approved",)
    search_fields = ["model_name", "advertiser"]
    list_par_page = 10
    # Furnction to change the icons of approved field
    def _(self, obj):
        if obj.approved == 'Approved':
            return True
        elif obj.approved == 'Pending':
            return None
        else:
            return False
    _.boolean = True
    # Function to color the text of approved field
    def status(self, obj):
        if obj.approved == "Approved":
            color = '#28a745'
        elif obj.approved == "Pending":
            color = '#fea95e'
        else:
            color = 'red'
        return format_html('<strong><p style="color:{}">{}</p></strong>'.format(color,obj.approved))
    status.allow_tags=True


# ================= This class specifies how to show attributes of comments in admin panel ================= #
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('email', 'content_type', 'object_id', 'created_date', "status", "_")
    list_filter = ('email','approved')
    search_fields = ('email','comment')
    # Furnction to change the icons of approved field
    def _(self, obj):
        if obj.approved == 'Approved':
            return True
        elif obj.approved == 'Pending':
            return None
        else:
            return False
    _.boolean = True
    # Function to color the text of approved field
    def status(self, obj):
        if obj.approved == "Approved":
            color = '#28a745'
        elif obj.approved == "Pending":
            color = '#fea95e'
        else:
            color = 'red'
        return format_html('<strong><p style="color:{}">{}</p></strong>'.format(color,obj.approved))
    status.allow_tags=True


# Registered styles model
admin.site.register(Styles)









