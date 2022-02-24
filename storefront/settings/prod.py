import os
import environ
from .common import *

env = environ.Env()
environ.Env.read_env(BASE_DIR / '.env')

DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']

DATABASES = {
    'default': env.db()
}
