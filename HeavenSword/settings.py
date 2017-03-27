# coding=utf-8
"""
Django settings for HeavenSword project.

Generated by 'django-admin startproject' using Django 1.9.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'xqlpniip)kgj&dod5e=k95!q6su!m$tsy__&li3-vx)tflp#yr'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    # 'django.contrib.admin',
    'xadmin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.sites',
    # 'django_comments',
    'crispy_forms',
    'web',
    # 'tools',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'HeavenSword.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
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

WSGI_APPLICATION = 'HeavenSword.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'HeavenSword',
        'USER': 'root',  # 你的数据库用户名
        'PASSWORD': '',  # 你的数据库密码
        'HOST': 'localhost',  # 你的数据库主机，留空默认为localhost
        'PORT': '3306',  # 你的数据库端口
    }
}

'''
superuser:admin
password:Admin6666!
'''

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

# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/
# 后台英文
# LANGUAGE_CODE = 'en-us'
# TIME_ZONE = 'UTC'
# 后台简体中文zh-Hant为繁体中文
LANGUAGE_CODE = 'zh-Hans'
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
STATIC_PATH = os.path.join(BASE_DIR, 'static')  # 静态文件目录设置
STATICFILES_DIRS = [STATIC_PATH, ]

WEB_PATH = os.path.join(BASE_DIR, 'web', )
TOOLS_PATH = os.path.join(BASE_DIR, 'tools', )

# 关闭浏览器session失效设置
SESSION_EXPIRE_AT_BROWSER_CLOSE = True  # 浏览器关闭session失效
SESSION_EXPIRY = 0  # session０秒失效
# 设置cookies为httponly
SESSION_COOKIE_HTTPONLY = True

# 邮箱服务
EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST='smtp.qq.com'
EMAIL_HOST_USER='1249742284@qq.com'
EMAIL_USE_SSL = True
EMAIL_HOST_PASSWORD='lfllryjbiejcgffe'
EMAIL_PORT=465
EMAIL_USE_TLS=False
DEFAULT_FROM_EMAIL='fly_luna@outlook.com'
