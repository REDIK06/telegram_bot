from aiogram import Router, F, types
from aiogram.filters import Command

kinopoisk_router = Router()


@kinopoisk_router.message(Command("kinopoisk"))
async def show_kinopoisk(message: types.Message):
    # keyboard
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="Top-1"),
                types.KeyboardButton(text="Top-2"),
            ],
            [
                types.KeyboardButton(text="Top-3"),
                types.KeyboardButton(text="Top-4"),
            ],
            [
                types.KeyboardButton(text="Top-5"),
                types.KeyboardButton(text="Top-6"),
            ],
            [
                types.KeyboardButton(text="Top-7"),
                types.KeyboardButton(text="Top-8")
            ],
            [
                types.KeyboardButton(text="Top-9"),
                types.KeyboardButton(text="Top-10"),
            ]
        ],
        resize_keyboard=True
    )
    await message.answer("Top-10 фильмов:", reply_markup=kb)


@kinopoisk_router.message(F.text.lower() == "top-1")
async def about_top1(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    await message.answer("1-Красное уведомление(2021)\n"
                         "ЖАНPЫ:\n"
                         "фильм-треллер,\n"
                         "экшентриллер \n"
                         "комедийный фильм", reply_markup=kb)


@kinopoisk_router.message(F.text.lower() == "top-2")
async def about_top2(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    await message.answer("2-Не смотри вверх(2021)\n"
                         "ЖАНPЫ:\n"
                         "чёрная комедия\n"
                         "научная фантастика\n"
                         "фильм-катастрофа\n"
                         "политическая сатира", reply_markup=kb)


@kinopoisk_router.message(F.text.lower() == "top-3")
async def about_top3(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    await message.answer("3-Птичий короб(2018)\n"
                         "ЖАНPЫ:\n"
                         "фантастика\n"
                         "фильм ужасов\n"
                         "драма", reply_markup=kb)


@kinopoisk_router.message(F.text.lower() == "top-4")
async def about_top4(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    await message.answer("4-Достать ножи: Стеклянная луковица(2022)\n"
                         "ЖАНР:\n"
                         "мистерия", reply_markup=kb)


@kinopoisk_router.message(F.text.lower() == "top-5")
async def about_top5(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    await message.answer("5-Серый человек(2022)\n"
                         "ЖАНPЫ:\n"
                         "боевик\n"
                         "триллер", reply_markup=kb)


@kinopoisk_router.message(F.text.lower() == "top-6")
async def about_top6(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    await message.answer("6-Проект 'Адам'(2022)\n"
                         "ЖАНPЫ:\n"
                         "научная фантастика\n"
                         "боевик\n"
                         "комедия", reply_markup=kb)


@kinopoisk_router.message(F.text.lower() == "top-7")
async def about_top7(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    await message.answer("7-Тайлер Рейк: Операция по спасению(2020)\n"
                         "ЖАНPЫ:\n"
                         "боевик\n"
                         "триллер\n"
                         "криминал", reply_markup=kb)


@kinopoisk_router.message(F.text.lower() == "top-8")
async def about_top8(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    await message.answer("8-Пурпурные сердца(2022)\n"
                         "ЖАНPЫ:\n"
                         "драма\n"
                         "мелодрама", reply_markup=kb)


@kinopoisk_router.message(F.text.lower() == "top-9")
async def about_top9(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    await message.answer("9-Непрощённая(2021)\n"
                         "ЖАНPЫ:\n"
                         "триллер\n"
                         "драма", reply_markup=kb)


@kinopoisk_router.message(F.text.lower() == "top-10")
async def about_top10(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    await message.answer("10-Ирландец(2019)\n"
                         "ЖАНPЫ:\n"
                         "драма\n"
                         "биография", reply_markup=kb)