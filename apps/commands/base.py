from aiogram import types
from aiogram.dispatcher.filters import Text
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from config import dp, bot

home = KeyboardButton('🍱 На главную меню')

pizza = KeyboardButton('🍕 Пицца')
drink = KeyboardButton('🍹 Напиток')
order = KeyboardButton('📜 История')
basket = KeyboardButton('⭐ Корзина')

buy = KeyboardButton('✅ Заказать')

home_menu = KeyboardButton('🍟 Меню')
order_menu = KeyboardButton('🥝 Заказы')

film = KeyboardButton('🎬 Смотреть')
email_my = KeyboardButton('📧 Отчет')

vip = KeyboardButton('🚀 Account 🚀')

admin_pizza = KeyboardButton('🍕 Добавить')
admin_drink = KeyboardButton('🍹 Добавить')

email_detail_mini = KeyboardButton('📧 Обший')
email_detail = KeyboardButton('📧 Детально')

anime = KeyboardButton('🏝 Аниме')
comedy = KeyboardButton('🌄 Комедиа')
mult = KeyboardButton('🏔 Мультфилим')
sport = KeyboardButton('🏕 Спорт')
font = KeyboardButton('🌄 Фантастика')
history = KeyboardButton('🏞 История')

menu_film = ReplyKeyboardMarkup(resize_keyboard=True).add(anime, history, font).add(sport, comedy, mult).add(vip)
menu_email = ReplyKeyboardMarkup(resize_keyboard=True).add(email_detail_mini, email_detail).add(vip)

admin_menu = ReplyKeyboardMarkup(resize_keyboard=True).add(admin_pizza, admin_drink).add(home)
vip_menu = ReplyKeyboardMarkup(resize_keyboard=True).add(film, email_my).add(home)

menu_key = ReplyKeyboardMarkup(resize_keyboard=True).add(home_menu, order_menu).add(vip)
menu_product = ReplyKeyboardMarkup(resize_keyboard=True).add(pizza, drink).add(home)
menu_history = ReplyKeyboardMarkup(resize_keyboard=True).add(order, basket, buy).add(home)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await bot.send_message(message.from_user.id, f"Добро пожаловать {message.from_user.username}", reply_markup=menu_key)


@dp.message_handler(Text(equals='🍱 На главную меню'))
async def home(message: types.Message):
    await bot.send_message(message.from_user.id, f"Главная меню",reply_markup=menu_key)


@dp.message_handler(Text(equals='🍟 Меню'))
async def product(message: types.Message):
    await bot.send_message(message.from_user.id, f"Что вы хотите",reply_markup=menu_product)


@dp.message_handler(Text(equals='🥝 Заказы'))
async def order(message: types.Message):
    await bot.send_message(message.from_user.id, f"Главная меню",reply_markup=menu_history)


@dp.message_handler(commands=['admin'])
async def order(message: types. Message):
    user_id = message.from_user.id
    if user_id == 5004318545:
        await bot.send_message(message.from_user.id, f"🌐Что вы хотите", reply_markup=admin_menu)
    else:
        await bot.send_message(message.from_user.id, f"📛Вы не админ")


@dp.message_handler(Text(equals='📧 Отчет'))
async def email(message: types.Message):
    await bot.send_message(message.from_user.id, f"Выберите",reply_markup=menu_email)


@dp.message_handler(Text(equals='🎬 Смотреть'))
async def film_all(message: types.Message):
    await bot.send_message(message.from_user.id, f"Выберите",reply_markup=menu_film)
