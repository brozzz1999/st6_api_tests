from pydantic import BaseModel, Field


class Meme(BaseModel):
    id: str
    info: object
    tags: dict
    text: str
    updated_by: str
    url: str
