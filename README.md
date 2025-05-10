# Vinted Fetcher

Ce projet permet de récupérer des articles depuis Vinted à l'aide de l'API publique.

Deux modes d'utilisation sont disponibles :

- `fetch_to_csv.py` : récupère les articles et les enregistre dans un fichier CSV.
- `fetch_to_webhook.py` : récupère les articles et les envoie à un webhook Discord.

## Configuration

Les paramètres de recherche (ex. : mots-clés, prix, taille, etc.) doivent être modifiés directement dans les fichiers Python (`fetch_to_csv.py` ou `fetch_to_webhook.py`).

## Dépendances

Utilise Python 3 et les modules standard (`requests`, `csv`, etc.).

## Utilisation

```bash
python fetch_to_csv.py
```
```bash
python fetch_to_webhook.csv
 ```
