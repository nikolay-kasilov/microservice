from schemas import GetPostSchema, CreatePostSchema
from models import PostORM
from database import session_factory
from sqlalchemy import select


async def create_post(post_data: CreatePostSchema) -> GetPostSchema:
    async with session_factory() as session:
        """ 
        {"title": "test", "content": "test"} ->
        title=test, content=test
        """
        post_orm = PostORM(**post_data.model_dump())
        session.add(post_orm)
        await session.commit()
        await session.refresh(post_orm)
        return GetPostSchema(**post_orm.__dict__)


async def get_posts() -> list[GetPostSchema]:
    async with session_factory() as session:
        query = select(PostORM)
        result = await session.execute(query)
        curr = result.scalars()
        res = [GetPostSchema(**row.__dict__) for row in curr]
        return res
