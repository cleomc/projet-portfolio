"""
Service CRUD — logique métier au-dessus du repo MongoDB.
Transforme les documents bruts en modèles Pydantic.
"""

from app.repositories import mongo_repo
from app.models.project import Project
from app.models.tag import Tag
from app.models.certification import Certification
from app.models.hobby import Hobby
from app.models.contact import Contact
from app.models.langue import Langue


def _serialize(doc: dict | None) -> dict | None:
    """Convertit l'ObjectId MongoDB en string pour la sérialisation."""
    if doc and "_id" in doc:
        doc["_id"] = str(doc["_id"])
    return doc


def _serialize_list(docs: list[dict]) -> list[dict]:
    return [_serialize(d) for d in docs]


# ── Profil ───────────────────────────────────────

async def get_profile() -> dict | None:
    doc = await mongo_repo.get_profile()
    return _serialize(doc)


# ── Projets ──────────────────────────────────────

async def get_all_projects() -> list[dict]:
    docs = await mongo_repo.get_all_projects()
    return _serialize_list(docs)


async def get_project_by_titre(titre: str) -> dict | None:
    doc = await mongo_repo.get_project_by_titre(titre)
    return _serialize(doc)


# ── Tags / Compétences ───────────────────────────

async def get_all_tags() -> list[dict]:
    docs = await mongo_repo.get_all_tags()
    return _serialize_list(docs)


# ── Hobbies ──────────────────────────────────────

async def get_all_hobbies() -> list[dict]:
    docs = await mongo_repo.get_all_hobbies()
    return _serialize_list(docs)


# ── Certifications ───────────────────────────────

async def get_all_certifications() -> list[dict]:
    docs = await mongo_repo.get_all_certifications()
    return _serialize_list(docs)


# ── Contact ──────────────────────────────────────

async def get_all_contacts() -> list[dict]:
    docs = await mongo_repo.get_all_contacts()
    return _serialize_list(docs)


# ── Langues ──────────────────────────────────────

async def get_all_langues() -> list[dict]:
    docs = await mongo_repo.get_all_langues()
    return _serialize_list(docs)


# ── Études ───────────────────────────────────────

async def get_all_etudes() -> list[dict]:
    docs = await mongo_repo.get_all_etudes()
    return _serialize_list(docs)
