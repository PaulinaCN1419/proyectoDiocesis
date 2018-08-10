from .base import *
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'diocesis',
        'USER': 'udiocesis',
        'PASSWORD': 'DDL2018/',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

STATIC_URL = '/static/'