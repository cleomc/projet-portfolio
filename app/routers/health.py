"""
Route health-check — vérifie la connectivité aux bases.
"""

from fastapi import APIRouter
from app.db.mongo import get_db
from app.db.neo4j import get_driver

router = APIRouter(tags=["Health"])


@router.get("/health")
async def health():
    """Vérifie que MongoDB et Neo4j sont accessibles."""
    status = {"status": "ok", "mongo": "disconnected", "neo4j": "disconnected"}

    # MongoDB
    try:
        db = get_db()
        await db.command("ping")
        status["mongo"] = "connected"
    except Exception as e:
        status["status"] = "degraded"
        status["mongo"] = f"error: {e}"

    # Neo4j
    try:
        driver = get_driver()
        async with driver.session() as session:
            await session.run("RETURN 1")
        status["neo4j"] = "connected"
    except Exception as e:
        status["status"] = "degraded"
        status["neo4j"] = f"error: {e}"

    return status
