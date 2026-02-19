"""
Routes publiques — données du portfolio depuis MongoDB.
"""

from fastapi import APIRouter
from app.services import crud_service

router = APIRouter(tags=["Public"])


@router.get("/profile")
async def profile():
    """Retourne le profil (moi)."""
    return await crud_service.get_profile()


@router.get("/projects")
async def projects():
    """Retourne tous les projets."""
    return await crud_service.get_all_projects()


@router.get("/projects/{titre}")
async def project_by_titre(titre: str):
    """Retourne un projet par son titre."""
    return await crud_service.get_project_by_titre(titre)


@router.get("/tags")
async def tags():
    """Retourne toutes les compétences / tags."""
    return await crud_service.get_all_tags()


@router.get("/hobbies")
async def hobbies():
    """Retourne tous les hobbies."""
    return await crud_service.get_all_hobbies()


@router.get("/certifications")
async def certifications():
    """Retourne toutes les certifications."""
    return await crud_service.get_all_certifications()


@router.get("/contact")
async def contact():
    """Retourne les moyens de contact."""
    return await crud_service.get_all_contacts()


@router.get("/langues")
async def langues():
    """Retourne les langues parlées."""
    return await crud_service.get_all_langues()


@router.get("/etudes")
async def etudes():
    """Retourne les études / formations."""
    return await crud_service.get_all_etudes()
