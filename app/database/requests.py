from sqlalchemy import select, func
from sqlalchemy.exc import NoResultFound

from app.database.models import Word
from app.database.models import async_session


async def get_word() -> Word | None:
    query = select(Word)
    async with async_session() as session:
        result = await session.execute(query)
        try:
            return result.scalar()
        except NoResultFound:
            return None


async def get_all_words() -> list[dict]:
    async with async_session() as session:
        stmt = select(Word)
        result = await session.execute(stmt)
        words = result.scalars().all()
        word_dict = [word.to_dict() for word in words]
        return word_dict


async def count_words() -> int:
    async with async_session() as session:
        words = await session.execute(select(func.count()).select_from(Word))
        return words.scalar()
