from django.urls import path
from .views import (
    index_view, contact_view, about_view, newsletter_view
    )

app_name = "website"

urlpatterns = [
    path('', index_view, name = "index"),
    path('contact/', contact_view, name = "contact"),
    path('about/', about_view, name = "about"),
    path('newsletter', newsletter_view, name='newsletter')
]