from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher
from aiogram.utils import executor
from aiogram import types

from config import dp, bot


import apps.commands.base
import apps.pizza.add_pizza
import apps.pizza.all_pizza
import apps.pizza.basket
import apps.pizza.user_order
import apps.drink.add_drink
import apps.drink.all_drink
import apps.film.all_film
import apps.account.register



if __name__ == '__main__':
    executor.start_polling(dp)