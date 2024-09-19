from datetime import datetime

from sqlalchemy import insert
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from database.db_config import db_settings
from database.models import link


async def create_session_db() -> AsyncSession:
    engine = create_async_engine(
        f"postgresql+asyncpg://{db_settings.DB_USER}:{db_settings.DB_PASS}@{db_settings.DB_HOST}:{db_settings.DB_PORT}/{db_settings.DB_NAME}", echo=True
    )
    async_session = sessionmaker(
        engine, class_=AsyncSession, expire_on_commit=False
    )

    return async_session


async def add_data(url: str, hashid: str, start_life: datetime, end_life: datetime):
    async_session = await create_session_db()

    async with async_session() as session:
        async with session.begin():
            stmt = insert(link).values(
                url=url,
                hashid=hashid,
                start_life=start_life,
                end_life=end_life
            )

            await session.execute(stmt)
        
        await session.commit()