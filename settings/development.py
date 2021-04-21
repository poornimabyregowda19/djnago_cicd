import os
DEBUG = True

from dotenv import load_dotenv
load_dotenv(".env.development")

SECRET_KEY = os.getenv('SECRET_KEY')
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS')
