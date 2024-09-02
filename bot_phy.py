import os
import re
from aiogram import  Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

with open('conf_both.cnf', 'r') as cnf:
    ctxt = cnf.read()
    po = re.search('(?<=' + 'bot_kye=' + ').*?(?=\n)', ctxt)
    key_bot_api = po.group(0)
    # print(key_bot)
bot = Bot(token=key_bot_api)
disp = Dispatcher(bot, storage=MemoryStorage())

@disp.message_handler(commands=['start'])
async def start(message):
    print('Привет! Я бот помогающий твоему здоровью.')


@disp.message_handler()
async def all_massages(message):
    print('Введите команду /start, чтобы начать общение.')


if __name__=='__main__':
    executor.start_polling(disp,skip_updates=True)


