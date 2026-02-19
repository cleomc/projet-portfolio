"""
Script de seed — insère les données JSON dans MongoDB et Neo4j.

Usage (depuis la racine du projet, dans le container) :
    python -m seed.seed
"""

import asyncio
import json
from pathlib import Path

from motor.motor_asyncio import AsyncIOMotorClient
from neo4j import AsyncGraphDatabase

# ── On utilise les settings de l'app ─────────────
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app.core.config import settings

DATA_DIR = Path(__file__).resolve().parent / "data"


def load_json(filename: str):
    """Charge un fichier JSON depuis le dossier data/."""
    filepath = DATA_DIR / filename
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)


# ══════════════════════════════════════════════════
#  MongoDB
# ══════════════════════════════════════════════════

async def seed_mongo():
    """Insère toutes les données dans MongoDB."""
    client = AsyncIOMotorClient(settings.MONGO_URI)
    db = client[settings.MONGO_DB_NAME]

    # On nettoie d'abord les collections existantes
    collections = ["moi", "projets", "competences", "hobbies",
                   "certifications", "contact", "langues", "etudes"]
    for col in collections:
        await db[col].delete_many({})

    # ── Moi (document unique) ──
    moi = load_json("moi.json")
    await db.moi.insert_one(moi)
    print(f"  ✅ moi : 1 document inséré")

    # ── Collections multiples ──
    mapping = {
        "projets": "projets.json",
        "competences": "competences.json",
        "hobbies": "hobbies.json",
        "certifications": "certifications.json",
        "contact": "contact.json",
        "langues": "langues.json",
        "etudes": "etudes.json",
    }
    for col_name, filename in mapping.items():
        data = load_json(filename)
        if data:
            await db[col_name].insert_many(data)
            print(f"  ✅ {col_name} : {len(data)} documents insérés")

    client.close()
    print("📦 MongoDB seed terminé !\n")


# ══════════════════════════════════════════════════
#  Neo4j
# ══════════════════════════════════════════════════

async def seed_neo4j():
    """Crée les nœuds et relations dans Neo4j."""
    # Neo4j peut mettre du temps à démarrer — on retente plusieurs fois
    driver = None
    for attempt in range(1, 11):
        try:
            driver = AsyncGraphDatabase.driver(
                settings.NEO4J_URI,
                auth=(settings.NEO4J_USER, settings.NEO4J_PASSWORD),
            )
            async with driver.session() as s:
                await s.run("RETURN 1")
            print(f"  ✅ Neo4j connecté (tentative {attempt})")
            break
        except Exception:
            print(f"  ⏳ Neo4j pas encore prêt, tentative {attempt}/10…")
            if driver:
                await driver.close()
                driver = None
            await asyncio.sleep(3)
    else:
        print("  ❌ Impossible de se connecter à Neo4j après 10 tentatives")
        return

    projets = load_json("projets.json")
    competences = load_json("competences.json")

    async with driver.session() as session:
        # Nettoyer le graphe
        await session.run("MATCH (n) DETACH DELETE n")

        # Créer les nœuds Competence (nom + img)
        for comp in competences:
            await session.run(
                """
                MERGE (c:Competence {nom: $nom})
                SET c.img = $img
                """,
                nom=comp["nom"],
                img=comp.get("img"),
            )
        print(f"  ✅ Neo4j : {len(competences)} nœuds Competence créés")

        # Créer les nœuds Projet + relations A_IMPLIQUE (avec description sur la relation)
        for proj in projets:
            await session.run(
                """
                CREATE (p:Projet {titre: $titre})
                """,
                titre=proj["titre"],
            )
            for comp_data in proj.get("competences", []):
                await session.run(
                    """
                    MATCH (p:Projet {titre: $titre})
                    MATCH (c:Competence {nom: $comp_nom})
                    CREATE (p)-[:A_IMPLIQUE {
                        description: $description,
                        lien: $lien
                    }]->(c)
                    """,
                    titre=proj["titre"],
                    comp_nom=comp_data["nom"],
                    description=comp_data.get("description", ""),
                    lien=comp_data.get("lien"),
                )
        print(f"  ✅ Neo4j : {len(projets)} nœuds Projet créés avec relations")

    await driver.close()
    print("📦 Neo4j seed terminé !\n")


# ══════════════════════════════════════════════════
#  Main
# ══════════════════════════════════════════════════

async def main():
    print("\n🌱 Démarrage du seed...\n")
    await seed_mongo()
    await seed_neo4j()
    print("🎉 Seed complet !")


if __name__ == "__main__":
    asyncio.run(main())
