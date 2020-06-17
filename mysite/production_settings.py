from .settings import *


DATABASES = {
    'agile_db': {
        'ENGINE':'django.db.backends.postgresql',
        'NAME':'agile',
        'USER':'zooeytsai',
        'PASSWORD':'tyla910ai',
        'HOST':'localhost',
        'PORT':'5432',
    },
}
STATIC_ROOT = 'staticfiles'
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
ALLOWED_HOSTS = ['*']
DEBUG = False