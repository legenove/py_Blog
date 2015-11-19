# coding=utf-8
"""
Django settings for mysite project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# BASE_DIR = os.path.dirname(__file__)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'b@i-657qn^_&^dkvot-jnhxwx&f#28ggbea=9m@s_gz^9*j%zh'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'contents',
    'south',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

# ROOT_URLCONF = 'mysite.urls'
ROOT_URLCONF = 'urls'

# WSGI_APPLICATION = 'mysite.wsgi.application'
WSGI_APPLICATION = 'wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mysite_blog',  # Or path to database file if using sqlite3.
        'USER': 'root',  # Not used with sqlite3.
        'PASSWORD': '',  # Not used with sqlite3.
        # 'HOST': 'localhost',  # Set to sempty string for localhost. Not used with sqlite3.
        'HOST': '',  # Set to sempty string for localhost. Not used with sqlite3.
        'PORT': '3306',  # 'CONN_MAX_AGE': 1*24*60*60,
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'zh_cn'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

LOGIN_URL = '/signin'
STATIC_URL = '/static/'
LOGIN_REDIRECT_URL = '/'
# STATIC_ROOT = '/static/'
# TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'mysite/templates')]
TEMPLATE_DIRS = [
    os.path.join(BASE_DIR, 'app/templates'),
    os.path.join(BASE_DIR, 'app/contents/templates'),
    os.path.join(BASE_DIR, 'app/outside/templates'),
    ]
DATE_FORMAT = 'Y-m-d'
DATETIME_FORMAT = 'Y-m-d H:i'
TIME_FORMAT = 'H:i'
TAG_IN_INDEX = (
    [u'技术', u'技术宅'],
    [u'生活', u'伪文艺'],
    [u'挑战', u'爱折腾'],
    [u'享乐', u'贪享乐']
)
