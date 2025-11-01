from typing import Any
from aiogram import Router, F
from aiogram.types import Message


constructions_r = Router()


@constructions_r.message(F.text.lower() == "конструкции")
async def constructions(message: Message) -> Any:
    await message.answer("тут будут конструкции")
