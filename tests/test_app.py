import json
import pytest

def test_healthz(client):
    response = client.get('/healthz')
    assert response.status_code == 200
    assert response.json == {"status": "test"}

def test_readyz(client):
    response = client.get('/readyz')
    assert response.status_code == 200
    assert response.json == {"status": "ready"}

def test_get_events_mocked(client, mocker):
    # Un seul système de mock, pas les deux mélangés
    mocker.patch('app.app.AZURE_CONNECTION_STRING', 'FakeConnectionString')
    fake_data = [{"id": 1, "title": "Event Test"}]
    fake_json = json.dumps(fake_data).encode('utf-8')

    mock_blob = mocker.patch('app.app.BlobServiceClient')
    mock_blob.from_connection_string.return_value \
        .get_blob_client.return_value \
        .download_blob.return_value \
        .readall.return_value = fake_json

    response = client.get('/api/events')
    assert response.status_code == 200
    assert response.json == fake_data

def test_get_news_mocked(client, mocker):
    mocker.patch('app.app.AZURE_CONNECTION_STRING', 'FakeConnectionString')
    fake_data = [{"id": 1, "title": "News Test"}]
    fake_json = json.dumps(fake_data).encode('utf-8')

    mock_blob = mocker.patch('app.app.BlobServiceClient')
    mock_blob.from_connection_string.return_value \
        .get_blob_client.return_value \
        .download_blob.return_value \
        .readall.return_value = fake_json

    response = client.get('/api/news')
    assert response.status_code == 200
    assert response.json == fake_data

def test_get_faq_mocked(client, mocker):
    mocker.patch('app.app.AZURE_CONNECTION_STRING', 'FakeConnectionString')
    fake_data = [{"question": "Q1?", "answer": "A1"}]
    fake_json = json.dumps(fake_data).encode('utf-8')

    mock_blob = mocker.patch('app.app.BlobServiceClient')
    mock_blob.from_connection_string.return_value \
        .get_blob_client.return_value \
        .download_blob.return_value \
        .readall.return_value = fake_json

    response = client.get('/api/faq')
    assert response.status_code == 200
    assert response.json == fake_data