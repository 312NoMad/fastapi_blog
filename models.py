from datetime import datetime
from pydantic import BaseModel


class PostCreate(BaseModel):
    title: str
    text: str


class PostBase(BaseModel):
    id: int
    title: str
    text: str

    created_at: datetime
    updated_at: datetime
