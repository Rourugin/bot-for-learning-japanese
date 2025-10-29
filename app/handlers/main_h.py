from typing import Any
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart


main_r = router()


@main_router.message(CommandStart())
async def cmd_start(message: Message) -> Any:
    await message.answer("🌸こんにちは!\n" +
                        "Добро пожаловать в наш уютный уголок, где ты сможешь поподробнее изучить японский язык, " + 
                         "а также узнать некоторые интересные факты о Японии и её культуре")


