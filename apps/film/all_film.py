import bs4
import requests
from aiogram import types
from aiogram.dispatcher.filters import Text
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from apps.db.function_db import info_pizza

from config import dp, bot
from apps.film.parser import TopCinema


@dp.message_handler(Text(equals='🏝 Аниме'))
async def all_film_data(message: types.Message):
    s = []
    data = TopCinema()
    for i in data.top():
        film = i.find('a')
        s.append(str('https://me.anwap.tube' + film['href']))
    data_film = s[:5]
    for i in data_film:
        await bot.send_message(message.from_user.id, str(i))


@dp.message_handler(Text(equals='🌄 Комедиа'))
async def all_film_data(message: types.Message):
    url = 'https://me.anwap.tube/films/r14'
    page = requests.get(url)
    soup = bs4.BeautifulSoup(page.text, 'html.parser')
    data = soup.find_all('div', class_='my_razdel film')
    s = []
    for i in data:
        film = i.find('a')
        s.append(str('https://me.anwap.tube' + film['href']))
    data_film = s[:5]
    for i in data_film:
        await bot.send_message(message.from_user.id, str(i))


@dp.message_handler(Text(equals='🏔 Мультфилим'))
async def all_film_data(message: types.Message):
    url = 'https://me.anwap.tube/films/r22'
    page = requests.get(url)
    soup = bs4.BeautifulSoup(page.text, 'html.parser')
    data = soup.find_all('div', class_='my_razdel film')
    s = []
    for i in data:
        film = i.find('a')
        s.append(str('https://me.anwap.tube' + film['href']))
    data_film = s[:5]
    for i in data_film:
        await bot.send_message(message.from_user.id, str(i))


@dp.message_handler(Text(equals='🏕 Спорт'))
async def all_film_data(message: types.Message):
    url = 'https://me.anwap.tube/films/r28'
    page = requests.get(url)
    soup = bs4.BeautifulSoup(page.text, 'html.parser')
    data = soup.find_all('div', class_='my_razdel film')
    s = []
    for i in data:
        film = i.find('a')
        s.append(str('https://me.anwap.tube' + film['href']))
    data_film = s[:5]
    for i in data_film:
        await bot.send_message(message.from_user.id, str(i))


@dp.message_handler(Text(equals='🌄 Фантастика'))
async def all_film_data(message: types.Message):
    url = 'https://me.anwap.tube/films/r31'
    page = requests.get(url)
    soup = bs4.BeautifulSoup(page.text, 'html.parser')
    data = soup.find_all('div', class_='my_razdel film')
    s = []
    for i in data:
        film = i.find('a')
        s.append(str('https://me.anwap.tube' + film['href']))
    data_film = s[:5]
    for i in data_film:
        await bot.send_message(message.from_user.id, str(i))


@dp.message_handler(Text(equals='🏞 История'))
async def all_film_data(message: types.Message):
    url = 'https://me.anwap.tube/films/r12'
    page = requests.get(url)
    soup = bs4.BeautifulSoup(page.text, 'html.parser')
    data = soup.find_all('div', class_='my_razdel film')
    s = []
    for i in data:
        film = i.find('a')
        s.append(str('https://me.anwap.tube' + film['href']))
    data_film = s[:5]
    for i in data_film:
        await bot.send_message(message.from_user.id, str(i))