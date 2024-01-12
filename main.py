import os
import random
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import load_dotenv
from os import getenv
import logging
from pprint import pprint
from pathlib import Path


load_dotenv()
TOKEN = getenv("BOT_TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: types.Message):
    pprint(message)
    await message.answer(f"Привет!{message.from_user.full_name}")


@dp.message(Command("myinfo"))
async def myinfo(message: types.Message):
    await message.answer(f"Ваш id:{message.from_user.id}\n "
                         f"Ваше имя: {message.from_user.first_name}\n"
                         f"Ваш никнейм: {message.from_user.username}")


@dp.message(Command("pic"))
async def random_pic(message: types.Message):
    photo_folder = "images"
    photos = os.listdir(photo_folder)
    photo_name = random.choice(photos)
    photo = types.FSInputFile(os.path.join(photo_folder, photo_name))
    await message.answer_photo(photo=photo, caption="ПРОГРАММИРОВАНИЕ")


@dp.message()
async def echo(message: types.Message):
    await message.answer(message.text)


async def main():
    await bot.set_my_commands([
        types.BotCommand(command="start",
                         description="Старт"),
        types.BotCommand(command="myinfo",
                         description="Ваши данные"),
        types.BotCommand(command="pic",
                         description="Картинки программирование"),
    ])
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())