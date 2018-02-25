from .base import *

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'c2',
        'USER': 'proxyuser',
        'PASSWORD': 'aQanADtDB&vkau6A+Wj3',
        'HOST': '35.196.84.189',
        'PORT': '5432',
    }
}

ALLOWED_HOSTS = [
    'localhost',
]
