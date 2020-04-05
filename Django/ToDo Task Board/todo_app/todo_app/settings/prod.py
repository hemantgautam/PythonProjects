from .base import *
import dj_database_url
DEBUG = False

DATABASES = {}
DATABASES['default'] = dj_database_url.config(conn_max_age=600)
