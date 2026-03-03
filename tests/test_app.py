import json
import pytest

# -------------------------------------------------------------------
# 1. TESTS DE SANTÉ (Health checks) obligatoires
# -------------------------------------------------------------------

def test_healthz(client):
    """
    Test obligatoire du Health Check (/healthz)
    Doit retourner 200 et un JSON status.
    """
    response = client.get('/healthz')
    assert response.status_code == 200
    assert "status" in response.json

def test_readyz(client):
    """
    Test obligatoire de disponibilité (/readyz)
    Doit retourner 200 et un JSON status.
    """
    response = client.get('/readyz')
    assert response.status_code == 200
    assert "status" in response.json

# -------------------------------------------------------------------
# 2. TESTS FONCTIONNELS (Mocks d'Azure) obligatoires
# -------------------------------------------------------------------

def test_get_events_mocked(client, mocker, monkeypatch):
    """ Test de /api/events sans connexion Azure """
    monkeypatch.setattr('app.app.AZURE_CONNECTION_STRING', 'DefaultEndpointsProtocol=https;AccountName=test;AccountKey=test;EndpointSuffix=core.windows.net')
    
    fake_data = [{"id": 1, "title": "Event Test", "date": "2024-01-01"}]
    fake_json = json.dumps(fake_data).encode('utf-8')

    mock_blob_service = mocker.patch('app.app.BlobServiceClient')
    mock_blob_service.from_connection_string.return_value \
        .get_blob_client.return_value \
        .download_blob.return_value \
        .readall.return_value = fake_json

    response = client.get('/api/events')
    assert response.status_code == 200
    assert response.json == fake_data

def test_get_news_mocked(client, mocker, monkeypatch):
    """ Test de /api/news sans connexion Azure """
    monkeypatch.setattr('app.app.AZURE_CONNECTION_STRING', 'DefaultEndpointsProtocol=https;AccountName=test;AccountKey=test;EndpointSuffix=core.windows.net')
    
    fake_data = [{"id": 1, "title": "News Test"}]
    fake_json = json.dumps(fake_data).encode('utf-8')

    mock_blob_service = mocker.patch('app.app.BlobServiceClient')
    mock_blob_service.from_connection_string.return_value \
        .get_blob_client.return_value \
        .download_blob.return_value \
        .readall.return_value = fake_json

    response = client.get('/api/news')
    assert response.status_code == 200
    assert response.json == fake_data

def test_get_faq_mocked(client, mocker, monkeypatch):
    """ Test de /api/faq sans connexion Azure """
    monkeypatch.setattr('app.app.AZURE_CONNECTION_STRING', 'DefaultEndpointsProtocol=https;AccountName=test;AccountKey=test;EndpointSuffix=core.windows.net')
    
    fake_data = [{"question": "Q1?", "answer": "A1"}]
    fake_json = json.dumps(fake_data).encode('utf-8')

    mock_blob_service = mocker.patch('app.app.BlobServiceClient')
    mock_blob_service.from_connection_string.return_value \
        .get_blob_client.return_value \
        .download_blob.return_value \
        .readall.return_value = fake_json

    response = client.get('/api/faq')
    assert response.status_code == 200
    assert response.json == fake_data