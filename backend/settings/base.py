import os
from decouple import config


# Builds paths inside project settings to normalize locations
BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

BACKEND_DIR = os.path.join(BASE_DIR, "backend")
FRONTEND_DIR = os.path.join(BASE_DIR, "frontend")

UPLOAD_FOLDER = os.path.join(BACKEND_DIR, "files", "uploads")

ALLOWED_EXTENSIONS = ["jpeg", "jpg", "png", "gif"]

SQLALCHEMY_DATABASE_URI = (
    f"sqlite:///{os.path.join(BACKEND_DIR, 'dev_db.sqlite3')}"
)

WTF_CSRF_SECRET_KEY = config("CSRF_KEY")

# default mail settings for Flask Mail
MAIL_SERVER = "localhost"
MAIL_PORT = 25
MAIL_USE_TLS = False
MAIL_USE_SSL = False
MAIL_DEBUG = True
MAIL_USERNAME = None
MAIL_PASSWORD = None
DEFAULT_MAIL_SENDER = None
