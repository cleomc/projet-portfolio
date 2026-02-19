"""
Fonctions de lecture dans Neo4j (graphe projets ↔ compétences).
L'utilisateur complétera les requêtes Cypher selon ses besoins.
"""


from app.db.neo4j import get_driver


async def get_all_projects_with_competences():
    """Retourne tous les projets avec leurs compétences liées."""
    driver = get_driver()
    query = """
    MATCH (Projet:Projet) - [A_IMPLIQUE : A_IMPLIQUE] -> (Competence:Competence)
    RETURN Projet, A_IMPLIQUE, Competence
    """
    records = None
    async with driver.session() as session:
        result = await session.run(query)
        records = [record.data() async for record in result]
        return records

async def get_competences_for_project(titre: str):
    """Retourne les compétences liées à un projet donné."""
    driver = get_driver()
    records = None
    async with driver.session() as session:
        # TODO
        raise NotImplementedError
    return records


async def get_all_competences():
    """Retourne toutes les compétences du graphe."""
    driver = get_driver()
    records = None
    async with driver.session() as session:
        # TODO
        raise NotImplementedError
    return records
