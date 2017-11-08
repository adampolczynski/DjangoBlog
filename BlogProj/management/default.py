"""
Django default settings for Blog project.

Crate a local.py in this same folder to set your local settings.

"""

#should i create settings.py that overrides this default?

from os import path
from django.utils.translation import ugettext_lazy as _
import environ 

root = environ.Path(__file__) - 3
env = environ.Env(DEBUG=(bool, True), ) # uncomment later, think about environ
environ.Env.read_env(env_file=root('.env'))
BASE_DIR = root()

dirname = path.dirname

BASE_DIR = dirname(dirname(dirname(path.abspath(__file__))))
DEBUG = env('DEBUG')

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', []) 

SECRET_KEY = env('SECRET_KEY')

SITE_ID = env('SITE_ID')

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'debug_toolbar',
    'compressor',
    'registration',
    'celery',
    'BlogProj',
    'blog',
    'articles',
    'comments',
)

# --- STATIC FILES ---
STATIC_URL = '/static/'
STATIC_ROOT = env('STATIC_ROOT', default=(root - 1)('static'))

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

# --- MEDIA ---
MEDIA_URL = '/media/'
MEDIA_ROOT = env('MEDIA_ROOT', default=(root - 1)('media'))

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates/'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': (
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.request',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
            )
        }
    },
]

MIDDLEWARE_CLASSES = (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sites.middleware.CurrentSiteMiddleware',
)

ROOT_URLCONF = 'BlogProj.urls'
WSGI_APPLICATION = 'BlogProj.wsgi.application'

USE_TZ = True
TIME_ZONE = 'UTC'

# --- LANGUAGES ---
USE_I18N = True
USE_L10N = True
LANGUAGE_CODE = 'en-us'


# --- FILE UPLOAD ---
FILE_UPLOAD_MAX_MEMORY_SIZE = 2621440  # i.e. 2.5 MB
FILE_UPLOAD_PERMISSIONS = None
FILE_UPLOAD_DIRECTORY_PERMISSIONS = None

# --- DATABASE ---
# --- POSTGRESQL
DATABASES = {
    'default': env.db(
        default='postgres://soixvngf:eoXGFRZbpl8UH25E_w7CUnQPQfx_97MM@baasu.db.elephantsql.com:5432/soixvngf'),
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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


# --- DJANGO COMPRESSOR ---
# STATICFILES_FINDERS += ('compressor.finders.CompressorFinder',)

# --- CACHE ---
# {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
#         'TIMEOUT': 300,
#     }
# }

# --- DJANGO REGISTRATION REDUX ---
ACCOUNT_ACTIVATION_DAYS = 7
REGISTRATION_AUTO_LOGIN = False

DEBUG_TOOLBAR_PATCH_SETTINGS = False
INTERNAL_IPS = ['127.0.0.1']


