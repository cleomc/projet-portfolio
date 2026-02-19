# Portfolio API 🚀

API FastAPI servant les données d'un portfolio personnel, avec **MongoDB** (données documentaires) et **Neo4j** (graphe projets ↔ compétences).

## Prérequis

- [Docker](https://docs.docker.com/get-docker/) & Docker Compose

## Lancement

```bash
# 1. Lancer les services (FastAPI + MongoDB + Neo4j)
docker compose up -d --build

# 2. Insérer les données d'exemple
docker compose exec api python -m seed.seed

# 3. Vérifier que tout fonctionne
curl http://localhost:8000/health

# 4 voir les msg api en live
docker compose logs -f api
```

## Endpoints

### Health
| Méthode | Route | Description |
|---------|-------|-------------|
| GET | `/health` | Vérifier la connectivité aux bases |

### Données publiques (MongoDB)
| Méthode | Route | Description |
|---------|-------|-------------|
| GET | `/profile` | Profil (moi) |
| GET | `/projects` | Tous les projets |
| GET | `/projects/{titre}` | Un projet par titre |
| GET | `/tags` | Toutes les compétences |
| GET | `/hobbies` | Hobbies |
| GET | `/certifications` | Certifications |
| GET | `/contact` | Moyens de contact |
| GET | `/langues` | Langues parlées |

### Graphe (Neo4j)
| Méthode | Route | Description |
|---------|-------|-------------|
| GET | `/graph/projects` | Projets avec compétences liées |
| GET | `/graph/projects/{titre}/competences` | Compétences d'un projet |
| GET | `/graph/competences` | Toutes les compétences du graphe |

## Documentation interactive

Une fois lancé, la doc Swagger est accessible sur :
- **Swagger UI** : [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc** : [http://localhost:8000/redoc](http://localhost:8000/redoc)

## Neo4j Browser

Visualisez le graphe directement : [http://localhost:7474](http://localhost:7474)

## Structure du projet

```
portfolio-api/
├── app/
│   ├── main.py               # point d'entrée FastAPI
│   ├── core/config.py        # lecture .env
│   ├── db/
│   │   ├── mongo.py          # connexion MongoDB
│   │   └── neo4j.py          # connexion Neo4j
│   ├── models/               # modèles Pydantic
│   ├── repositories/         # accès données (Mongo / Neo4j)
│   ├── services/             # logique métier
│   └── routers/              # routes FastAPI
├── seed/
│   ├── data/                 # fichiers JSON de seed
│   └── seed.py               # script d'insertion
├── .env
├── docker-compose.yml
├── Dockerfile
└── requirements.txt
```

## Seed

Les fichiers JSON dans `seed/data/` contiennent des données d'exemple. Remplacez-les par vos vraies données, puis relancez :

```bash
docker compose exec api python -m seed.seed
```
