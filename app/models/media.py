from pydantic import BaseModel, Field
from typing import Optional


class Media(BaseModel):
    """Modèle d'un média / image (référence Google Drive ou URL)."""

    id: Optional[str] = Field(None, alias="_id")
    nom: str
    url: str
    type: Optional[str] = None  # ex: "image", "video"
    description: Optional[str] = None

    model_config = {"populate_by_name": True}
