import os
import environ
from .common import *


env = environ.Env()
environ.Env.read_env(BASE_DIR / '.env')

DEBUG = False

SECRET_KEY = env('SECRET_KEY')

ALLOWED_HOSTS = env.list('ALLOWED_HOST')

DATABASES = {
    'default': env.db()
}
