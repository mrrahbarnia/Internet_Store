from django.contrib.syndication.views import Feed
from .models import (
    WomanProducts, MenProducts, KidProducts, Accessories)

# ============ Men products rss feed ============ #
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


# ============ women products rss feed ============ #
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


# ============ kids products rss feed ============ #
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


# ============ accessories rss feed ============ #
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
