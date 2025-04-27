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
# Installation avec Homebrew
brew install neo4j

# Démarrage du service
brew services start neo4j

# Configuration du mot de passe
neo4j-admin set-initial-password votreMotDePasse
```

### 4. Lancement de l'application
```bash
python app.py
```

## Guide de Test des Routes API

### Utilisateurs

#### Créer un utilisateur
```bash
curl -X POST http://localhost:5000/api/users \
  -H "Content-Type: application/json" \
  -d '{"name": "John Doe", "email": "john@example.com"}'
```

#### Lister les utilisateurs
```bash
curl http://localhost:5000/api/users
```

#### Mettre à jour un utilisateur
```bash
curl -X PUT http://localhost:5000/api/users/1 \
  -H "Content-Type: application/json" \
  -d '{"name": "John Updated", "email": "john.updated@example.com"}'
```

#### Supprimer un utilisateur
```bash
curl -X DELETE http://localhost:5000/api/users/1
```

### Posts

#### Créer un post
```bash
curl -X POST http://localhost:5000/api/users/1/posts \
  -H "Content-Type: application/json" \
  -d '{"title": "Mon premier post", "content": "Contenu du post"}'
```

#### Lister les posts
```bash
curl http://localhost:5000/api/posts
```

### Commentaires

#### Ajouter un commentaire
```bash
curl -X POST http://localhost:5000/api/posts/1/comments \
  -H "Content-Type: application/json" \
  -d '{"user_id": 1, "content": "Super post!"}'
```

#### Lister les commentaires d'un post
```bash
curl http://localhost:5000/api/posts/1/comments
```

### Relations

#### Ajouter un ami
```bash
curl -X POST http://localhost:5000/api/users/1/friends \
  -H "Content-Type: application/json" \
  -d '{"friend_id": 2}'
```

#### Liker un post
```bash
curl -X POST http://localhost:5000/api/posts/1/like \
  -H "Content-Type: application/json" \
  -d '{"user_id": 1}'
```

## Structure du Projet
```
TD-Neo4j/
├── app.py           # Point d'entrée de l'application
├── requirements.txt # Dépendances
├── models/         # Modèles de données
│   ├── utilisateur.py
│   ├── post.py
│   ├── commentaire.py
│   └── relations.py
└── routes/         # Routes API
    ├── users.py
    ├── posts.py
    └── comments.py
```

## Fonctionnalités

- [x] Gestion des utilisateurs (CRUD)
- [x] Gestion des posts (CRUD)
- [x] Gestion des commentaires (CRUD)
- [x] Relations d'amitié entre utilisateurs
- [x] Système de like pour posts et commentaires
