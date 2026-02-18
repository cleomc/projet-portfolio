from neo4j import AsyncGraphDatabase
from app.core.config import settings

driver = None


async def connect_neo4j():
    """Ouvre la connexion Neo4j."""
    global driver
    driver = AsyncGraphDatabase.driver(
        settings.NEO4J_URI,
        auth=(settings.NEO4J_USER, settings.NEO4J_PASSWORD),
    )
    # Vérifie la connectivité
    async with driver.session() as session:
        await session.run("RETURN 1")
    print("✅ Neo4j connecté")


async def close_neo4j():
    """Ferme la connexion Neo4j."""
    global driver
    if driver:
        await driver.close()
        print("🔌 Neo4j déconnecté")


def get_driver():
    """Retourne le driver Neo4j courant."""
    return driver
