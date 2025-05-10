



import json
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

BOT_TOKEN = '8012549233:AAFMOqhI3U_cz2jOPMJofB1nQBrz5Ni97VQ'

data_file="dz_json/dz_2.json"

bot = Bot(token=BOT_TOKEN)
storage=MemoryStorage()
dp = Dispatcher(bot, storage=storage)

kb=InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True) # kb создаём новою клав.
b1=InlineKeyboardButton('knopka', callback_data='knopka')
kb.add(b1)

def load_data():
    try:
        with open(data_file,"r", encoding="utf-8") as file:
            return json.load(file)
    except:
        return {}

def save_data(data):
    with open(data_file,"w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

class perviiState(StatesGroup):
    S1=State()
    S2=State()
    S3=State()

@dp.message_handler(commands=['start'])
async def send_welcom(message: types.Message):
    user_id = str(message.from_user.id)
    data=load_data()
    await perviiState.S1.set()

    if user_id not in data:
        data[user_id]={}
        data[user_id]["id"] = message.from_user.id
        data[user_id]["user_name"] = message.from_user.username
        save_data(data)

    await bot.send_message(user_id, "введи имя")

@dp.message_handler(state=perviiState.S1)
async def send_welcom(message: types.Message):
    user_id = str(message.from_user.id)
    data=load_data()

    data[user_id]["name"]=message.text
    await bot.send_message(user_id, "введите свой возрост.")

    await perviiState.S2.set()

@dp.message_handler(state=perviiState.S2)
async def send_welcom(message: types.Message):
    user_id = str(message.from_user.id)
    data=load_data()

    data[user_id]["age"]=message.text
    await bot.send_message(user_id, "спасибо.", reply_markup=kb)

    await perviiState.S3.set()

# @dp.message_handler(state=perviiState.S3)
# async def send_welcom(message: types.Message):
#     user_id = str(message.from_user.id)
#     data=load_data()
#     if message.text=="knopka":
#
#         await bot.send_message(user_id, f"{data[user_id]['id']}")

@dp.callback_query_handler(state="*")
async def button_handler(callback_query: types.CallbackQuery):
    user_id = str(callback_query.from_user.id)
    data=load_data()
    if callback_query.data == "knopka":
        await bot.send_message(user_id, f"{data[user_id]['id']}")

executor.start_polling(dp, skip_updates=True)