import os
import json
from flask import Flask, jsonify
from azure.storage.blob import BlobServiceClient
from cachetools import TTLCache

app = Flask(__name__)

# CONFIGURATION
# IMPORTANT: On récupère la clé via variable d'environnement, jamais en dur [cite: 106]
AZURE_CONNECTION_STRING = os.getenv("AZURE_CONNECTION_STRING")
CONTAINER_NAME = "content"
CACHE_TTL = 60  # secondes 

# Initialisation du cache (max 100 objets, expire après 60s)
cache = TTLCache(maxsize=100, ttl=CACHE_TTL)

def get_blob_data(filename):
    """
    Récupère un fichier JSON depuis Azure Blob Storage avec mise en cache.
    """
    # 1. Vérifier si la donnée est dans le cache
    if filename in cache:
        print(f"DEBUG: Récupération depuis le cache pour {filename}")
        return cache[filename]

    # 2. Sinon, récupérer depuis Azure
    try:
        if not AZURE_CONNECTION_STRING:
            return {"error": "Azure Connection String not configured"}, 500

        blob_service_client = BlobServiceClient.from_connection_string(AZURE_CONNECTION_STRING)
        blob_client = blob_service_client.get_blob_client(container=CONTAINER_NAME, blob=filename)
        
        # Téléchargement et parsing du JSON
        download_stream = blob_client.download_blob()
        data = json.loads(download_stream.readall())
        
        # 3. Stocker dans le cache
        cache[filename] = data
        print(f"DEBUG: Récupération depuis Azure pour {filename}")
        return data
        
    except Exception as e:
        print(f"ERROR: {str(e)}")
        return {"error": f"Impossible de lire {filename}", "details": str(e)}, 500

# ENDPOINTS API 

@app.route('/api/events', methods=['GET'])
def get_events():
    """Retourne les événements [cite: 33]"""
    data = get_blob_data("events.json")
    return jsonify(data)

@app.route('/api/news', methods=['GET'])
def get_news():
    """Retourne les actualités [cite: 35]"""
    data = get_blob_data("news.json") # Assure-toi d'avoir news.json sur Azure
    return jsonify(data)

@app.route('/api/faq', methods=['GET'])
def get_faq():
    """Retourne la FAQ [cite: 37]"""
    data = get_blob_data("faq.json") # Assure-toi d'avoir faq.json sur Azure
    return jsonify(data)

# HEALTH CHECKS [cite: 127]

@app.route('/healthz', methods=['GET'])
def healthz():
    """Vérification de vie [cite: 38]"""
    return jsonify({"status": "alive"}), 200

@app.route('/readyz', methods=['GET'])
def readyz():
    """Vérification de disponibilité [cite: 40]"""
    # Ici on pourrait tester la connexion à Azure si on voulait être strict
    return jsonify({"status": "ready"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)