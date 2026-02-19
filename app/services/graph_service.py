"""
Service Graph — logique métier au-dessus du repo Neo4j.
"""

from app.repositories import neo4j_repo


async def get_all_projects_with_competences() -> dict[str, dict]:
    """Retourne tous les projets avec leurs compétences."""
    records = await neo4j_repo.get_all_projects_with_competences()
    result = {}
    for record in records:
        projet_titre = record["Projet"]["titre"]
        comp_nom = record["Competence"]["nom"]
        if projet_titre not in result:
            result[projet_titre] = {}
        result[projet_titre][comp_nom] = {
           # "description": record["A_IMPLIQUE"].get("description"),
           # "img": record["A_IMPLIQUE"].get("img"),
           "description": record["A_IMPLIQUE"].get("description"),
           "img": record["A_IMPLIQUE"].get("img")
        }
    return result


async def get_competences_for_project(titre: str) -> list[dict]:
    """Retourne les compétences d'un projet donné."""
    return await neo4j_repo.get_competences_for_project(titre)


async def get_all_competences() -> list[dict]:
    """Retourne toutes les compétences du graphe."""
    return await neo4j_repo.get_all_competences()
