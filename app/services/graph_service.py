"""
Service Graph — logique métier au-dessus du repo Neo4j.
"""

from app.repositories import neo4j_repo


async def get_all_projects_with_competences() -> list[dict]:
    """Retourne tous les projets avec leurs compétences."""
    return await neo4j_repo.get_all_projects_with_competences()


async def get_competences_for_project(titre: str) -> dict:
    """Retourne les compétences d'un projet donné, groupées par projet."""
    records = await neo4j_repo.get_competences_for_project(titre)
    result = {}
    for record in records:
        projet_titre = record["p"]["titre"]
        comp_nom = record["c"]["nom"]
        if projet_titre not in result:
            result[projet_titre] = {}
        result[projet_titre][comp_nom] = {
            "description": record["i"].get("description"),
            "img": record["i"].get("img"),
        }
    return result


async def get_all_competences() -> dict:
    """Retourne toutes les compétences du graphe."""
    records = await neo4j_repo.get_all_competences()
    return {
        record["c"]["nom"]: {"img": record["c"].get("img")}
        for record in records
    }
