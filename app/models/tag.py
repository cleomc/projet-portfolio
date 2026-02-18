from pydantic import BaseModel, Field
from typing import Optional


class Tag(BaseModel):
    """Modèle d'une compétence / tag (MongoDB + Neo4j)."""

    id: Optional[str] = Field(None, alias="_id")
    nom: str
    description: Optional[str] = None
    img: Optional[str] = None
    lien: Optional[str] = None

    model_config = {"populate_by_name": True}
