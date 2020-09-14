"""
Django settings for base project.

Generated by 'django-admin startproject' using Django 2.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
from . import util

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY_FILENAME = os.path.join(BASE_DIR, "squire/secret_key.txt")
SECRET_KEY = util.get_secret_key(SECRET_KEY_FILENAME)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DJANGO_ENV') != 'PRODUCTION'

if os.getenv('SENTRY_DSN'): # pragma: no cover
    import sentry_sdk
    from sentry_sdk.integrations.django import DjangoIntegration

    sentry_sdk.init(
            os.getenv('SENTRY_DSN'),
            integrations=[DjangoIntegration()],
            # Do not send email addresses to Sentry
            send_default_pii=False
    )

# Hosts on which the application will run
ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # External Libraries
    'bootstrap4',
    'recurrence',
    'rest_framework',
    # Internal Components
    'core', # Core Module should load first
    'achievements',
    'activity_calendar',
    'membership_file',
    # More External Libraries
    'django_cleanup.apps.CleanupConfig',
    'import_export',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware', #Determine Language based on user's Language preference
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'squire.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            'squire/templates'
        ],
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

WSGI_APPLICATION = 'squire.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/
# https://samulinatri.com/blog/django-translation

LANGUAGE_CODE = 'en-gb'
#LANGUAGE_CODE = 'nl'

LANGUAGES = [
    ('en', 'English'),
    ('nl', 'Dutch'),
]

TIME_ZONE = 'Europe/Amsterdam'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]

# Log Settings
APPLICATION_LOG_LEVEL = 'INFO'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'console': {
            # exact format is not important, this is the minimum information
            'format': '%(asctime)s (%(name)-12s) [%(levelname)s] %(message)s',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'console',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
        },
        'squire': {
            'handlers': ['console'],
            'level': APPLICATION_LOG_LEVEL,
        },
        'core': {
            'handlers': ['console'],
            'level': APPLICATION_LOG_LEVEL,
        },
        'activity_calendar': {
            'handlers': ['console'],
            'level': APPLICATION_LOG_LEVEL,
        },
        'membership_file': {
            'handlers': ['console'],
            'level': APPLICATION_LOG_LEVEL,
        },
        'achievements': {
            'handlers': ['console'],
            'level': APPLICATION_LOG_LEVEL,
        },
    },
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'htdocs', 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'htdocs', 'media')

# Additional places to look for static files
STATICFILES_DIRS = []


# The directory in which the coverage reports should be stored
COVERAGE_REPORT_DIR = os.path.join(BASE_DIR, 'coverage')

# Automatically create a /coverage folder if it does not exist
util.create_coverage_directory(COVERAGE_REPORT_DIR)

####################################################################
# Login Settings

# The URL or named URL pattern where requests are redirected for login
# when using the login_required() decorator.
# Also used to specify the location of the login page
LOGIN_URL = '/login' 

# The URL or named URL pattern where requests are redirected after
# login when the LoginView doesn’t get a next GET parameter.
LOGIN_REDIRECT_URL = '/' # Redirect to homepage

# Not a native Django-setting, but used to specify the location of the logout page
LOGOUT_URL = '/logout'

# The URL or named URL pattern where requests are redirected after
# logout if LogoutView doesn’t have a next_page attribute.
LOGOUT_REDIRECT_URL = '/logout/success'


# Not a native Django setting, but used to specify the url to redirect to
# when the membership_required-decorator does not receive a fail_url parameter
MEMBERSHIP_FAIL_URL = '/no_member'

# Where the membership file will be exported to. Can be set to None to disable this functionality
MEMBERSHIP_FILE_EXPORT_PATH = os.getenv('MEMBERSHIP_FILE_EXPORT_PATH') or os.path.join(BASE_DIR, "output")

####################################################################
# Other Settings
# Non-native Django setting
APPLICATION_NAME = 'Squire'
COMMITTEE_ABBREVIATION = 'UUPS'
COMMITTEE_FULL_NAME = 'UUPS Ultraviolet Programmer Squad'

if not os.getenv('SENTRY_DSN'):
    # People who get error code notifications if Debug = False
    ADMINS = [
        (APPLICATION_NAME + ' Developer',       'developer@example.com'),
        (APPLICATION_NAME + ' Administrator',   'administrator@example.com'),
    ]

# The email address that error messages come from, such as those sent to ADMINS and MANAGERS.
SERVER_EMAIL = f'{APPLICATION_NAME} Error <{APPLICATION_NAME.lower()}-error@kotkt.nl>'

# Default email address to use for various automated correspondence from the site manager(s).
DEFAULT_FROM_EMAIL = f'{APPLICATION_NAME} <{APPLICATION_NAME.lower()}-noreply@kotkt.nl>'

# Debug settings
# Also run the following command to imitate an SMTP server locally: python -m smtpd -n -c DebuggingServer localhost:1025
# Emails that are sent will be shown in that terminal
if DEBUG:
    EMAIL_HOST = 'localhost'
    EMAIL_PORT = 1025
    EMAIL_HOST_USER = ''
    EMAIL_HOST_PASSWORD = ''
    EMAIL_USE_TLS = False

