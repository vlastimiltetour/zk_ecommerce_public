import os
from .base import *


DEBUG = False


ADMINS = [
    ('Zuzi Koko', 'zuzi@zuzikoko.com'),
]

ALLOWED_HOSTS = ['zuzikoko.com', 'www.zuzikoko.com','68.183.78.31','localhost', '127.0.0.1', '[::1]', ]
#https://kinsta.com/knowledgebase/edit-mac-hosts-file/


DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': os.environ.get('POSTGRES_DB'),
       'USER': os.environ.get('POSTGRES_USER'),
       'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
       'HOST': 'db',
       'PORT': 5432,
   }
}


#Redis settings old
REDIS_HOST = 'redis'
REDIS_PORT = 6379
REDIS_DB = 1
#CELERY_BROKER_URL = "redis://redis:6379/1"
#CELERY_RESULT_BACKEND = "redis://redis:6379/1"

#broker settings from: https://kyria.github.io/LazyBlacksmith/getting_started/docker/
CELERY_BROKER_URL = 'amqp://myuser:mypassword@rabbitmq:5672'
CELERY_RESULT_BACKEND = 'rpc://'

# Security
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True