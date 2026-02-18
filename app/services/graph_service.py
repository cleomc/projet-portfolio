"""
Service Graph — logique métier au-dessus du repo Neo4j.
"""

from app.repositories import neo4j_repo


async def get_all_projects_with_competences() -> list[dict]:
    """Retourne tous les projets avec leurs compétences."""
    return await neo4j_repo.get_all_projects_with_competences()


async def get_competences_for_project(titre: str) -> list[dict]:
    """Retourne les compétences d'un projet donné."""
    return await neo4j_repo.get_competences_for_project(titre)


async def get_all_competences() -> list[dict]:
    """Retourne toutes les compétences du graphe."""
    return await neo4j_repo.get_all_competences()
