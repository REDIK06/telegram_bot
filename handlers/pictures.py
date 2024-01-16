from aiogram import Router, types
from aiogram.filters import Command
import os
import random

pictures_router = Router()


@pictures_router.message(Command("pic"))
async def random_pic(message: types.Message):
    photo_folder = "images"
    photos = os.listdir(photo_folder)
    photo_name = random.choice(photos)
    photo = types.FSInputFile(os.path.join(photo_folder, photo_name))
    await message.answer_photo(photo=photo, caption="ПРОГРАММИРОВАНИЕ")
