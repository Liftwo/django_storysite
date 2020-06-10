from .settings import *
import dj_database_url


DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.sqlite3',
        'NAME': '/Users/zooeytsai/PycharmProjects/mysite/db.sqlite3',
    },
    'agile_db': {
        'ENGINE':'django.db.backends.sqlite3',
        'NAME': '/Users/zooeytsai/PycharmProjects/mysite/agile_tai.db',
    },
}

DATABASE_ROUTERS = ['db_router.AgileRouter']

STATIC_ROOT = 'staticfiles'
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
ALLOWED_HOSTS = ['*']
DEBUG = False