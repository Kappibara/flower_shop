import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Configuration:
    SQLALCHEMY_DATABASE_URI = (
        os.environ.get("DATABASE_URL")
        or "postgresql://postgres:postgres@localhost:5432/flower_shop"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CSRF_ENABLED = True
    SECRET_KEY = os.environ.get("SECRET_KEY") or os.urandom(32)
    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY") or os.urandom(32)
    GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID", None) or "1058164694225-i93chrpcm6e7qqa1vgjkcsb01t6tqr0a.apps.googleusercontent.com"
    GOOGLE_CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET", None) or "EZEOLRICNqpCjvJ0w-sXIv0k"
    GOOGLE_ACCESS_TOKEN_URL = "https://oauth2.googleapis.com/token"
    GOOGLE_AUTHORIZE_URL = "https://accounts.google.com/o/oauth2/auth"
    GOOGLE_API_BASE_URL = "https://oauth2.googleapis.com/"
