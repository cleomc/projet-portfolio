from pydantic import BaseModel, Field
from typing import Optional


class Contact(BaseModel):
    """Modèle d'un moyen de contact (MongoDB)."""

    id: Optional[str] = Field(None, alias="_id")
    nom: str
    valeur: str
    img: Optional[str] = None
    lien: Optional[str] = None

    model_config = {"populate_by_name": True}
