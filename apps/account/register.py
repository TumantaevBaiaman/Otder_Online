import asyncio
import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from aiogram import types
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import StatesGroup, State

from apps import validation
from apps.commands.base import vip_menu, menu_key
from apps.db import function_db
from apps.message import text_error, text_ok

from config import dp, bot, sender_email, password_email


class StateRegister(StatesGroup):

    name_state = State()
    email_state = State()
    phone_state = State()
    data = State()
    validation  = State()


@dp.message_handler(Text(equals='🚀 Account 🚀'))
async def register(message: types.Message, state: StateRegister):
    id_user = message.from_user.id
    if int(id_user) in function_db.all_user():
        await bot.send_message(message.from_user.id, "Welcome 🚀 VIP 🚀 Account", reply_markup=vip_menu)
        state.finish()
    else:
        await bot.send_message(message.from_user.id, "Ваш Фамилия и Имя")
        await StateRegister.name_state.set()


@dp.message_handler(state=StateRegister.name_state)
async def username(message: types.Message, state: StateRegister):
    name = message.text

    if validation.validate_text(name)==False:
        await StateRegister.name_state.set()
        await bot.send_message(message.from_user.id, text_error['name'])

    elif validation.validate_text(name)==True:
        async with state.proxy() as data:
            data['name_state'] = message.text
        await StateRegister.next()
        await bot.send_message(message.from_user.id, text_ok['email'])


@dp.message_handler(state=StateRegister.email_state)
async def gmail(message: types.Message, state: StateRegister):
    email = message.text

    if validation.validate_email(email)==False:
        await StateRegister.name_state.set()
        await bot.send_message(message.from_user.id, "Ошибка попробуйте занова")

    elif validation.validate_email(email)==True:
        async with state.proxy() as data:
            data['email_state'] = message.text
        await StateRegister.phone_state.set()
        await bot.send_message(message.from_user.id, text_ok['phone'])


@dp.message_handler(state=StateRegister.phone_state)
async def phone(message: types.Message, state: StateRegister):
    phone = message.text

    if validation.validate_phone(phone)==False:
        await StateRegister.phone_state.set()
        await bot.send_message(message.from_user.id, text_error['phone'])

    else:

        code = random.randint(1000, 10000)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()

        async with state.proxy() as data:
            try:
                server.login(sender_email, password_email)
                msg = str(code)

                server.sendmail(sender_email, data['email_state'], msg)
                print('ok')
            except Exception as _ex:
                pass

        async with state.proxy() as data:
            data['phone_state'] = message.text
            data['data'] = str(code)
            await StateRegister.validation.set()
            await bot.send_message(message.from_user.id, "Промотрите ваш @gmail аккаунт\nВам должен отправиться код для подверждению\nВы должны поставит этот код здес")


@dp.message_handler(state=StateRegister.validation)
async def process_phone_command(message: types.Message, state: StateRegister):
    code = str(message.text)
    async with state.proxy() as data:
        if data['data'] == code:
            info = {
                'id_user': message.from_user.id,
                'username': data['name_state'],
                'email': data['email_state'],
                'phone': data['phone_state']
            }
            function_db.add_user(info)
            await bot.send_message(message.from_user.id, "Вам подключен 🚀 VIP 🚀 аккаунт на месяц\nПосле этого вам стоит платить месяц 10$ что бы пользоваться этим функциям", reply_markup=vip_menu)
            await state.finish()
        elif code=='отмена':
            await bot.send_message(message.from_user.id, 'Был отмена регистрации',reply_markup=menu_key)
            await state.finish()
        else:
            await StateRegister.validation.set()
            await bot.send_message(message.from_user.id, "Ошибка попробуйте еще раз")