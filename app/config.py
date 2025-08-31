import os
from dotenv import load_dotenv

# CARGAR ENV
load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_ENABLED = True
    BABEL_DEFAULT_LOCALE = 'es'
    BABEL_SUPPORTED_LOCALES = ['es', 'en']

class TestConfig(Config):
    """
    Configuración para test. Sobreescribe las configuraciones en común de "Config".
    """
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_ENABLED = False