import os
import re
from aiogram import  Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
from aiogram.dispatcher.filters.state import State, StatesGroup
class UserState(StatesGroup):
    age = State()
    growth = State()
    weight  = State()

bot = Bot(token=key_bot_api)
disp = Dispatcher(bot, storage=MemoryStorage())

@disp.message_handler(text = 'Calories')
async def set_age(message):
    await message.answer('Введите свой возраст:')
    await UserState.age.set()

with open('conf_both.cnf', 'r') as cnf:
    ctxt = cnf.read()
    po = re.search('(?<=' + 'bot_kye=' + ').*?(?=\n)', ctxt)
    key_bot_api = po.group(0)
    # print(key_bot)
@disp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.')
@disp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age = message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()
@disp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth = message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()

@disp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    colory = 10 х data['weight'] + 6,25 x data['growth'] - 5 х data['age'] + 5
    await message.answer(colory)
    await state.finish()
@disp.message_handler()
async def all_massages(message):
    await message.answer('Введите команду /start, чтобы начать общение.')

if __name__=='__main__':
    executor.start_polling(disp,skip_updates=True)


