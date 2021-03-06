"""
Django default settings for Blog project.

Crate a local.py in this same folder to set your local settings.

"""

from os import path
from django.utils.translation import ugettext_lazy as _
import environ 

root = environ.Path(__file__) - 3
env = environ.Env(DEBUG=(bool, True), )
environ.Env.read_env(env_file=root('.env'))
BASE_DIR = root()

dirname = path.dirname

BASE_DIR = dirname(dirname(dirname(path.abspath(__file__))))
DEBUG = env('DEBUG')

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', []) 

SECRET_KEY = env('SECRET_KEY')

SITE_ID = env('SITE_ID')

INSTALLED_APPS = (
    'suit', # must be before admin
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'BlogProj',
    'blog',
    'articles',
    'comments',
    'products',
    'loginas',
    'debug_toolbar',
    'compressor',
    'haystack',
    'celery',
    'allauth', #all auth
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.twitter',
)
# LOGINAS
LOGINAS_UPDATE_LAST_LOGIN = False
LOGINAS_REDIRECT_URL = '/'

# EMAIL CONFIGURATION
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'androdappshelper@gmail.com'
EMAIL_HOST_PASSWORD = env('EMAIL_PASSWORD')
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# --- STATIC ---
STATIC_URL = '/static/'
STATIC_ROOT = env('STATIC_ROOT', default=(root)('static'))

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

# --- MEDIA ---
MEDIA_URL = '/media/'
MEDIA_ROOT = env('MEDIA_ROOT', default=(root)('media'))

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
# backends for allauth
AUTHENTICATION_BACKENDS = (
    'allauth.account.auth_backends.AuthenticationBackend',
    'django.contrib.auth.backends.ModelBackend',
)
# facebook
SOCIALACCOUNT_PROVIDERS = {
    'facebook': {
        'METHOD': 'oauth2',
        'SCOPE': ['email', 'public_profile', 'user_friends'],
        'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
        'INIT_PARAMS': {'cookie': True},
        'FIELDS': [
            'id',
            'email',
            'name',
            'first_name',
            'last_name',
            'verified',
            'locale',
            'timezone',
            'link',
            'gender',
            'updated_time',
        ],
        'EXCHANGE_TOKEN': True,
        'LOCALE_FUNC': 'path.to.callable',
        'VERIFIED_EMAIL': False,
        'VERSION': 'v2.5',
    }
}
SOCIALACCOUNT_EMAIL_VERIFICATION = 'none'
SOCIALACCOUNT_EMAIL_REQUIRED = False
SOCIALACCOUNT_QUERY_EMAIL = True

# login/logout redirections
LOGOUT_REDIRECT_URL = '/'
LOGIN_REDIRECT_URL = '/'

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
        default=env('DB_POSTGRES')
        ),
}
# HEROKU DATABASE CONF
import dj_database_url
db_from_env = dj_database_url.config()#conn_max_age=500
DATABASES['default'].update(db_from_env)

# broker for celery tasks
BROKER_URL = 'django://'

#haystack configuration
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.solr_backend.SolrEngine',
        'URL': env('SOLR_URL')
    },
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
STATICFILES_FINDERS += ('compressor.finders.CompressorFinder',)
