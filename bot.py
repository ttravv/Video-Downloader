import logging
import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from dotenv import dotenv_values
from utils.logic import get_direct_link
from utils.keyboard import start_keyboard
from aiogram import html

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
config = dotenv_values(".env")
bot = Bot(token=config["BOT"])
dp = Dispatcher(bot=bot)


@dp.message(Command("start"))
async def start_button(message: types.Message):
    kb = start_keyboard()
    await message.answer("Выберите команду", reply_markup=kb)


@dp.message(F.text.contains("Скачать видео из YouTube"))
async def answer_handler(message: types.Message):
    await message.answer("Пришлите ссылку")


@dp.message(F.text.regexp(r"^https:\/\/(www\.youtube.*|youtu\.be.*|youtube\.com.*)"))
async def youtube_handler(message: types.Message):
    url = str(message.text)
    direct_link = get_direct_link(url)
    text = html.link("Вот лови", html.quote(direct_link))
    await message.answer(text, parse_mode="HTML")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
