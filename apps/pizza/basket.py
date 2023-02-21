from aiogram import types
from aiogram.dispatcher.filters import Text
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from apps.db.function_db import basket_pizza, info_basket, delete_data_in_basket
from config import dp, bot


@dp.callback_query_handler(Text(startswith='add '))
async def basket(call: types.CallbackQuery):
    # await sql_data.sql_del(call.data.replace('add ',''))
    data = call.data.replace("add ","").split(' ')
    data_basket = {
        'id_user': call.from_user.id,
        'product': data[0],
        'payment': data[-1]
    }
    basket_pizza(data_basket)
    await call.answer(text=f'{call.data.replace("add ","")} добавление', show_alert=True)


@dp.callback_query_handler(Text(startswith='dell '))
async def basket(call: types.CallbackQuery):
    delete_data_in_basket(call.data.replace('dell ',''))
    await call.answer(text=f'Убран из корзины', show_alert=True)


@dp.message_handler(Text(equals='⭐ Корзина'))
async def all_basket(message: types.Message):
    data_basket = info_basket(message.from_user.id)
    for i in data_basket:
        await bot.send_message(message.from_user.id, text=f'Название: {i[2]}\nЦена: {i[3]} сом')
        await bot.send_message(message.from_user.id, text='^^^^^', reply_markup=InlineKeyboardMarkup().\
                               add(InlineKeyboardButton(f'Убрать из корзины {i[2]}', callback_data=f'dell {i[0]}')))