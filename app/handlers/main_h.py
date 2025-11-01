from typing import Any
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart

import app.keyboards.main_k as kb


main_r = Router()


@main_r.message(CommandStart())
async def cmd_start(message: Message) -> Any:
    await message.answer("🌸こんにちは!\n" +
                        "Добро пожаловать в наш уютный уголок, где ты сможешь поподробнее изучить японский язык, " + 
                         "а также узнать некоторые интересные факты о Японии и её культуре", reply_markup=kb.main)


