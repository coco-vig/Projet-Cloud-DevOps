# Stratégie Git

Le cahier des charges impose une stratégie **Trunk-based** ou **Git Flow**, ainsi qu’une justification et des règles de maintenabilité. 

## Choix : Trunk-based development

**Pourquoi ?**
- Adapté à un binôme et à un projet itératif : branches courtes, intégration fréquente.
- C’est cohérent avec une CI/CD déclenchée à chaque push sur `main` (intégration continue). 

## Comment garantir un historique lisible et maintenable ?

Mesures proposées :
- PR obligatoire sur `main`, avec review (au moins 1 approbation).
- Merge en **squash** (1 commit par feature/fix).
- Conventions de commits (Conventional Commits) + noms de branches (`feat/`, `fix/`, `docs/`).
- Templates : PR template / issue template (optionnel).
- (Plus tard) checks CI obligatoires avant merge.

## Quels fichiers ne doivent jamais être versionnés ?

- Secrets et variables locales : `.env`, clés, certificats, tokens
- Dépendances locales / environnements : `.venv/`, `__pycache__/`, caches
- Fichiers générés : logs, coverage, artefacts build

👉 Voir `.gitignore` à la racine (il couvre ces cas).
