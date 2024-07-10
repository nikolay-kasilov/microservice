from database import Base
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime


class PostORM(Base):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    content: Mapped[str]
    timestamp: Mapped[datetime]
    author: Mapped[str | None]
