# ============ Development Settings Config ============ # 
from core.settings import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-)v&-fz8rs1yjqwdimswmc5eimbf7m9(ey5-)d(*4sjn#dfc-_w'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS CONFIG
ALLOWED_HOSTS = ['*']

# INSTALLED_APPS = []

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Django sites framework config
SITE_ID = 2

# Static and media roots
STATIC_ROOT = BASE_DIR / "static"
MEDIA_ROOT = BASE_DIR / 'media'
STATICFILES_DIRS = [
    BASE_DIR / "statics",
]