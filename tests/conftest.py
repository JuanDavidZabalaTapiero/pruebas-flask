import pytest
from app import create_app
from app.config import TestConfig
from app.extensions import db

@pytest.fixture(scope="session")
def app():
    """
    Crea la aplicación Flask para pruebas con BD en memoria.
    """
    app = create_app(TestConfig)
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture()
def client(app):
    """
    Cliente de pruebas para simular requests HTTP.
    """
    return app.test_client()

@pytest.fixture()
def session(app):
    """
    Sesión de base de datos aislada para cada test.
    """
    with app.app_context():
        db.drop_all()
        db.create_all()
        yield db.session
        db.session.rollback()