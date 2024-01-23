import asyncio
import logging
from bot import bot, dp, set_commands
from handlers import (
    start_router,
    pictures_router,
    kinopoisk_router,
    movie_survey_router
)
from db.queries import init_db, create_tables, populate_db


async def on_startup(dispatcher):
    print('Бот вышел в онлайн')
    init_db()
    create_tables()
    populate_db()


async def main():
    await set_commands()
    dp.include_router(start_router)
    dp.include_router(pictures_router)
    dp.include_router(kinopoisk_router)
    dp.include_router(movie_survey_router)
    dp.startup.register(on_startup)

    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
