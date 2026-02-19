from pydantic import BaseModel, Field
from typing import Optional


class Etude(BaseModel):
    """Modèle d'une étude / formation (MongoDB)."""

    id: Optional[str] = Field(None, alias="_id")
    titre: str
    etablissement: str
    description: Optional[str] = None
    periode: Optional[str] = None
    diplome: Optional[str] = None
    lien: Optional[str] = None

    model_config = {"populate_by_name": True}
