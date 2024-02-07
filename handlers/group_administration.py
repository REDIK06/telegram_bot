from aiogram import Router, F, types
from aiogram.filters import Command
from datetime import timedelta

group_administration_router = Router()

BAD_WORDS = ("бестолковый", "тупой", "глупый")


@group_administration_router.message(Command("ban", prefix="/!"))
@group_administration_router.message(F.chat.type == "group")
async def ban_user(message: types.Message):
    print("Text:", message.text)
    admins = await message.chat.get_administrators()
    is_admin = message.reply_to_message.from_user.id in [admin.user.id for admin in admins]

    if message.reply_to_message:
        if not is_admin:
            await message.bot.ban_chat_member(
                chat_id=message.chat.id,
                user_id=message.reply_to_message.from_user.id,
                until_date=timedelta(20)
            )
            await message.answer(f"Был забанен @{message.reply_to_message.from_user.username}")


@group_administration_router.message((F.chat.type == "supergroup") & (F.text))
async def catch_bad_words(message: types.Message):
    print("Chat type", message.chat.type)
    for word in BAD_WORDS:
        if word in message.text:
            admins = await message.chat.get_administrators()
            is_admin = message.from_user.id in [admin.user.id for admin in admins]
            if not is_admin:
                await message.answer(f"Прошу вас избежать грубых или нецензурных слов! \n"
                                     f"@{message.from_user.username} использовал(а) запрещенное слово.")
                await message.bot.ban_chat_member(
                    chat_id=message.chat.id,
                    user_id=message.from_user.id,
                    until_date=timedelta(seconds=20)
                )
                break
            else:
                await message.answer(f"Уважаемый админ, не стоит использовать нецензурные слова. "
                                     f"Пожалуйста, будьте внимательны.")
                break

