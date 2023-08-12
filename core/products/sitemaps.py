from django.contrib.sitemaps import Sitemap
from django.db.models.base import Model
from django.urls import reverse
from products.models import (
    MenProducts, WomanProducts, KidProducts, Accessories)


class MenProductsSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5
    def items(self):
        return MenProducts.objects.filter(approved=True)
    def lastmod(self, obj):
        return obj.published_date
    def location(self, item):
        return reverse('products:men-single', kwargs={'men_product':item.model_name})
    


class WomenProductsSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5
    def items(self):
        return WomanProducts.objects.filter(approved=True)
    def lastmod(self, obj):
        return obj.published_date 
    def location(self, item):
        return reverse('products:women-single', kwargs={'women_product':item.model_name})
    

class KidProductsSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5
    def items(self):
        return KidProducts.objects.filter(approved=True)
    def lastmod(self, obj):
        return obj.published_date 
    def location(self, item):
        return reverse('products:kids-single', kwargs={'kids_product':item.model_name})
    

class AccessoriesSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5
    def items(self):
        return Accessories.objects.filter(approved=True)
    def lastmod(self, obj):
        return obj.published_date 
    def location(self, item):
        return reverse('products:accessories-single', kwargs={'accessory':item.model_name})
    