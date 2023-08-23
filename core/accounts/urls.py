from django.urls import path
from .views import (
    login_view, signup_view, logout_view)

app_name = "accounts"

urlpatterns = [
    # ========== Login URL ========== #
    path('login/', login_view, name = "login"),
    # ========== Signup URL ========== #
    path('signup/', signup_view, name = 'signup'),
    # ========== Logout URL ========== #
    path('logout/', logout_view, name = 'logout')
]
