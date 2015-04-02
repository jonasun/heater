"""
Django settings for heater project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

"""
LOGGING = {
    'version': 1,
    'loggers': {
        'root': {
            'handlers': 'baeHandler',
            'propagate': True,
            'level': 'INFO',
        },
    },
    'formatters': {
        'simpleFormatter': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
    },
    'handlers': {
        'baeHandler': {
            'level': 'DEBUG',
            'class': 'bae_log.handlers.BaeLogHandler',
            'formatter':'simpleFormatter',
            'args':'("xS0uX3l5ZWnML0yDYmpdDMou", "kYhhYypbT4U5Qa40psUOH9vWbIG6kjCG", 1)',
        },
    }
}
"""
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'p&6c5z7u)s#pb+9*c((r2$==9v6+5_n*fvfphm(2rz+bip=h^h'

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = False
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['.duapp.com','.duapp.com.','127.0.0.1']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'webapi',
    'demo',
    'mcu',
    'client',
    'bae_log',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

AUTHENTICATION_BACKENDS = (
    'myauth.auth.MyCustomBackend' ,
)

ROOT_URLCONF = 'heater.urls'

WSGI_APPLICATION = 'heater.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django',                     
        'USER': 'heater',                    
        'PASSWORD': '',                 
        'HOST': '127.0.0.1',                      
        'PORT': '3306',                     
    }
}
'''

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'svrid5383l0123m',                     
        'USER': 'bae',                    
        'PASSWORD': 'kYhhYypbT4U5Qa40psUOH9vWbIG6kjCG',                 
        'HOST': 'svrid5383l0123m.mysql.duapp.com',                      
        'PORT': 10027,                     
    }
}
#conn = MySQLdb.Connection(host='10.44.87.60',port=8306, user='heater',passwd='heater', db='django')
# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'zh-CN'

TIME_ZONE = 'Asia/Shanghai'
#TIME_ZONE ='GMT-8'
USE_I18N = True

USE_L10N = True

#USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

TEMPLATE_DIRS =os.path.join(BASE_DIR,'templates/')

#STATIC_ROOT = os.path.join(BASE_DIR,'static')
