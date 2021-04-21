import os
DEBUG = True

from dotenv import load_dotenv
load_dotenv(".env.development")

SECRET_KEY = os.getenv('SECRET_KEY')
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS')

POSTGRESQL = {
    "engine": "django.contrib.gis.db.backends.postgis",
    "db_name": os.getenv('DBNAME'),
    "user": os.getenv('DBUSER'),
    "password": os.getenv('DBPASSWORD'),
    "host": os.getenv('DBHOST'),
    "port": os.getenv('DBPORT'),
}