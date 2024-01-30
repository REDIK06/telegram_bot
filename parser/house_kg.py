import httpx
from parsel import Selector
from pprint import pprint
from aiogram import Router, F, types
from aiogram.filters import Command

parse_router = Router()
MAIN_URL = "https://www.house.kg/snyat"
ORIGINAL_URL = "https://www.house.kg/snyat"


def get_page():
    response = httpx.get(MAIN_URL)
    html = Selector(text=response.text)
    return html


def get_title(html: Selector):
    title = html.css("title::text").get()
    print(title)


def get_houses_data(html: Selector):
    houses_links = html.css("div.listing a::attr(href)").getall()
    houses = list(map(lambda house: f"{ORIGINAL_URL}{house}", houses_links))
    pprint(houses[:3])
    return houses


def get_house():
    html = get_page()
    return get_houses_data(html)


@parse_router.message(Command("parse"))
async def house(message: types.Message):
    objects = get_house()
    for i in objects:
        await message.answer(i)
