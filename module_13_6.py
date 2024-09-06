import os
import re
from aiogram import  Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import  ReplyKeyboardMarkup,KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight  = State()

with open('conf_both.cnf', 'r') as cnf:
    ctxt = cnf.read()
    po = re.search('(?<=' + 'bot_kye=' + ').*?(?=\n)', ctxt)
    key_bot_api = po.group(0)
    # print(key_bot)

bot = Bot(token=key_bot_api)
disp = Dispatcher(bot, storage=MemoryStorage())
keybr = ReplyKeyboardMarkup(resize_keyboard=True)
butt_inf = KeyboardButton(text='Информация')
butt_sc = KeyboardButton(text='Рассчитать')
keybr.add(butt_inf)
keybr.add(butt_sc)

ikeybrt = InlineKeyboardMarkup()
butt_1 = InlineKeyboardButton(text='Рассчитать норму калорий' , callback_data='calories')
butt_2 = InlineKeyboardButton(text='Формулы расчёта' , callback_data='calories')
ikeybrt.add(butt_1)
ikeybrt.add(butt_2)
@disp.message_handler(text = 'Рассчитать')
async def main_menu(message):
    await message.answer(text='Выберите опцию:', reply_markup=ikeybrt)
@disp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('Формула: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5')
    await call.answer()

@disp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью. У меня есть клавиатура', reply_markup= keybr)
@disp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age = message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()
#@disp.message_handler(state=UserState.growth)
@disp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()
async def set_weight(message, state):
    await state.update_data(growth = message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()
@disp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    colory = 10 * int(data['weight']) + 6.25 * int(data['growth']) - 5 * int(data['age']) + 5
    await message.answer(colory)
    await state.finish()
@disp.message_handler()
async def all_massages(message):
    await message.answer('Введите команду /start, чтобы начать общение.')

if __name__=='__main__':
    executor.start_polling(disp,skip_updates=True)


