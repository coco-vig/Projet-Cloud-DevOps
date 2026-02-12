import json
from unittest.mock import MagicMock

def test_healthz(client):
    """
    Test obligatoire du Health Check 
    Doit retourner 200 et un JSON status.
    """
    response = client.get('/healthz')
    assert response.status_code == 200
    assert response.json == {"status": "alive"}

def test_get_events_mocked(client, mocker):
    """
    Test de /api/events sans connexion Azure.
    On utilise 'mocker' pour simuler la réponse d'Azure.
    """
    # 1. Données factices que le faux Azure va renvoyer
    fake_data = [{"id": 1, "title": "Event Test", "date": "2024-01-01"}]
    fake_json = json.dumps(fake_data).encode('utf-8')

    # 2. On remplace la connexion Azure par un Mock
    # On cible 'app.app.BlobServiceClient' car c'est là qu'il est importé
    mock_blob_service = mocker.patch('app.app.BlobServiceClient')
    
    # On configure la chaîne d'appels pour qu'elle renvoie nos fake_data
    # Client -> Container -> Blob -> Download -> Readall
    mock_blob_service.from_connection_string.return_value \
        .get_blob_client.return_value \
        .download_blob.return_value \
        .readall.return_value = fake_json

    # 3. On lance la requête
    response = client.get('/api/events')

    # 4. Vérifications
    assert response.status_code == 200
    assert response.json == fake_data  # On doit recevoir nos fausses données