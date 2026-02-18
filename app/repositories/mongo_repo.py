"""
Fonctions de lecture / écriture dans MongoDB.
L'utilisateur complétera les requêtes selon ses besoins.
"""

from app.db.mongo import get_db


# ── Profil (moi) ─────────────────────────────────

async def get_profile():
    """Retourne le document unique du profil."""
    db = get_db()
    # TODO
    raise NotImplementedError
    return None


# ── Projets ──────────────────────────────────────

async def get_all_projects():
    """Retourne tous les projets."""
    db = get_db()
    # TODO
    raise NotImplementedError
    return None


async def get_project_by_titre(titre: str):
    """Retourne un projet par son titre."""
    db = get_db()
    # TODO
    raise NotImplementedError
    return None


# ── Compétences / Tags ───────────────────────────

async def get_all_tags():
    """Retourne toutes les compétences."""
    db = get_db()
    # TODO
    raise NotImplementedError
    return None


# ── Hobbies ──────────────────────────────────────

async def get_all_hobbies():
    """Retourne tous les hobbies."""
    db = get_db()
    # TODO
    raise NotImplementedError
    return None


# ── Certifications ───────────────────────────────

async def get_all_certifications():
    """Retourne toutes les certifications."""
    db = get_db()
    # TODO
    raise NotImplementedError
    return None


# ── Contact ──────────────────────────────────────

async def get_all_contacts():
    """Retourne tous les moyens de contact."""
    db = get_db()
    # TODO
    raise NotImplementedError
    return None


# ── Langues ──────────────────────────────────────

async def get_all_langues():
    """Retourne toutes les langues."""
    db = get_db()
    # TODO
    raise NotImplementedError
    return None
