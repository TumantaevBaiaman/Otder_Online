from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import StatesGroup, State
from apps.db.function_db import add_pizza
from config import dp, bot


class StatePizza(StatesGroup):
    img_id = State()
    pizza_name = State()
    description = State()
    payment = State()


@dp.message_handler(Text(equals='🍕 Добавить'), state=None)
async def idea(message: types.Message, state: StatePizza):
    id_user = message.from_user.id
    await bot.send_message(message.from_user.id, "🍕Добавьте картинки пиццы")
    await StatePizza.img_id.set()


@dp.message_handler(state=StatePizza.img_id, content_types=['photo', 'video', 'text'])
async def pizza_img(message: types.Message, state: FSMContext):
    id_user = message.from_user.id
    if message.content_type == 'text' or message.content_type == 'video':
        await bot.send_message(message.from_user.id, "❌Вы добавили что-то другое\n🍕Добавьте картинки пиццы")
        await StatePizza.img_id.set()
    else:
        async with state.proxy() as data:
            data['img_id'] = message.photo[0].file_id
            await bot.send_message(message.from_user.id, "🍕Добавьте название пиццы")
            await StatePizza.pizza_name.set()


@dp.message_handler(state=StatePizza.pizza_name, content_types=['photo', 'video', 'text'])
async def pizza_name(message: types.Message, state: FSMContext):
    id_user = message.from_user.id
    if message.content_type == 'photo' or message.content_type == 'video':
        await bot.send_message(message.from_user.id, "❌Вы добавили что-то другое\n🍕Добавьте название пиццы")
        await StatePizza.img_id.set()
    else:
        async with state.proxy() as data:
            data['pizza_name'] = message.text
            await bot.send_message(message.from_user.id, "🍕Добавьте описание пиццы")
            await StatePizza.description.set()


@dp.message_handler(state=StatePizza.description, content_types=['photo', 'video', 'text'])
async def pizza_description(message: types.Message, state: FSMContext):
    id_user = message.from_user.id
    if message.content_type == 'photo' or message.content_type == 'video':
        await bot.send_message(message.from_user.id, "❌Вы добавили что-то другое\n🍕Добавьте описание пиццы")
        await StatePizza.img_id.set()
    else:
        async with state.proxy() as data:
            data['description'] = message.text
            await bot.send_message(message.from_user.id, "🍕Добавте цены пиццы")
            await StatePizza.payment.set()


@dp.message_handler(state=StatePizza.payment, content_types=['photo', 'video', 'text'])
async def pizza_payment(message: types.Message, state: FSMContext):
    id_user = message.from_user.id
    if message.content_type == 'photo' or message.content_type == 'video':
        await bot.send_message(message.from_user.id, "❌Вы добавили что-то другое\n🍕Добавьте цены пиццы")
        await StatePizza.img_id.set()
    else:
        async with state.proxy() as data:
            data['payment'] = message.text
            data_pizza = {
                'img_id': data['img_id'],
                'pizza_name': data['pizza_name'],
                'description': data['description'],
                'payment': data['payment']
            }
            add_pizza(data_pizza)
            await bot.send_message(message.from_user.id, "✔🍕Пицца добавлен")
            await state.finish()



