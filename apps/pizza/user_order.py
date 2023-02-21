import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from aiogram import types
from aiogram.dispatcher.filters import Text
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from apps.db.function_db import basket_pizza, info_basket, delete_data_in_basket, order_pizza, info_order, info_email
from config import dp, bot, sender_email, password_email


@dp.message_handler(Text(equals='✅ Заказать'))
async def order(message: types.Message):
    data_basket = info_basket(message.from_user.id)
    data = {
        'id_user': message.from_user.id,
        'product': '',
        'payment': 0
    }
    for i in data_basket:
        data['product'] += i[2]+' '+str(i[3])+'сом'+'\n'
        data['payment'] += i[3]
        delete_data_in_basket(i[0])
    order_pizza(data)
    await bot.send_message(message.from_user.id, text=f'Ваш чек:\n{data["product"]}\nЦена: {data["payment"]} сом')


@dp.message_handler(Text(equals='📜 История'))
async def all_order(message: types.Message):
    data_order = info_order(message.from_user.id)
    for i in data_order:
        await bot.send_message(message.from_user.id, text=f'Ваши заказы:\n{i[2]}\nЦена: {i[3]} сом\nДата заказа: {i[4]}\n')


@dp.message_handler(Text(equals='📧 Обший'))
async def email1(message: types.Message):
    data_order = info_order(message.from_user.id)
    data_email = info_email(message.from_user.id)
    text = ''
    sum = 0
    for i in data_order:
        text += str(i[4])+' '+str(i[3])+'\n'
        sum+=i[3]
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    text += str(sum)

    try:
        server.login(sender_email, password_email)
        msg = str(text)

        server.sendmail(sender_email, data_email[0], msg)
        await bot.send_message(message.from_user.id, text="Ваш gmail был отправлен отчет")

    except Exception as _ex:
        pass


@dp.message_handler(Text(equals='📧 Детально'))
async def email2(message: types.Message):
    data_order = info_order(message.from_user.id)
    data_email = info_email(message.from_user.id)
    text = ''
    sum = 0
    msg = MIMEMultipart()

    for i in data_order:
        text += str(i[2])

    with open("one.text", 'w') as f:
        f.write(str(text))
    with open("one.text") as f:
        file = MIMEText(f.read())
    file.add_header('content-disposition', 'attachment', filename='one.text')
    msg.attach(file)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    print(text)
    try:
        server.login(sender_email, password_email)

        server.sendmail(sender_email, data_email[0], msg.as_string())
        await bot.send_message(message.from_user.id, text="Ваш gmail был отправлен отчет")

    except Exception as _ex:
        pass
