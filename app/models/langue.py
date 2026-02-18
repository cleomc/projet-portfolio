from pydantic import BaseModel, Field
from typing import Optional


class Langue(BaseModel):
    """Modèle d'une langue parlée (MongoDB)."""

    id: Optional[str] = Field(None, alias="_id")
    nom: str
    niveau: str

    model_config = {"populate_by_name": True}
