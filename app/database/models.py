import os
from sqlalchemy import inspect
from dotenv import load_dotenv
from typing import Annotated, Optional
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine


load_dotenv()
engine = create_async_engine(url=os.getenv('SQLALCHEMY_URL'))
async_session = async_sessionmaker(engine)
intpk = Annotated[int, mapped_column(primary_key=True)]


class Base(AsyncAttrs, DeclarativeBase):
    pass


class Word(Base):
    __tablename__ = 'words'

    id: Mapped[intpk]
    word: Mapped[str]
    pronouns: Mapped[str]
    translate: Mapped[str]
    conjugation: Mapped[str]
    frForm: Mapped[str]
    scForm: Mapped[str]
    thForm: Mapped[str]
    teForm: Mapped[str]
    taForm: Mapped[str]

    def to_dict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}


async def async_main() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
