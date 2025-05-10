



import json
import os
import random
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
API_token='8012549233:AAFMOqhI3U_cz2jOPMJofB1nQBrz5Ni97VQ'

bot = Bot(token=API_token)
dp = Dispatcher(bot)

photo_path="rpg_game/photos/"
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

random_photo={photo_path[1]},{photo_path[2]},{photo_path[3]}
slovari={
    "1": "1.jpg",
    "2": "2.jpg",
    "3": "3.jpg",
}

@dp.message_handler(commands=['start'])
async def send_welcom(message: types.Message):
    user_id = str(message.from_user.id)

    name_photo=random.choice(list(slovari.values()))
    print(name_photo)
    file = open(photo_path+name_photo, "rb")


    await bot.send_photo(user_id, file)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)