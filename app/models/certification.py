from pydantic import BaseModel, Field
from typing import Optional


class Certification(BaseModel):
    """Modèle d'une certification (MongoDB)."""

    id: Optional[str] = Field(None, alias="_id")
    description: str
    date: Optional[str] = None
    img: Optional[str] = None
    lien: Optional[str] = None

    model_config = {"populate_by_name": True}
