from pathlib import Path
import os
import django_heroku
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-r^_&qz1=81q3vuhn14=e^b(c2vj_#n03-d7--68-jiz0i_d44d'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Application definition

INSTALLED_APPS = [
    "output.apps.OutputConfig",
    "accounts.apps.AccountsConfig",

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # マークダウン
    'mdeditor',

    # cloudinary
    'cloudinary_storage',
    'cloudinary',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = 'config.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

LOGIN_URL = 'accounts:login'  # ログインしていないときのリダイレクト先
LOGIN_REDIRECT_URL = 'output:output_list'  # ログイン後のリダイレクト先
LOGOUT_REDIRECT_URL = 'accounts:login'  # ログアウト後のリダイレクト先

SITE_ID = 1

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# マークダウン設定
X_FRAME_OPTIONS = 'SAMEORIGIN'

# DEBUG = True

if DEBUG:
    ALLOWED_HOSTS = ["*"]

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

if not DEBUG:

    ALLOWED_HOSTS = ["outpro.herokuapp.com"]

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'outpro',
            'USER': 'outpro',
            'PASSWORD': '',
            'HOST': 'localhost',
            'PORT': '',
            'ATOMIC_REQUESTS': True,
        }
    }

    STATIC_ROOT = os.path.join(BASE_DIR, 'static')

    django_heroku.settings(locals())

    db_from_env = dj_database_url.config()
    DATABASES['default'].update(db_from_env)

    # ログ出力
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        # ログ出力フォーマットの設定
        'formatters': {
            'production': {
                'format': '%(asctime)s [%(levelname)s] %(process)d %(thread)d '
                          '%(pathname)s:%(lineno)d %(message)s'
            },
        },
        # ハンドラの設定
        'handlers': {
            'file': {
                'level': 'INFO',
                'class': 'logging.FileHandler',
                'filename': '{}/app.log'.format(BASE_DIR),
                'formatter': 'production',
            },
        },
        # ロガーの設定
        'loggers': {
            # 自分で追加したアプリケーション全般のログを拾うロガー
            '': {
                'handlers': ['file'],
                'level': 'INFO',
                'propagate': False,
            },
            # Django自身が出力するログ全般を拾うロガー
            'django': {
                'handlers': ['file'],
                'level': 'INFO',
                'propagate': False,
            },
        },
    }

    # # 500エラー
    # from django.views.decorators.csrf import requires_csrf_token
    # from django.http import (
    #     HttpResponseBadRequest, HttpResponseForbidden, HttpResponseNotFound,
    #     HttpResponseServerError, )
    #
    # @requires_csrf_token
    # def my_customized_server_error(request, template_name='500.html'):
    #     import sys
    #     from django.views import debug
    #     error_html = debug.technical_500_response(request, *sys.exc_info()).content
    #     return HttpResponseServerError(error_html)


    CLOUDINARY_STORAGE = {
        'CLOUD_NAME': 'dxqgqsi0r',
        'API_KEY': '847422912398694',
        'API_SECRET': 'RME13DcmjNR_WsrXTu5MjZ1m5_c',
    }

    DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

