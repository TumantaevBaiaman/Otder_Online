from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher

TOKEN = "token bot"

ip = "localhost"
user = "username"
password = "password"
db_name = "db_name"

sender_email = "email to send message"
password_email = "password email"


storage = MemoryStorage()
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)