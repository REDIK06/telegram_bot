from aiogram import Router, F, types
from aiogram.filters import Command
from db.queries import get_movies_by_genre



kinopoisk_router = Router()


@kinopoisk_router.message(Command("kinopoisk"))
async def show_kinopoisk(message: types.Message):
    # keyboard
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="фильм/треллер/экшентриллер"),
                types.KeyboardButton(text="чёрная комедия/научная фантастика"),
            ],
            [
                types.KeyboardButton(text="фантастика/фильм ужасов/драма"),
                types.KeyboardButton(text="мистерия"),
            ],
            [
                types.KeyboardButton(text="боевик/триллер"),
                types.KeyboardButton(text="научная фантастика/боевик/комедия"),
            ],
            [
                types.KeyboardButton(text="боевик/триллер/криминал"),
                types.KeyboardButton(text="драма/мелодрама")
            ],
            [
                types.KeyboardButton(text="триллер/драма"),
                types.KeyboardButton(text="драма/биография"),
            ]

        ],
        resize_keyboard=True
    )
    await message.answer("Top-10 фильмов:", reply_markup=kb)


@kinopoisk_router.message(F.text.lower() == "фильм/треллер/экшентриллер")
async def about_top1(message: types.Message):
    movies = get_movies_by_genre(1)
    kb = types.ReplyKeyboardRemove()
    for movie in movies:
        await message.answer(f'Название:{movie[1]}\n'
                             f'Жанр:{movie[2]}\n'
                             f'Время просмотра: {movie[3]}\n'
                             f'Дата выхода:{movie[4]}', reply_markup=kb)
    # await message.answer("1-Красное уведомление(2021)\n"
    #                      "ЖАНPЫ:\n"
    #                      "фильм-треллер,\n"
    #                      "экшентриллер \n"
    #                      "комедийный фильм", reply_markup=kb)


@kinopoisk_router.message(F.text.lower() == "чёрная комедия/научная фантастика")
async def about_top2(message: types.Message):
    movies = get_movies_by_genre(2)
    kb = types.ReplyKeyboardRemove()
    for movie in movies:
        await message.answer(f'Название:{movie[1]}\n'
                             f'Жанр:{movie[2]}\n'
                             f'Время просмотра: {movie[3]}\n'
                             f'Дата выхода:{movie[4]}', reply_markup=kb)
    # await message.answer("2-Не смотри вверх(2021)\n"
    #                      "ЖАНPЫ:\n"
    #                      "чёрная комедия\n"
    #                      "научная фантастика\n"
    #                      "фильм-катастрофа\n"
    #                      "политическая сатира", reply_markup=kb)


@kinopoisk_router.message(F.text.lower() == "фантастика/фильм ужасов/драма")
async def about_top3(message: types.Message):
    movies = get_movies_by_genre(3)
    kb = types.ReplyKeyboardRemove()
    for movie in movies:
        await message.answer(f'Название:{movie[1]}\n'
                             f'Жанр:{movie[2]}\n'
                             f'Время просмотра: {movie[3]}\n'
                             f'Дата выхода:{movie[4]}', reply_markup=kb)
    # await message.answer("3-Птичий короб(2018)\n"
    #                      "ЖАНPЫ:\n"
    #                      "фантастика\n"
    #                      "фильм ужасов\n"
    #                      "драма", reply_markup=kb)


@kinopoisk_router.message(F.text.lower() == "мистерия")
async def about_top4(message: types.Message):
    movies = get_movies_by_genre(4)
    kb = types.ReplyKeyboardRemove()
    for movie in movies:
        await message.answer(f'Название:{movie[1]}\n'
                             f'Жанр:{movie[2]}\n'
                             f'Время просмотра: {movie[3]}\n'
                             f'Дата выхода:{movie[4]}', reply_markup=kb)
    # await message.answer("4-Достать ножи: Стеклянная луковица(2022)\n"
    #                      "ЖАНР:\n"
    #                      "мистерия", reply_markup=kb)


