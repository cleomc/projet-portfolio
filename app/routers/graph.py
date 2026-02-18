"""
Routes graphe — données Neo4j (projets ↔ compétences).
"""

from fastapi import APIRouter
from app.services import graph_service

router = APIRouter(prefix="/graph", tags=["Graph"])


@router.get("/projects")
async def graph_projects():
    """Retourne tous les projets avec leurs compétences (Neo4j)."""
    return await graph_service.get_all_projects_with_competences()


@router.get("/projects/{titre}/competences")
async def graph_project_competences(titre: str):
    """Retourne les compétences d'un projet donné (Neo4j)."""
    return await graph_service.get_competences_for_project(titre)


@router.get("/competences")
async def graph_competences():
    """Retourne toutes les compétences du graphe (Neo4j)."""
    return await graph_service.get_all_competences()
