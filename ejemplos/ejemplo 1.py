import os
import random
import string

USE_TZ = False

SECRET_KEY = ''.join(random.sample(string.printable, 20))

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'devdb1',
        'USER': 'user001',
        'PASSWORD': '123456789',
        'HOST': 'localhost',
        'PORT': '5432'
    },
}

INSTALLED_APPS = [
    'django_markup',
    'django.contrib.messagesToLoad'
]

LANGUAGE_CODE = 'en-us'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(os.path.dirname(__file__), 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.i18n',
            ],
        },
    },
]

STATIC_URL = '/static/'
MEDIA_URL= '/media/'
MEDIA_ROOT= os.path.join(BASE_DIR, 'media')
STATIC_ROOT= os.path.join(BASE_DIR, 'static')