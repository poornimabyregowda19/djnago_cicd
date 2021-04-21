import os

DEBUG = False
from dotenv import load_dotenv
load_dotenv(".env.production")

SECRET_KEY = os.getenv('SECRET_KEY')
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS')
