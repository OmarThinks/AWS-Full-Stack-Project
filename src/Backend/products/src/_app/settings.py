"""
Django settings for _app project.

Generated by 'django-admin startproject' using Django 3.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure--=)7m2xq3b&gn-=esjp0@ehkb4_$q9l!n97g!e%d4@od7j3y*3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["products-app-env.eba-r2kpmfiy.us-west-2.elasticbeanstalk.com"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    "products",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = '_app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = '_app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
"""


default_db_engine = os.environ.get(
    'DEFAULT_DB_ENGINE', 'django.db.backends.sqlite3')
default_db_name = os.environ.get(
    'DEFAULT_DB_NAME', BASE_DIR / 'db.sqlite3')
default_db_user = os.environ.get(
    'DEFAULT_DB_USER', BASE_DIR / '')
default_db_password = os.environ.get(
    'DEFAULT_DB_PASSWORD', BASE_DIR / '')
default_db_host = os.environ.get(
    'DEFAULT_DB_HOST', BASE_DIR / '')
default_db_port = os.environ.get(
    'DEFAULT_DB_PORT', BASE_DIR / '')






database_dict={
        'ENGINE': default_db_engine,
        'NAME': default_db_name,
        'USER': default_db_user,
        'PASSWORD': default_db_password,
        'HOST': default_db_host,   # Or an IP Address that your DB is hosted on
        'PORT': default_db_port,
    }
"""
"""
print("This is it", flush=True)
print(database_dict, flush=True)
print("This was it", flush=True)
"""
"""

DATABASES = {
    'default': database_dict
}
"""

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



"""
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': '_app.config.StandardResultsSetPagination',
    'PAGE_SIZE': 3
}
"""