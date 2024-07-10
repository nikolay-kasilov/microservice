from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from settings import settings

Base = declarative_base()


def setup_db():
    engine = create_async_engine(settings.db_url)
    session_factory = async_sessionmaker(bind=engine)

    return session_factory


session_factory = setup_db()
