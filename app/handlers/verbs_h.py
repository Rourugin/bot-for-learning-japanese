from typing import Any
from aiogram import Router, F
from aiogram.types import Message

from app.database import requests as rq


verbs_r = Router()


@verbs_r.message()
async def verb(message: Message) -> Any:
    word_num = None
    words_count = await rq.count_words()
    text = ""
    words = await rq.get_all_words()
    for i in range(0, words_count):
        if (message.text.lower() == words[i]['word']) or (message.text.lower() == words[i]['pronouns']) or (message.text.lower() == words[i]['translate']):
            word_num = i
    if word_num == None:
        text = "К сожалению, этого слова нет в нашем словаре:(\nНо мы обязательно это исправим!"
    elif word_num != None:
        text += words[word_num]['word']
        text += " - "
        text += words[word_num]['translate']
        text += "\n"
        text += words[word_num]['conjugation']
        text += "\nПервая основа: "
        text += words[word_num]['frForm']
        text += "\nВторая основа: "
        text += words[word_num]['scForm']
        text += "\nТретья основа: "
        text += words[word_num]['thForm']
        text += "\nФорма на て: "
        text += words[word_num]['teForm']
        text += "\nФорма на た: "
        text += words[word_num]['taForm']
    await message.answer(text)
