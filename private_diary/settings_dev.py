from .settings_common import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-3@q7+e5@%5$8bt(09^xfto)8$aw081r-6lze=qq2b7&x46ir^e'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,

    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO'
        },

        'diary': {
            'handlers': ['console'],
            'level': 'INFO'
        }
    },

    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'dev'
        },
    },

    'formatters': {
        'dev': {
            'format': '\t'.join([
                '%(asctime)s',
                '[%(levelname)s]',
                '%(pathname)s(Line:%(lineno)d)',
                '%(message)s'
            ])
        },
    }
}