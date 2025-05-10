



import json
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

BOT_TOKEN = '8012549233:AAFMOqhI3U_cz2jOPMJofB1nQBrz5Ni97VQ'

PATH_SUCHET= "fle/rpg_game/json/suget.json"
PHOTO_PATH="fle/rpg_game/photos/"
PATH_IGROKI="fle/rpg_game/json/igroki.json"

bot = Bot(token=BOT_TOKEN)
storage=MemoryStorage()
dp = Dispatcher(bot, storage=storage)

kb=ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True) # kb создаём новою клав.
b1=KeyboardButton('knopka')
kb.add(b1)

class perviiState(StatesGroup):
    S1=State()
    S2=State()
    S3 = State()

@dp.message_handler(commands=['start'])
async def send_welcom(message: types.Message):
    user_id = str(message.from_user.id)
    await perviiState.S1.set()

    await bot.send_message(user_id, "привет, сейчас первый стэйт", reply_markup=kb)

@dp.message_handler(state=perviiState.S1, commands=['knopka'])
async def send_welcom(message: types.Message):
    user_id = str(message.from_user.id)

    await perviiState.S2.set()

    await bot.send_message(user_id, "у тебя второй стэйт")


@dp.message_handler(state=perviiState.S2, commands=['knopka'])
async def send_welcom(message: types.Message):
    user_id = str(message.from_user.id)

    await perviiState.S3.set()

    await bot.send_message(user_id, "у тебя третий стэйт")


@dp.message_handler(state=perviiState.S3, commands=['knopka'])
async def send_welcom(message: types.Message):
    user_id = str(message.from_user.id)

    await perviiState.S1.set()

    await bot.send_message(user_id, "у тебя первый стэйт")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)