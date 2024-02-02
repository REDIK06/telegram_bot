from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv
from os import getenv
from apscheduler.schedulers.asyncio import AsyncIOScheduler

load_dotenv()
TOKEN = getenv("BOT_TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher()
scheduler = AsyncIOScheduler()


async def set_commands():
    await bot.set_my_commands([
        types.BotCommand(command="start", description="Старт"),
        types.BotCommand(command="pic", description="Отправить картинку"),
        types.BotCommand(command="kinopoisk", description="Кинопоиск"),
        types.BotCommand(command="survey", description="Опрос о фильмах"),
        types.BotCommand(command="parse", description="Страница парситься"),
    ])
