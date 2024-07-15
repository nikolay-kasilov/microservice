from fastapi import FastAPI
from schemas import GetPostSchema, CreatePostSchema
import aiohttp
from settings import settings as s


async def get_posts() -> list[GetPostSchema]:
    async with aiohttp.ClientSession() as session:
        async with session.get(f"http://{s.CORE_HOST}:{s.CORE_PORT}/api") as resp:
            data = await resp.json()
    return [GetPostSchema(**post) for post in data]


async def create_posts(post_data: CreatePostSchema) -> GetPostSchema:
    async with aiohttp.ClientSession() as session:
        async with session.post(
            f"http://{s.CORE_HOST}:{s.CORE_PORT}/api", data=post_data.model_dump_json()
        ) as resp:
            data = await resp.json()
            print(data)
    return GetPostSchema(**data)


def setup_app():
    application = FastAPI()
    application.add_api_route("/api/post", create_posts, methods=["POST"])
    application.add_api_route("/api/post", get_posts, methods=["GET"])
    return application


app = setup_app()
