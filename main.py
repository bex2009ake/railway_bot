from aiogram import Bot, Dispatcher, types, executor
from dotenv import load_dotenv
import requests
import os



load_dotenv()
API_TOKEN = os.getenv('TOKEN')
BANK_URL = os.getenv('URL')


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def start_func(msg: types.Message):
    await msg.answer('Hello I`m bot !!!')

@dp.message_handler()
async def money_func(msg: types.Message):
    try:
        data = msg.text.split(' ')
        res = requests.get(BANK_URL+data[0])
        await msg.answer(res.json()['conversion_rates'][data[1]])
    except:
        await msg.answer('Something is wrong')


if __name__ == '__main__':
    executor.start_polling(dp)