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
