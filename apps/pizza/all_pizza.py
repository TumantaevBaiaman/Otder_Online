from aiogram import types
from aiogram.dispatcher.filters import Text
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from apps.db.function_db import info_pizza

from config import dp, bot


@dp.message_handler(Text(equals='🍕 Пицца'))
async def all_pizza(message: types.Message):
    data_pizza = info_pizza()
    for i in data_pizza:
        await bot.send_photo(message.from_user.id, i[1],  f'Название: {i[2]}\nОписание: {i[3]}\nЦена: {i[4]} сом')
        await bot.send_message(message.from_user.id, text='^^^^^', reply_markup=InlineKeyboardMarkup().\
                               add(InlineKeyboardButton(f'Добавить корзину {i[2]}', callback_data=f'add {i[2]} {i[4]}')))