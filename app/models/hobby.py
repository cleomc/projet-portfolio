from pydantic import BaseModel, Field
from typing import Optional


class Hobby(BaseModel):
    """Modèle d'un hobby / loisir (MongoDB)."""

    id: Optional[str] = Field(None, alias="_id")
    titre: str
    description: Optional[str] = None
    img: Optional[str] = None
    lien: Optional[str] = None

    model_config = {"populate_by_name": True}
