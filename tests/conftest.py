import pytest
import sys
import os

# Ajoute le dossier racine au chemin pour que Python trouve "app"
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.app import app as flask_app

@pytest.fixture
def client():
    """Crée un client de test Flask"""
    flask_app.config['TESTING'] = True
    with flask_app.test_client() as client:
        yield client