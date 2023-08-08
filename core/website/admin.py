from django.contrib import admin
from website.models import Contact,NewsLetter
# Register your models here.

@admin.register(NewsLetter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ["email", "name"]
    list_filter = ["email", "name"]
    fields = ["email", "name"]
    search_fields = ["email"]

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ["email", "name"]
    list_filter = ["email", "name"]
    fields = ["email", "name", "message"]
    search_fields = ["email", "name", "message"]
