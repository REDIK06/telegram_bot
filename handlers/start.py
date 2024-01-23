from aiogram import Router, F, types
from aiogram.filters import Command
from pprint import pprint

start_router = Router()


@start_router.message(Command("start"))
async def start(message: types.Message):
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="кинокомпания netflix", url="https://www.netflix.com/")
            ],
            [
                types.InlineKeyboardButton(text="instagram:netflix", url="https://instagram.com/"),
            ],
            [
                types.InlineKeyboardButton(text="О компании netflix", callback_data="about_netflix"),
            ]
        ]
    )

    await message.answer(f"Привет! {message.from_user.full_name}", reply_markup=kb)


@start_router.callback_query(F.data == "about_netflix")
async def about_netflix(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer("Американская развлекательная компания, а также стриминговый сервис фильмов и сериалов.🎥")
