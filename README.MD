# Brussels - Christian

Bruxelles, capitale de l’Europe et centre névralgique de la Belgique, souhaite moderniser l’accès et
l’analyse des données liées à son activité urbaine. Votre équipe a été sollicitée pour développer une
solution visant à centraliser, structurer et exploiter diérentes données relatives à la ville. Ces
données permettront de mieux comprendre son fonctionnement et de fournir des services utiles aux
citoyens, entreprises, et gestionnaires urbains.

Notre mission est de concevoir et de développer un pipeline complet de gestion des données, allant
de leur collecte à leur exposition via une API, tout en assurant la cohérence et la qualité des
informations dans la base

## Setup

### 1. Créer votre Environnement Virtuel (venv)

Lancez en ligne de commandes :

#### MacOS

- `python3 -m venv .venv`.
- `source .venv/bin/activate`

#### Windows

- `python3 -m venv .venv`
- `.venv\Scripts\activate.ps1`

#### Quitter l'environnement virtuel quand vous voulez

Lancez en ligne de commandes `deactivate`

### 2. Installez toutes les dépendances (à faire en ligne de commandes) :

`python3 -m pip install -r requirements.txt`

### 3. Lancer docker

- `docker-compose up -d`

## Lancer le projet

### Récupérer les variables d'envrionnement

Renommez le fichier `.env.example` en `.env` et demandez au développeur les valeurs à indiquer pour chaque variable.

### Exécuter le script principal

Il suffit d'exécuter le script principal en ligne de commandes :

`python main.py`

> Note : en ligne de commandes, il se peut que vous ayez à remplacer `python` par `py`, `python3` ou `python3.11` selon la version de python que vous utilisez sur votre machine.

## Version de python

Développé en [python3](https://www.python.org/download/releases/3.0/)
