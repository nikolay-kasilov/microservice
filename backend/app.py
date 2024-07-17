from fastapi import FastAPI
from schemas import GetPostSchema, CreatePostSchema
import aiohttp
from settings import settings as s
from logger import logger


async def get_posts() -> list[GetPostSchema]:
    async with aiohttp.ClientSession() as session:
        async with session.get(f"http://{s.CORE_HOST}:{s.CORE_PORT}/api") as resp:
            data = await resp.json()
    return [GetPostSchema(**post) for post in data]


async def create_posts(post_data: CreatePostSchema) -> GetPostSchema:
    async with aiohttp.ClientSession() as session:
        async with session.post(
            f"http://{s.CORE_HOST}:{s.CORE_PORT}/api", json=post_data.to_dict()
        ) as resp:
            data = await resp.json()
            logger.info(f"{[data]}")
    return GetPostSchema(**data)


def setup_app():
    application = FastAPI()
    application.add_api_route("/api/post", create_posts, methods=["POST"])
    application.add_api_route("/api/post", get_posts, methods=["GET"])
    return application


app = setup_app()
