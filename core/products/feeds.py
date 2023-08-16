from django.contrib.syndication.views import Feed
from .models import (
    WomanProducts, MenProducts, KidProducts, Accessories)


class MenProductsFeed(Feed):
    title = "Men products"
    link = "rss/feed/"
    description = "Best men products ever."

    def items(self):
        return WomanProducts.objects.filter(approved = "Approved")

    def item_title(self, item):
        return item.model_name

    def item_description(self, item):
        return item.introduction[:100]
    
class WomenProductsFeed(Feed):
    title = "Women products"
    link = "rss/feed/"
    description = "Best women products ever."

    def items(self):
        return MenProducts.objects.filter(approved = "Approved")

    def item_title(self, item):
        return item.model_name

    def item_description(self, item):
        return item.introduction[:100]
    
class KidsProductsFeed(Feed):
    title = "Kids products"
    link = "rss/feed/"
    description = "Best kids products ever."

    def items(self):
        return KidProducts.objects.filter(approved = "Approved")

    def item_title(self, item):
        return item.model_name

    def item_description(self, item):
        return item.introduction[:100]
    

class AccessoriesFeed(Feed):
    title = "Accesories"
    link = "rss/feed/"
    description = "Best accessories ever."

    def items(self):
        return Accessories.objects.filter(approved = "Approved")

    def item_title(self, item):
        return item.model_name

    def item_description(self, item):
        return item.introduction[:100]
