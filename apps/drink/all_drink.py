from aiogram import types
from aiogram.dispatcher.filters import Text
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from apps.db.function_db import info_drink

from config import dp, bot


@dp.message_handler(Text(equals='🍹 Напиток'))
async def all_drink(message: types.Message):
    data_drink = info_drink()
    for i in data_drink:
        await bot.send_photo(message.from_user.id, i[1],  f'Название: {i[2]}\nОписание: {i[3]}\nЦена: {i[4]} сом')
        await bot.send_message(message.from_user.id, text='^^^^^', reply_markup=InlineKeyboardMarkup().\
                               add(InlineKeyboardButton(f'Добавить корзину {i[2]}', callback_data=f'add {i[2]} {i[4]}')))