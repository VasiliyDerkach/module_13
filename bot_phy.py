import os
import re
from aiogram import  Bot, Dispatcher, types, executor
from aiogram.comtrib.fsm_starage.memory import MemoryStorage
import asyncio
if __name__=='__main__':
    with open('conf_both.cnf','r') as cnf:
        ctxt = cnf.read()
        po = re.search('(?<=' + 'bot_kye=' + ').*?(?=\n)', ctxt)
        key_bot_api = po.group(0)
        #print(key_bot)
    bot = Bot(token=key_bot_api)
    disp = Dispatcher(bot, storage=MemoryStorage())

    @disp.message_handler()
    async def
