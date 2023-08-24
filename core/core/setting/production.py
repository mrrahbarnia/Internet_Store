# ============ Production Settings Config ============ # 
from core.settings import *
from decouple import config

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', cast=bool, default=False)

# ALLOWED_HOSTS CONFIG
ALLOWED_HOSTS = ['mrrahbarnia.com','www.mrrahbarnia.com']

# INSTALLED_APPS = []

# Google SMTP server configue
EMAIL_BACKEND = config('EMAIL_BACKEND')
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_USE_TLS = config('EMAIL_USE_TLS', cast=bool, default=True)
EMAIL_PORT = config('EMAIL_PORT', cast=int)
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')

# Django sites framework config
SITE_ID = 4

# Static and media roots
STATIC_ROOT = BASE_DIR / "static"
MEDIA_ROOT = BASE_DIR / 'media'
STATICFILES_DIRS = [
    BASE_DIR / "statics",
]

# Database config
DATABASES = {
    'default': {
        'ENGINE': config('ENGINE'),
        'NAME': config('NAME'),
        'USER': config('USER'),
        'PASSWORD': config('PASSWORD'),
        'HOST': config('HOST'),
        'PORT': config('PORT',cast=int),
    }
}


## X-XSS-Protection
SECURE_BROWSER_XSS_FILTER = True
## X-Frame-Options
X_FRAME_OPTIONS = 'SAMEORIGIN'
#X-Content-Type-Options
SECURE_CONTENT_TYPE_NOSNIFF = True
## Strict-Transport-Security
SECURE_HSTS_SECONDS = 15768000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

## that requests over HTTP are redirected to HTTPS. aslo can config in webserver
SECURE_SSL_REDIRECT = True 

# for more security
CSRF_COOKIE_SECURE = True
CSRF_USE_SESSIONS = True
CSRF_COOKIE_HTTPONLY = True
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_SAMESITE = 'Strict'

# CSP config
CSP_DEFAULT_SRC = ["'self'"]
CSP_SCRIPT_SRC = ["http://127.0.0.1:8000","https://fonts.googleapis.com","https://fonts.gstatic.com"]
CSP_STYLE_SRC = ["http://127.0.0.1:8000","https://fonts.googleapis.com","https://fonts.gstatic.com"]
CSP_IMG_SRC = ["'self'",
    "https://www.googletagmanager.com",
    "https://www.google-analytics.com"]
CSP_FRAME_SRC = ["https://www.google.com/"]
CSP_INCLUDE_NONCE_IN = ["script-src"]