@kinopoisk_router.message(F.text.lower() == "боевик/триллер")
async def about_top5(message: types.Message):
    movies = get_movies_by_genre(5)
    kb = types.ReplyKeyboardRemove()
    for movie in movies:
        await message.answer(f'Название:{movie[1]}\n'
                             f'Жанр:{movie[2]}\n'
                             f'Время просмотра: {movie[3]}\n'
                             f'Дата выхода:{movie[4]}', reply_markup=kb)
    # await message.answer("5-Серый человек(2022)\n"
    #                      "ЖАНPЫ:\n"
    #                      "боевик\n"
    #                      "триллер", reply_markup=kb)


@kinopoisk_router.message(F.text.lower() == "научная фантастика/боевик/комедия")
async def about_top6(message: types.Message):
    movies = get_movies_by_genre(6)
    kb = types.ReplyKeyboardRemove()
    for movie in movies:
        await message.answer(f'Название:{movie[1]}\n'
                             f'Жанр:{movie[2]}\n'
                             f'Время просмотра: {movie[3]}\n'
                             f'Дата выхода:{movie[4]}', reply_markup=kb)
    # await message.answer("6-Проект 'Адам'(2022)\n"
    #                      "ЖАНPЫ:\n"
    #                      "научная фантастика\n"
    #                      "боевик\n"
    #                      "комедия", reply_markup=kb)


@kinopoisk_router.message(F.text.lower() == "боевик/триллер/криминал")
async def about_top7(message: types.Message):
    movies = get_movies_by_genre(7)
    kb = types.ReplyKeyboardRemove()
    for movie in movies:
        await message.answer(f'Название:{movie[1]}\n'
                             f'Жанр:{movie[2]}\n'
                             f'Время просмотра: {movie[3]}\n'
                             f'Дата выхода:{movie[4]}', reply_markup=kb)
    # await message.answer("7-Тайлер Рейк: Операция по спасению(2020)\n"
    #                      "ЖАНPЫ:\n"
    #                      "боевик\n"
    #                      "триллер\n"
    #                      "криминал", reply_markup=kb)


@kinopoisk_router.message(F.text.lower() == "драма/мелодрама")
async def about_top8(message: types.Message):
    movies = get_movies_by_genre(8)
    kb = types.ReplyKeyboardRemove()
    for movie in movies:
        await message.answer(f'Название:{movie[1]}\n'
                         f'Жанр:{movie[2]}\n'
                         f'Время просмотра: {movie[3]}\n'
                         f'Дата выхода:{movie[4]}', reply_markup=kb)
    # await message.answer("8-Пурпурные сердца(2022)\n"
    #                      "ЖАНPЫ:\n"
    #                      "драма\n"
    #                      "мелодрама", reply_markup=kb)


@kinopoisk_router.message(F.text.lower() == "триллер/драма")
async def about_top9(message: types.Message):
    movies = get_movies_by_genre(9)
    kb = types.ReplyKeyboardRemove()
    for movie in movies:
        await message.answer(f'Название:{movie[1]}\n'
                             f'Жанр:{movie[2]}\n'
                             f'Время просмотра: {movie[3]}\n'
                             f'Дата выхода:{movie[4]}', reply_markup=kb)
    # await message.answer("9-Непрощённая(2021)\n"
    #                      "ЖАНPЫ:\n"
    #                      "триллер\n"
    #                      "драма", reply_markup=kb)


@kinopoisk_router.message(F.text.lower() == "драма/биография")
async def about_top10(message: types.Message):
    movies = get_movies_by_genre(10)
    kb = types.ReplyKeyboardRemove()
    for movie in movies:
        await message.answer(f'Название:{movie[1]}\n'
                             f'Жанр:{movie[2]}\n'
                             f'Время просмотра: {movie[3]}\n'
                             f'Дата выхода:{movie[4]}', reply_markup=kb)
    # await message.answer("10-Ирландец(2019)\n"
    #                      "ЖАНPЫ:\n"
    #                      "драма\n"
    #                      "биография", reply_markup=kb)




