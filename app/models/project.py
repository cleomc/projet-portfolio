from pydantic import BaseModel, Field
from typing import Optional


class Project(BaseModel):
    """Modèle d'un projet (MongoDB)."""

    id: Optional[str] = Field(None, alias="_id")
    titre: str
    description: str
    competences: list[str] = []  # liste d'ids de compétences
    collaborateur: Optional[str] = None
    lien: Optional[str] = None
    periode: Optional[str] = None

    model_config = {"populate_by_name": True}
