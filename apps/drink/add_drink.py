from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import StatesGroup, State
from apps.db.function_db import add_drink
from config import dp, bot


class StateDrink(StatesGroup):
    img_id = State()
    drink_name = State()
    description = State()
    payment = State()


@dp.message_handler(Text(equals='🍹 Добавить'), state=None)
async def drink(message: types.Message, state: StateDrink):
    id_user = message.from_user.id
    await bot.send_message(message.from_user.id, "🍹Добавьте картинки напитки")
    await StateDrink.img_id.set()


@dp.message_handler(state=StateDrink.img_id, content_types=['photo', 'video', 'text'])
async def drink_img(message: types.Message, state: FSMContext):
    id_user = message.from_user.id
    if message.content_type == 'text' or message.content_type == 'video':
        await bot.send_message(message.from_user.id, "❌Вы добавили что-то другое\n🍹Добавьте картинки напитки")
        await StateDrink.img_id.set()
    else:
        async with state.proxy() as data:
            data['img_id'] = message.photo[0].file_id
            await bot.send_message(message.from_user.id, "🍹Добавьте название напитки")
            await StateDrink.drink_name.set()


@dp.message_handler(state=StateDrink.drink_name, content_types=['photo', 'video', 'text'])
async def drink_name(message: types.Message, state: FSMContext):
    id_user = message.from_user.id
    if message.content_type == 'photo' or message.content_type == 'video':
        await bot.send_message(message.from_user.id, "❌Вы добавили что-то другое\n🍹Добавьте название напитки")
        await StateDrink.img_id.set()
    else:
        async with state.proxy() as data:
            data['drink_name'] = message.text
            await bot.send_message(message.from_user.id, "🍹Добавьте описание напитки")
            await StateDrink.description.set()


@dp.message_handler(state=StateDrink.description, content_types=['photo', 'video', 'text'])
async def drink_description(message: types.Message, state: FSMContext):
    id_user = message.from_user.id
    if message.content_type == 'photo' or message.content_type == 'video':
        await bot.send_message(message.from_user.id, "❌Вы добавили что-то другое\n🍹Добавьте описание напитки")
        await StateDrink.img_id.set()
    else:
        async with state.proxy() as data:
            data['description'] = message.text
            await bot.send_message(message.from_user.id, "🍹Добавте цены напитки")
            await StateDrink.payment.set()


@dp.message_handler(state=StateDrink.payment, content_types=['photo', 'video', 'text'])
async def drink_payment(message: types.Message, state: FSMContext):
    id_user = message.from_user.id
    if message.content_type == 'photo' or message.content_type == 'video':
        await bot.send_message(message.from_user.id, "❌Вы добавили что-то другое\n🍹Добавьте цены напитки")
        await StateDrink.img_id.set()
    else:
        async with state.proxy() as data:
            data['payment'] = message.text
            data_drink = {
                'img_id': data['img_id'],
                'drink_name': data['drink_name'],
                'description': data['description'],
                'payment': data['payment']
            }
            add_drink(data_drink)
            await bot.send_message(message.from_user.id, "✔🍹Напиток добавлен")
            await state.finish()