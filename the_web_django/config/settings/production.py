from .base import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres_sak',
        'USER': 'user',
        'PASSWORD': 'password',
        'HOST': '0.0.0.0',
        'PORT': '5432',
    }
}
