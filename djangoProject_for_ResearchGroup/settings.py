import os.path
import pymysql
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-!y)q^eh)dg9h5wvqu6z2*^5(4%r(k(#ir(3!q6gx1!-l4)rd)r'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG =  True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app01',
    'tinymce',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'app01.middleware.auth.AuthMiddleware'
]

ROOT_URLCONF = 'djangoProject_for_ResearchGroup.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'djangoProject_for_ResearchGroup.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'djangoproject_for_researchgroup',  # 数据库名字
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',  # 那台机器安装了MySQL
        'PORT': 3306,
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

#LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_ROOT_for_teacherphoto = os.path.join(BASE_DIR, 'app01/static/media_for_teacherphoto').replace('\\', '/')  # 设置文件存放路径
MEDIA_ROOT_for_studentphoto = os.path.join(BASE_DIR, 'app01/static/media_for_studentphoto').replace('\\', '/')
MEDIA_ROOT_for_code = os.path.join(BASE_DIR, 'app01/static/media_for_code').replace('\\', '/')
MEDIA_ROOT_for_publicity = os.path.join(BASE_DIR, 'app01/static/media_for_publicity').replace('\\', '/')
MEDIA_ROOT_for_labphoto = os.path.join(BASE_DIR, 'app01/static/media_for_labphoto').replace('\\', '/')
MEDIA_ROOT_for_instrument = os.path.join(BASE_DIR, 'app01/static/media_for_instrument').replace('\\', '/')
MEDIA_ROOT_for_news = os.path.join(BASE_DIR, 'app01/static/media_for_news').replace('\\', '/')


#配置celery
BROKER_URL = 'redis://localhost:6379/0'

# 配置：配置用户村春结果
CELERY_RESULT_BACKEND = 'redis://localhost:6379/1'

#链接超时的时间设置
BROKE_TRANSPORT_OPTIONS = {'visiblility_timeout':3600}

#消息格式
CELERY_ACCEPT_CONNECT = ['application/json']

CELERY_TASK_SERIALIZER = 'json'

CELERY_RESULT_SERIALIZER = 'json'

#celery的时区
CELERY_TOMEZONE = TIME_ZONE


