import os

from .settings import *

SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = [os.environ.get('ALLOWED_HOST')]

STATIC_ROOT = '/usr/share/nginx/html/static/'
MEDIA_ROOT = '/usr/share/nginx/html/media/'

AWS_SES_ACCESS_KEY_ID = os.environ.get('AWS_SES_ACCESS_KEY_ID')
AWS_SES_SECRET_ACCESS_KEY = os.environ.get('AWS_SES_SECRET_ACCESS_KEY')
EMAIL_BACKEND = 'django_ses.SESBackend'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,

    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'INFO'
        },

        'diary': {
            'handlers': ['file'],
            'level': 'INFO'
        }
    },

    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/django.log'),
            'formatter': 'prod',
            'when': 'D',
            'interval': 1,
            'backupCount': 7,
        },
    },

    'formatters': {
        'prod': {
            'format': '\t'.join([
                '%(asctime)s',
                '[%(levelname)s]',
                '%(pathname)s(Line:%(lineno)d)',
                '%(message)s'
            ])
        },
    }
}