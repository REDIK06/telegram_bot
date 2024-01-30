from aiogram import types


def genre_kb():
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="Фантастика"),
                types.KeyboardButton(text="Драма")
            ],
            [
                types.KeyboardButton(text="Комедия"),
                types.KeyboardButton(text="Боевик")
            ],
        ]
    )
    return kb


def time_kb():
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="Часто"),
                types.KeyboardButton(text="Не часто")
            ],
            [
                types.KeyboardButton(text="Периодически"),
                types.KeyboardButton(text="Регулярно")
            ],
        ]
    )
    return kb


def gender_kb():
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="Мужской"),
            ],
            [
                types.KeyboardButton(text="Женский"),
            ],
        ]
    )
    return kb
