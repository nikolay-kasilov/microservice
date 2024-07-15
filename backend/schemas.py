from pydantic import BaseModel
from datetime import datetime


class CreatePostSchema(BaseModel):
    title: str
    content: str
    timestamp: datetime


class GetPostSchema(CreatePostSchema):
    id: int
