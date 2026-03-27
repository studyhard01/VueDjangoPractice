from .base import *


SECRET_KEY = 'wwr2^nl0ol9+86-7o1xd50m3br^6r@rqpqjb%4(o!rb%@3w4%e'

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
