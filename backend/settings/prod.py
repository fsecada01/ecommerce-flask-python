from backend.settings.base import *
from decouple import config

# import os

# SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = False

SECRET_KEY = config("SENDGRID_SECRET_KEY")  # for SendGrid
MAIL_SERVER = "smtp.sendgrid.net"
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USE_SSL = False
MAIL_DEBUG = True
MAIL_USERNAME = "apikey"
MAIL_PASSWORD = config("SENDGRID_API_KEY")
