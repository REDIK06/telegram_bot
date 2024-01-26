from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

movie_survey_router = Router()


class MoviePoll(StatesGroup):
    name = State()
    whats_your_gender = State()
    age = State()
    movie_genre = State()
    movie_frequency = State()
    favorite_movie = State()
    recommended_movie = State()


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


@movie_survey_router.message(Command("survey"))
async def start_survey(message: types.Message, state: FSMContext):
    await state.set_state(MoviePoll.whats_your_gender)
    await message.answer("Приступим к проведению опроса! Можете остановить опрос командой /cancel")
    await message.answer("Как Вас зовут?")


@movie_survey_router.message(Command("cancel"))
@movie_survey_router.message(F.text.lower() == "отмена")
async def cancel_registration(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer("Проведение опроса приостановлено")


@movie_survey_router.message(MoviePoll.whats_your_gender)
async def process_whats_your_gender(message: types.Message, state: FSMContext):
    await state.update_data(whats_your_gender=message.text)
    await state.set_state(MoviePoll.name)
    await message.answer("ваш пол(мужской/женский)", reply_markup=gender_kb())


@movie_survey_router.message(MoviePoll.name)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(MoviePoll.age)
    await message.answer("Сколько Вам лет?")


@movie_survey_router.message(MoviePoll.age)
async def process_age(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("Возраст должен быть числом")
    elif not 12 <= int(message.text) <= 90:
        await message.answer("Возраст должен быть от 12 до 90 лет")
    else:
        age = int(message.text)
        await state.update_data(age=age)
        await state.set_state(MoviePoll.movie_genre)
        await message.answer("Выберите ваш любимый жанр фильма", reply_markup=genre_kb())


@movie_survey_router.message(MoviePoll.movie_genre)
async def process_movie_genre(message: types.Message, state: FSMContext):
    await state.update_data(movie_genre=message.text)
    await state.set_state(MoviePoll.movie_frequency)
    await message.answer("Как часто смотрите фильмы?", reply_markup=time_kb())


@movie_survey_router.message(MoviePoll.movie_frequency)
async def process_movie_frequency(message: types.Message, state: FSMContext):
    await state.set_state(MoviePoll.favorite_movie)
    await message.answer("Ваш любимый фильм")


@movie_survey_router.message(MoviePoll.favorite_movie)
async def process_favorite_movie(message: types.Message, state: FSMContext):
    if not message.text.isalpha():
        await message.answer("Пожалуйста, введите только буквы, а не числа.")
    else:
        await state.update_data(favorite_movie=message.text)
        await state.set_state(MoviePoll.recommended_movie)
        await message.answer("Какой фильм вы порекомендуете?")


@movie_survey_router.message(MoviePoll.recommended_movie)
async def process_recommended_movie(message: types.Message, state: FSMContext):
    await state.update_data(recommended_movie=message.text)
    data = await state.get_data()
    await message.answer(f"Ваши данные: {data}")
    await message.answer("Благодарим за пройдённый опрос!")
    await state.clear()
