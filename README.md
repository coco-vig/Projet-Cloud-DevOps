# Plateforme de diffusion de contenu statique (Cloud & DevOps)

Ce dépôt implémente une plateforme **cloud-native** de diffusion de contenu statique (événements, actualités, FAQ) stocké dans **Azure Blob Storage**, exposé via une API REST (Flask) et déployé sur **AKS** avec une chaîne **CI/CD GitHub Actions**. fileciteturn1file2

## Objectifs (extraits du cahier des charges)

- Lire des fichiers **JSON/YAML** depuis **Azure Blob Storage** fileciteturn1file2  
- Exposer les endpoints :
  - `GET /api/events` — événements fileciteturn1file2  
  - `GET /api/news` — actualités fileciteturn1file2  
  - `GET /api/faq` — FAQ fileciteturn1file2  
  - `GET /healthz` — vérification de vie fileciteturn1file2  
  - `GET /readyz` — vérification de disponibilité fileciteturn1file2  
- Mettre en place un cache mémoire avec **TTL** (ex : 60 s) fileciteturn1file2  
- Fournir une interface web minimale pour visualiser les données fileciteturn1file2  

## Architecture (étape 1)

Voir `docs/architecture.md` (schéma + explications).

## Structure du dépôt

- `app/` : application Flask (code)
- `tests/` : tests automatisés (pytest)
- `k8s/` : manifests Kubernetes (AKS)
- `.github/workflows/` : pipelines CI/CD GitHub Actions
- `docs/` : docs projet (architecture, décisions, etc.)

## Stratégie Git

Choix recommandé : **Trunk-based development** (branches courtes + PR vers `main`) — cohérent avec un pipeline déclenché à chaque push sur `main`. fileciteturn1file3

Conventions proposées :
- Branches : `feat/...`, `fix/...`, `docs/...`
- Commits : Conventional Commits (ex: `feat: add blob storage client`)
- Merges : **squash** pour un historique lisible
- Protection `main` : PR obligatoire + review + (plus tard) checks CI obligatoires

Réponses attendues dans le rapport :
1) Pourquoi cette stratégie Git ?  
2) Comment garantir un historique lisible et maintenable ?  
3) Quels fichiers ne doivent jamais être versionnés ? fileciteturn1file2  

Un guide prêt à copier est dans `docs/git-strategy.md`.

## Configuration (local)

Copier le fichier d’exemple :

```bash
cp .env.example .env
```

⚠️ Ne pas committer `.env` (voir `.gitignore`).

## Lancer en local

> À compléter à l’étape 2 (Flask local).

## Tests

> À compléter à l’étape 3 (Tests Flask).

## Docker / CI / AKS

> À compléter dans les étapes suivantes (4 → 7). fileciteturn1file3
