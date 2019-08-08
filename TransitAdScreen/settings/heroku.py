"""
DJANGO_SETTINGS_MODULE=TransitAdScreen.settings.heroku
"""
import django_heroku
import dj_database_url
from .base import *  # noqa: 403
from utils.environment import env


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY', '')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['.herokuapp.com']


# Configure Django Project for Heroku
django_heroku.settings(locals())


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

db_from_env = dj_database_url.config(conn_max_age=500, ssl_require=True)
DATABASES['default'].update(db_from_env)  # noqa: F405
