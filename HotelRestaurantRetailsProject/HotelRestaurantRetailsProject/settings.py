"""
Django settings for HotelRestaurantRetailsProject project.

Generated by 'django-admin startproject' using Django 4.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os
from datetime import timedelta
import datetime
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-_hszmocki1+jo&s38az5reg8@nl4=*)fay2nv1y=g@is*3p@99'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'HotelApis',
    'AccountApis',
    'RestaurantApis',
    'CartApis',
    'RetailsApis',
    'TemplatesApp',
    'PostDataApp',
    'django_filters',
    'rest_framework',
    'drf_yasg',  #swagger documentation
    'djoser',
    'corsheaders', #to connect django and react
    'rest_framework.authtoken',
    #'import_export',


]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'HotelRestaurantRetailsProject.urls'

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

WSGI_APPLICATION = 'HotelRestaurantRetailsProject.wsgi.application'
AUTH_USER_MODEL="HotelApis.MyUser"

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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



REST_FRAMEWORK = {
    # 'NON_FIELD_ERRORS_KEY':'errors',
    # 'DEFAULT_AUTHENTICATION_CLASSES': (

    #     'rest_framework_simplejwt.authentication.JWTAuthentication',
    # ),

    # # ukitoa hiyo ya chini utaondoa m2 kuona apis mpka alogin
    # #"DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated"),
    #"DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    #"PAGE_SIZE": 1,
}





DATE_INPUT_FORMATS = [
    '%d-%m-%Y %H:%M:%S',
]

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en'#'en-us'

TIME_ZONE = 'Africa/Dar_es_Salaam'
#TIME_ZONE = 'UTC'

USE_I18N = True

USE_LION = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'

# CORS_ORIGIN_WHITELIST =[
#     "http://localhost:3000",
# ]

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True



#STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "static"
# CRISPY_TEMPLATE_PACK = "bootstrap4"



MEDIA_URL = "/media/"
MEDIA_ROOT= BASE_DIR / "media"
# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
#sending email in django
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'dimosoeljunior8@gmail.com'
EMAIL_HOST_PASSWORD = 'rrqvntxaattupawv'
EMAIL_USE_TLS = True

