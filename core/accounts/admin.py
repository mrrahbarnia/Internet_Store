from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
# Register your models here.

class CustomUserAdmin(UserAdmin):
    """ This class is for exhibiting user model in admin panel """
    model = User
    list_display = ["email", "is_staff", "is_active"]
    list_filter = ["email", "is_staff", "is_active"]
    ordering = ("email",)
    search_fields = ("email",)

    fieldsets = (
        ("Authentication", {"fields": ("email", "username", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "is_superuser", "groups", "user_permissions")}),
        ("Important dates", {"fields": ("last_login",)})
    )
    
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "username", "password1", "password2", 
                           "is_active", "is_staff", "groups",
                           "user_permissions"),
            },
        ),
    )


admin.site.register(User,CustomUserAdmin)