import pytest
from app.app import app as flask_app, cache

@pytest.fixture
def client():
    flask_app.config['TESTING'] = True
    cache.clear()  # 🔑 Vider le cache entre chaque test
    with flask_app.test_client() as client:
        yield client