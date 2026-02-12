# 1. Image de base légère (SLIM) pour réduire la taille 
FROM python:3.9-slim

# 2. Variables d'environnement pour optimiser Python
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# 3. Définir le répertoire de travail
WORKDIR /app

# 4. Copier les dépendances et installer
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copier le code de l'application
COPY app/ .
# Copier le dossier templates explicitement au bon endroit
COPY app/templates ./templates
COPY app/static ./static

# 6. SÉCURITÉ : Créer un utilisateur non-root 
RUN useradd -m appuser
USER appuser

# 7. Documenter le port (5001 car c'est celui qu'on utilise)
EXPOSE 5001

# 8. Commande de démarrage
CMD ["python", "app.py"]