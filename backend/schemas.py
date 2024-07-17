from pydantic import BaseModel
from datetime import datetime


class CreatePostSchema(BaseModel):
    title: str
    content: str
    timestamp: datetime

    def to_dict(self):
        return {
            "title": self.title,
            "content": self.content,
            "timestamp": self.timestamp.strftime("%Y-%m-%dT%H:%M"),
        }


class GetPostSchema(CreatePostSchema):
    id: int
