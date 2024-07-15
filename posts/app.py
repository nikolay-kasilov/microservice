from fastapi import FastAPI
from routing import router
from logger import logger


def create_application():
    application = FastAPI()
    application.include_router(router=router, prefix="/api")
    logger.info(f"{application=}")

    return application


app = create_application()
