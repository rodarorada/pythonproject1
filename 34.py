import json
#
# persons={
#     "0000": {
#         "name":"ilya",
#         "age":11
#     },
#     "0001": {
#         "name":"vasya",
#         "age":355
#     }
# }
# with open("users.json","w") as file:
#     json.dump(persons,file,ensure_ascii=False,indent=4)
#     """
#     persons что пишем
#     file куда пишем
#     ensure_ascii=False для того, чтобы файл был читаем
#     indent=4 отступы по 4 пробела
#     """
#
# with open("users.json","r") as file:
#     data=json.load(file)
#     print(data)
#
# data["0002"]={
#     "name":"petya",
#     "age":40
#     }
#
# data["0000"]["age"]=12
#
#
# with open("users.json","w") as file:
#     json.dump(data,file,ensure_ascii=False,indent=4)


import random
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
API_token="8160336953:AAE70jhfhEc0uPr32s6AA7ra3aR3DFxK8IA"

bot = Bot(token=API_token)
dp = Dispatcher(bot)

kb=ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True) # kb создаём новою клав.
b1=KeyboardButton('info') # новая кнопка

kb.add(b1) # add новая строка

data_file="users.json"

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):

    try: #попытайся что-то сделать
        with open(data_file,"r",encoding="utf-8") as file:
            users=json.load(file)
    except: #если не получится
        users={}

    users[message.from_user.id]={}
    users[message.from_user.id]['username']=message.from_user.username
    users[message.from_user.id]['first_name']=message.from_user.first_name

    with open(data_file,"w") as file:
        json.dump(users,file, indent=4)

    await message.reply("Ты был добавлен в базу данных!", reply_markup=kb)

@dp.message_handler()
async def on_startup(message: types.Message):

    if message.text=='info':
        with open(data_file, "r") as file:
            users=json.load(file)
            for key, value in users.items():
                await bot.send_message(key, f"привет {value['first_name']}, с айди {key}, я тебя помню.")

"""
{"message_id": 67,
 "from": {"id": 6402241967, "is_bot": false, "first_name": "Rodarorada", "username": "Dio_comunist", "language_code": "ru"}, 
 "chat": {"id": 6402241967, "first_name": "Rodarorada", "username": "Dio_comunist", "type": "private"},
  "date": 1729359856, "text": "/start",
   "entities": [{"type": "bot_command", "offset": 0, "length": 6}]}
"""

if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)