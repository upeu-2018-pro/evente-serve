"""
Django settings for evente_main project on Heroku. For more info, see:
https://github.com/heroku/heroku-django-template-upeu

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import dj_database_url
from django.urls import reverse_lazy

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "$3zmrggd$wnwxl+#z0ark&cda)dewr5w1+d2s_atg9!(!m12$h"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Application definition

INSTALLED_APPS = [
    #'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    # Disable Django's own staticfiles handling in favour of WhiteNoise, for
    # greater consistency between gunicorn and `./manage.py runserver`. See:
    # http://whitenoise.evans.io/en/stable/django.html#using-whitenoise-in-development
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',

    'social_django',
    'core',
    'accounts',
    'django.contrib.admin',
    'bootstrap3',

    'django.contrib.admindocs',
    'oauth2_provider',
    'rest_framework',
    'corsheaders',

    'catalogo',

]

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

ROOT_URLCONF = 'evente_main.urls'

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
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
            'debug': DEBUG,
        },
    },
]

WSGI_APPLICATION = 'evente_main.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },

]

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Change 'default' database configuration with $DATABASE_URL.
DATABASES['default'].update(dj_database_url.config(conn_max_age=500))

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = [
    os.path.join(PROJECT_ROOT, 'static'),
]

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# add vars

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


AUTH_USER_MODEL = 'core.User'
SOCIAL_AUTH_USER_MODEL = 'core.User'

LOGIN_REDIRECT_URL = reverse_lazy('dashboard')
LOGIN_URL = reverse_lazy('login')
LOGOUT_URL = reverse_lazy('logout')


# 設定 Django 在 console 中輸出 e-mail 內容來代替通過 SMTP 服務發送郵件
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# EMAIL
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'upeu2018pro@gmail.com'
EMAIL_HOST_PASSWORD = '123456782018'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'upeu2018pro@gmail.com'

AUTHENTICATION_BACKENDS = (
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.github.GithubOAuth2',
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'django.contrib.auth.backends.ModelBackend',
    'accounts.authentication.EmailAuthBackend',
    #'oauth2_provider.backends.OAuth2Backend',
)

AUTHENTICATION_BACKENDSx = (
    'oauth2_provider.backends.OAuth2Backend',
    # Uncomment following if you want to access the admin
    'django.contrib.auth.backends.ModelBackend',

)

SOCIAL_AUTH_URL_NAMESPACE = 'social'

SOCIAL_AUTH_FACEBOOK_KEY = '1505995752817741'
SOCIAL_AUTH_FACEBOOK_SECRET = 'a1b671143334bf268f0881655dd7f08c'
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
    'fields': 'id, name, email'
}

SOCIAL_AUTH_GITHUB_KEY = 'ddcde373489a4be6deec'
SOCIAL_AUTH_GITHUB_SECRET = '39319ff7120c0f1cb57af7130f323ebf7cb35669'
SOCIAL_AUTH_GITHUB_SCOPE = ['email']
SOCIAL_AUTH_GITHUB_PROFILE_EXTRA_PARAMS = {
    'fields': 'id, name, email'
}

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '1082996671890-fbu61vmp0gfehh7tg0tgs7feenqr95qj.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'kYj_RFjlDyDQbt6SnscPrC1j'
SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = ['email']
SOCIAL_AUTH_GOOGLE_PROFILE_EXTRA_PARAMS = {
    'fields': 'id, name, email'
}
#SOCIAL_AUTH_GOOGLE_OAUTH2_WHITELISTED_DOMAINS = ['upeu.edu.pe', ]

SOCIAL_AUTH_TWITTER_KEY = 'SYaVSEKyHbeoFrUJm6zEU1XVa'
SOCIAL_AUTH_TWITTER_SECRET = 'deltB2apIjLqThoJXDRPkPVI8ure7x9Ik5RD3g6mF6H64gOrnJ'
SOCIAL_AUTH_TWITTER_OAUTH2_SCOPE = ['email']
SOCIAL_AUTH_TWITTER_PROFILE_EXTRA_PARAMS = {
    'fields': 'id, name, email'
}


#CSRF_USE_SESSIONS = False
CORS_ORIGIN_ALLOW_ALL = True  # False
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_WHITELIST = ('127.0.0.1:9001', '127.0.0.1:9003',
                         'localhost:9003', 'localhost:8003')
# Also
OAUTH2_PROVIDER = {
    # this is the list of available scopes
    'SCOPES': {
        'read': 'Read scope',
        'write': 'Write scope',
        'openid': 'Access to your openid connect',
        'home': 'Access to your home page',
        'backend': 'Access to your backend app',
        'catalogo': 'Access to your catalogo app',
        'ubigeo': 'Access to your ubigeo app',
        'eventos': 'Access to your admision app',
        'acuerdos': 'Access to your admision app',
        'admision': 'Access to your admision app',
    }
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        #'rest_framework.authentication.SessionAuthentication',
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
    )
}


import datetime


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose0': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'verbose': {
            'format': "[%(asctime)s] [%(levelname)s] [%(name)s:%(lineno)s] [%(path)s] [%(ip)s] [%(user)s] [%(method)s] %(message)s",
            'datefmt': "%Y-%m-%d %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
        'verbose_dj': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%Y-%m-%d %H:%M:%S"
        },
    },
    'handlers': {

        'file_django': {
            'level': 'DEBUG',
            #'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
            'class': 'logging.FileHandler',
            'filename': os.path.join(
                BASE_DIR, 'temp/logs',
                'dj%s.txt' % (datetime.datetime.now().strftime("%Y-%m-%d"))
            ),
            'formatter': 'verbose_dj'
        },
        'file_log': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(
                BASE_DIR, 'temp/logs',
                'log%s.txt' % (datetime.datetime.now().strftime("%Y-%m-%d"))
            ),
            'formatter': 'verbose'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose0'
        },

    },
    'loggers': {
        'django': {
            'handlers': ['file_django'],
            'propagate': False,
            'level': 'DEBUG',
        },
        'apps': {
            'handlers': ['file_log'],
            'level': 'DEBUG',
        },
    },
    'root': {
        'handlers': ['console', 'file_log', ],
        'level': 'INFO'
    },
}


# Backup/restore database https://code.djangoproject.com/wiki/Fixtures
FIXTURE_DIRS = (
    os.path.join(BASE_DIR, 'fixtures'),
)
