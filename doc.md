# Documentation de l'API

> Base URL : `http://localhost:8000`

---

## Health

### `GET /health`

Vérifie la connectivité aux bases de données.

**Paramètres**
```
Aucun
```

**Réponses**

- **200** :
```json
{
  "status": "ok",
  "mongo": "connected",
  "neo4j": "connected"
}
```

- **200** (dégradé — une base inaccessible) :
```json
{
  "status": "degraded",
  "mongo": "connected",
  "neo4j": "error: ..."
}
```

---

## Public (MongoDB)

### `GET /profile`

Retourne le document unique du profil.

**Paramètres**
```
Aucun
```

**Réponses**

- **200** :
```json
{
  "_id": "String",
  "nom": "String",
  "prenom": "String",
  "intro": "String"
}
```

- **200** (aucun profil trouvé) :
```json
null
```

---

### `GET /projects`

Retourne tous les projets.

**Paramètres**
```
Aucun
```

**Réponses**

- **200** :
```json
[
  {
    "_id": "String",
    "titre": "String",
    "description": "String",
    "competences": [
      {
        "nom": "String",
        "description": "String",
        "lien": "String | null"
      }
    ],
    "collaborateur": "String | null",
    "lien": "String | null",
    "periode": "String"
  }
]
```

---

### `GET /projects/{titre}`

Retourne un projet par son titre.

**Paramètres**

| Nom    | Type   | In   | Description          |
|--------|--------|------|----------------------|
| titre  | String | path | Titre exact du projet |

**Réponses**

- **200** :
```json
{
  "_id": "String",
  "titre": "String",
  "description": "String",
  "competences": [
    {
      "nom": "String",
      "description": "String",
      "lien": "String | null"
    }
  ],
  "collaborateur": "String | null",
  "lien": "String | null",
  "periode": "String"
}
```

- **200** (projet non trouvé) :
```json
null
```

---

### `GET /tags`

Retourne toutes les compétences (triées par nom, depuis MongoDB).

**Paramètres**
```
Aucun
```

**Réponses**

- **200** :
```json
[
  {
    "_id": "String",
    "nom": "String",
    "img": "String | null"
  }
]
```

---

### `GET /hobbies`

Retourne tous les hobbies.

**Paramètres**
```
Aucun
```

**Réponses**

- **200** :
```json
[
  {
    "_id": "String",
    "titre": "String",
    "description": "String",
    "img": "String | null",
    "lien": "String | null"
  }
]
```

---

### `GET /certifications`

Retourne toutes les certifications.

**Paramètres**
```
Aucun
```

**Réponses**

- **200** :
```json
[
  {
    "_id": "String",
    "description": "String",
    "date": "String",
    "img": "String | null",
    "lien": "String | null"
  }
]
```

---

### `GET /contact`

Retourne les moyens de contact.

**Paramètres**
```
Aucun
```

**Réponses**

- **200** :
```json
[
  {
    "_id": "String",
    "nom": "String",
    "valeur": "String",
    "img": "String | null",
    "lien": "String | null"
  }
]
```

---

### `GET /langues`

Retourne les langues parlées.

**Paramètres**
```
Aucun
```

**Réponses**

- **200** :
```json
[
  {
    "_id": "String",
    "nom": "String",
    "niveau": "String"
  }
]
```

---

### `GET /etudes`

Retourne les études / formations.

**Paramètres**
```
Aucun
```

**Réponses**

- **200** :
```json
[
  {
    "_id": "String",
    "titre": "String",
    "etablissement": "String",
    "description": "String",
    "periode": "String",
    "diplome": "String",
    "lien": "String | null"
  }
]
```

---

## Graph (Neo4j)

### `GET /graph/projects`

Retourne tous les projets avec leurs compétences depuis le graphe Neo4j.

**Paramètres**
```
Aucun
```

**Réponses**

- **500** : ⚠️ *Endpoint pas encore implémenté (`NotImplementedError`).*

---

### `GET /graph/projects/{titre}/competences`

Retourne les compétences d'un projet donné, groupées par titre de projet.

**Paramètres**

| Nom    | Type   | In   | Description          |
|--------|--------|------|----------------------|
| titre  | String | path | Titre exact du projet |

**Réponses**

- **200** :
```json
{
  "Chatbot IA": {
    "react": {
      "description": "Interface de chat temps réel",
      "img": "String | null"
    },
    "docker": {
      "description": "Déploiement multi-conteneurs",
      "img": "String | null"
    },
    "python": {
      "description": "Intégration des modèles de langage",
      "img": "String | null"
    }
  }
}
```

> **Note** : `description` et `img` proviennent de la **relation** `A_IMPLIQUE`, pas du nœud Competence.

- **200** (projet non trouvé ou sans compétences) :
```json
{}
```

---

### `GET /graph/competences`

Retourne toutes les compétences du graphe Neo4j.

**Paramètres**
```
Aucun
```

**Réponses**

- **200** :
```json
{
  "python": {
    "img": "https://upload.wikimedia.org/..."
  },
  "react": {
    "img": "https://upload.wikimedia.org/..."
  },
  "mongodb": {
    "img": null
  }
}
```

> **Note** : `img` provient du **nœud** Competence dans Neo4j.
