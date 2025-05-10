



import json
import os
import random
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
API_token='8012549233:AAFMOqhI3U_cz2jOPMJofB1nQBrz5Ni97VQ'

bot = Bot(token=API_token)
dp = Dispatcher(bot)

data_file="strang.json"

def load_data():
    try:
        with open(data_file,"r", encoding="utf-8") as file:
            return json.load(file)
    except:
        return {}

def save_data(data):
    with open(data_file,"w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def get_reply_keybort(user_id):
    kb=ReplyKeyboardMarkup(resize_keyboard=True)
    data=load_data()
    kb.add(KeyboardButton("id"), KeyboardButton(f"name"), KeyboardButton(f"last_name"))
    return kb

@dp.message_handler(commands=['start'])
async def send_welcom(message: types.Message):
    user_id = str(message.from_user.id)
    data = load_data()

    if user_id not in data:
        data[user_id]={}
        data[user_id]["id"] = message.from_user.id
        data[user_id]["name"] = message.from_user.first_name
        data[user_id]["last_name"] = message.from_user.last_name
        save_data(data)

    await bot.send_message(user_id, "/id   /name     /last_name   ")

@dp.message_handler(commands=['id'])
async def send_id(message: types.Message):
    user_id=str(message.from_user.id)
    data=load_data()

    id = data[user_id]['id']

    await message.answer(f" твой id = {id}.")

@dp.message_handler(commands=['name'])
async def send_name(message: types.Message):
    user_id=str(message.from_user.id)
    data=load_data()

    await message.answer(f" твой name = {data[user_id]['name']}.")

@dp.message_handler(commands=['last_name'])
async def send_id(message: types.Message):
    user_id=str(message.from_user.id)
    data=load_data()

    await message.answer(f" твой last name = {data[user_id]['last_name']}.")

executor.start_polling(dp, skip_updates=True)