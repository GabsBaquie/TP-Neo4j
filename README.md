# TD-NEO4J

## Prérequis
- Python 3.x
- Neo4j
- Environnement virtuel Python

## Installation

### 1. Configuration de l'environnement
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Installation des dépendances
```bash
pip install -r requirements.txt
```

### 3. Configuration de Neo4j
```bash
brew services start neo4j
```

### 4. Lancement de l'application
```bash
python app.py
```

## Endpoints API
- `/` - Page d'accueil
- `/api/users` - Gestion des utilisateurs
- `/api/posts` - Gestion des posts
- `/api/comments` - Gestion des commentaires