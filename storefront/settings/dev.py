from .common import *

DEBUG = True

SECRET_KEY = 'django-insecure-hs6j037urx6iav+7#10%-vu4l4f5@@-1_zo)oft4g7$vf2$jmp'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'storefront3',
        'USER': 'postgres',
        'PASSWORD': '1342917',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
