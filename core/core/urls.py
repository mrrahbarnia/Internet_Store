from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from website.sitemaps import WebsiteViewSitemap
from products.sitemaps import (
    MenProductsSitemap, WomenProductsSitemap,
    KidProductsSitemap, AccessoriesSitemap)
from django.contrib.auth import views as auth_view
from accounts.forms import (
    PasswordResetForm, SetPasswordForm, PasswordChangeForm)

# Sitemaps urls
sitemaps = {
    "static": WebsiteViewSitemap,
    "menproducts_sitemaps":MenProductsSitemap,
    "womenproducts-sitemaps":WomenProductsSitemap,
    "kidsproducts-sitemaps":KidProductsSitemap,
    "accessoriessitemaps":AccessoriesSitemap
}

urlpatterns = [
    #======== Admin panel url ========#
    path('admin/', admin.site.urls),
    #======== Website app urls ========#
    path('',include("website.urls")),
    #======== Products app urls ========#
    path('products/',include('products.urls')),
    #======== Accounts app urls ========#
    path('accounts/',include("accounts.urls")),
    #======== Captcha url config ========#
    path('captcha/', include('captcha.urls')),
    #======== Sitemap url config ========#
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
    #======== Robots.txt url config ========#
    path('robots.txt', include('robots.urls')),
    #======== Debug-toolbar url config ========#
    path("__debug__/", include('debug_toolbar.urls')),
    #======== Summernote url config ========#
    path('summernote/', include('django_summernote.urls')),
    #======== Urls for reseting password if user forgot the password ========#
    path('reset_password/', auth_view.PasswordResetView.as_view(template_name = 'accounts/password_reset_form.html',form_class=PasswordResetForm), name='reset_password'),
    path('password_reset_done/', auth_view.PasswordResetDoneView.as_view(template_name = 'accounts/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(template_name = 'accounts/password_reset_confirm.html',form_class=SetPasswordForm), name='password_reset_confirm'),
    path('password_reset_complete/', auth_view.PasswordResetCompleteView.as_view(template_name = 'accounts/password_reset_complete.html'), name='password_reset_complete'),
    # =============== Urls for changing password while user is authenticated =============== #
    path('password_change/', auth_view.PasswordChangeView.as_view(template_name = 'accounts/password_change_form.html',form_class=PasswordChangeForm), name='password_change'),
    path('password_change_done', auth_view.PasswordChangeDoneView.as_view(template_name = 'accounts/password_change_done.html'), name='password_change_done'),
]

# This part only uses for development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)