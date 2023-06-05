"""
Django settings for Event_Project project.

Generated by 'django-admin startproject' using Django 4.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import os
from pathlib import Path

from django.conf import settings
import cloudinary
import cloudinary.api
import cloudinary.uploader


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

from decouple import config
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG =config('DEBUG',cast=bool) 
host=os.environ.get('RENDER_EXTERNAL_URL')

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.postgres',
    'rest_framework',
    'corsheaders',
    'dj_rest_auth',
    'allauth',
    'allauth.account',
    'rest_framework_simplejwt',
    'django_filters',
    'rest_framework_swagger',
    'drf_yasg',
    'cloudinary',
    'Users.apps.UsersConfig',
    'Events.apps.EventsConfig',
    'ADMIN.apps.AdminConfig',
    'Transactions.apps.TransactionsConfig',
   

]
SITE_ID=1
AUTH_USER_MODEL='Users.User'
ACCOUNT_AUTHENTICATION_METHOD='email'
ACCOUNT_EMAIL_VERIFICATION='mandatory'
ACCOUNT_EMAIL_REQUIRED= True
CORS_ALLOW_ALL_ORIGINS=True
ACCOUNT_USERNAME_REQUIRED=False
ACCOUNT_USER_MODEL_USERNAME_FIELD=None
CELERY_BROKER_URL=config('CELERY_BROKER_URL') 
CELERY_RESULT_BACKEND=config('CELERY_RESULT_BACKEND')
DJANGO_SUPERUSER_EMAIL=config('SUPERUSER_EMAIL')
DJANGO_SUPERUSER_PASSWORD=config('SUPERUSER_PASSWORD')

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
     'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Event_Project.urls'
REST_AUTH_TOKEN_MODEL=None
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'Event_Project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases


DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.postgresql',
         'USER': config('POSTGRES_USER'),
         'NAME':config('POSTGRES_NAME'), 
         'PASSWORD':config('POSTGRES_PASSWORD'),
         'HOST': 'db',
         'PORT': 5432,

    }
 }

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME':BASE_DIR /"db.sqlite3",
#
#    }
#}


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


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Lagos'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
MEDIA_URL='media/'
STATIC_ROOT='static'
MEDIA_ROOT='media'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

PAYSTACK_SECRET_KEY=config('PAYSTACK_SECRET_KEY')
EMAIL_BACKEND= 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST='smtp.gmail.com'
EMAIL_HOST_PASSWORD=config('EMAIL_HOST_PASSWORD')
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_USE_SSL=False
EMAIL_HOST_USER=config('EMAIL_HOST_USER')
REST_AUTH_PW_RESET_USE_SITES_DOMAIN= True

AUTHENTICATION_BACKENDS= (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend")

CSRF_COOKIE_SECURE=True

REST_FRAMEWORK= {
     "DEFAULT_AUTHENTICATION_CLASSES":[
         'rest_framework.authentication.SessionAuthentication',
        "dj_rest_auth.jwt_auth.JWTCookieAuthentication"
    ],

    "DEFAULT_PERMISSION_CLASSES":[ 
        'rest_framework.permissions.IsAuthenticated'
    ],

    

    "DEFAULT_PAGINATION_CLASS": 'rest_framework.pagination.LimitOffsetPagination',
    "PAGE_SIZE": 10,

    'DEFAULT_SCHEMA_CLASS':'rest_framework.schemas.AutoSchema',
    
}
REST_AUTH={
    "USER_DETAILS_SERIALIZER":'Users.serializers.UserDetailSerializer', 
    "REGISTER_SERIALIZER":'Users.serializers.RegisterSerializer', 
    "TOKEN_MODEL" :None, 
    "JWT_AUTH_COOKIE" :'ticket-plug-access-cookie', 
    "JWT_AUTH_REFRESH_COOKIE" : 'ticket-plug-refresh-cookie', 
    "USE_JWT": True, 
    'PASSWORD_RESET_USE_SITES_DOMAIN': True,
    'OLD_PASSWORD_FIELD_ENABLED': True, 
    "LOGIN_SERIALIZER" :'Users.serializers.LoginSerializer'
}

from datetime import timedelta
SIMPLE_JWT={
    'ACCESS_TOKEN_LIFETIME':timedelta(minutes=6),
    'REFRESH_TOKEN_LIFETIME':timedelta(days=14), 
    'SIGNING_KEY':config('SIGNING_KEY')
}

DEFAULT_FROM_EMAIL='TicketPlug@gmail.com'
ACCOUNT_ADAPTER='Event_Project.adapter.CustomAdapter'
FRONTEND_URL=config('FRONTEND_URL')

SWAGGER_SETTINGS={
'LOGIN_URL':'rest_login',
'LOGOUT_URL':'rest_logout',
}
SESSION_COOKIE_SECURE=True
CSRF_COOKIE_SECURE=True


cloudinary.config( 
  cloud_name = config('CLOUD_NAME'), 
  api_key = config('CLOUD_API_KEY') , 
  api_secret =  config('CLOUD_API_SECRET')
)
