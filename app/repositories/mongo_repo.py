"""
Fonctions de lecture / écriture dans MongoDB.

"""
from __future__ import annotations

from typing import Optional

from app.db.mongo import get_db




# ── Profil (moi) ─────────────────────────────────

async def get_profile() -> Optional[dict]:
    """Retourne le document unique du profil (collection: moi)."""
    db = get_db()
    doc = await db["moi"].find_one({})
    return doc


# ── Projets ──────────────────────────────────────

async def get_all_projects(limit: int = 100) -> list[dict]:
    """
    Retourne tous les projets (collection: projets).
    - limit paramétrable pour éviter de renvoyer un JSON énorme par accident
    """
    db = get_db()
    docs = await db["projets"].find({}).to_list(length=limit)
    return docs


async def get_project_by_titre(titre: str) -> Optional[dict]:
    """Retourne un projet par son titre (collection: projets)."""
    db = get_db()
    doc = await db["projets"].find_one({"titre": titre})
    return doc


# ─────────────────────────────────────────────────────────────
# Fonctions supplémentaires (nouvelles) — pour plus d'interactions
# ─────────────────────────────────────────────────────────────

async def get_projects_paginated(limit: int = 10, skip: int = 0) -> list[dict]:
    """
  pagination simple.
    """
    db = get_db()
    docs = await (
        db["projets"]
        .find({})
        .skip(skip)
        .limit(limit)
        .to_list(length=limit)
    )
    return docs


async def search_projects(query: str, limit: int = 50) -> list[dict]:
    """
   recherche simple (regex case-insensitive) sur titre + description.

    """
    db = get_db()
    docs = await db["projets"].find({
        "$or": [
            {"titre": {"$regex": query, "$options": "i"}},
            {"description": {"$regex": query, "$options": "i"}},
        ]
    }).limit(limit).to_list(length=limit)
    return docs


async def get_projects_by_competence(nom: str, limit: int = 100) -> list[dict]:
    """
    filtrer les projets par compétence sans changer ta structure actuelle.
    """
    db = get_db()
    docs = await db["projets"].find({"competences.nom": nom}).to_list(length=limit)
    return docs


async def count_projects() -> int:
    """ compter le nombre total de projets."""
    db = get_db()
    return await db["projets"].count_documents({})


async def get_recent_projects(limit: int = 5) -> list[dict]:
    """
    récupérer les projets les plus récents.

    Sans champ created_at dans ton JSON, on utilise le tri par _id (ObjectId),
    qui est chronologique.
    """
    db = get_db()
    docs = await (
        db["projets"]
        .find({})
        .sort("_id", -1)
        .limit(limit)
        .to_list(length=limit)
    )
    return docs


# ── Compétences / Tags ───────────────────────────

async def get_all_tags(limit: int = 200) -> list[dict]:
    """
    Retourne toutes les compétences (collection: competences).
    - tri alphabétique
    - limit pour éviter les gros retours
    """
    db = get_db()
    docs = await db["competences"].find({}).sort("nom", 1).to_list(length=limit)
    return docs


# ── Hobbies ──────────────────────────────────────

async def get_all_hobbies(limit: int = 200) -> list[dict]:
    """Retourne tous les hobbies (collection: hobbies)."""
    db = get_db()
    docs = await db["hobbies"].find({}).to_list(length=limit)
    return docs


# ── Certifications ───────────────────────────────

async def get_all_certifications(limit: int = 200) -> list[dict]:
    """Retourne toutes les certifications (collection: certifications)."""
    db = get_db()
    docs = await db["certifications"].find({}).to_list(length=limit)
    return docs


# ── Contact ──────────────────────────────────────

async def get_all_contacts(limit: int = 200) -> list[dict]:
    """Retourne tous les moyens de contact (collection: contact)."""
    db = get_db()
    docs = await db["contact"].find({}).to_list(length=limit)
    return docs


# ── Langues ──────────────────────────────────────

async def get_all_langues(limit: int = 200) -> list[dict]:
    """Retourne toutes les langues (collection: langues)."""
    db = get_db()
    docs = await db["langues"].find({}).to_list(length=limit)
    return docs


async def get_all_etudes():
    """Retourne toutes les études / formations."""
    db = get_db()
    docs = await db["etudes"].find({}).to_list(length=limit)
    return docs
