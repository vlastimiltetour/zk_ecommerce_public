from .base import *

#run from terminal
# export DJANGO_SETTINGS_MODULE=web.settings.local
# set DJANGO_SETTINGS_MODULE=web.settings.local
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
DJANGO_CSS_INLINE_ENABLE = not DEBUG

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

ALLOWED_HOSTS = ['*', 'localhost']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

#Redis settings old
# Redis settings
REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DB = 1

def show_toolbar(request):
    return True
#debug toolbar help: https://stackoverflow.com/questions/54513675/django-can-t-load-module-debug-toolbar-no-module-named-debug-toolbar
DEBUG_TOOLBAR_CONFIG = {
  "SHOW_TOOLBAR_CALLBACK" : show_toolbar,
}