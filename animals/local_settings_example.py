import datetime

JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=5)
}

CORS_ORIGIN_ALLOW_ALL = True
INTERNAL_IPS = ['127.0.0.1', ]
DEBUG = True
ALLOWED_HOSTS = ['*']
