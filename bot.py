from aiogram import executor
from aiogram import types
from dispatcher import dp

from Bothelp import BotDB
BotDB = BotDB('baza.db')

@dp.message_handler(commands = "start")
async def start(message: types.Message):
    await message.reply("Добро пожаловать!")


@dp.message_handler(commands='chek_url')
async def start(message: types.Message):
    await message.reply("Отправь сслыку")

@dp.message_handler()
async def url(message: types.Message):
    if (not BotDB.url(message.text)):
        if (BotDB.classification(message.text))==True:
            await message.reply('Это не фишинговая ссылка')
            BotDB.add_url(message.text,0)
        else:
            await message.reply('Это фишинговая ссылка')
            BotDB.add_url(message.text, 1)
    else:
        if (not BotDB.label(message.text)):
            await message.reply('Это  (фишинговая) ссылка')
        else:
            await message.reply('Это  (не)фишинговая ссылка')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)