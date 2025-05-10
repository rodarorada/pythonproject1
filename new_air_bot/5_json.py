import  json

import asyncio
from aiogram import Bot,Dispatcher, types
from aiogram.utils import executor

BOT_TOKEN = '6403405667:AAEF8AQPPRDHyRkHQb-y3mjpLxpJ0odmofg' #@morfius_test2_bot
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# Имя файла для хранения данных
DATA_FILE = "files/users.json"


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    print(message)


    try: # попытка что-то сделать
        file=  open(DATA_FILE, "r")
        users=json.load(file)
    except:     # если не получилось
        users={}

    users[message.from_user.id]=message.from_user.username
    with open(DATA_FILE, "w") as file:
        json.dump(users, file, indent=4)

    await message.reply("Ты был добавлен в базу!")


async def on_startup(_):
    with open( DATA_FILE, "r") as file:
        users=json.load(file)
        for i in users.keys():
            await bot.send_message(i, "привет, я тебя помню.")


if __name__ == "__main__":

    executor.start_polling(dp,skip_updates=True, on_startup=on_startup)

"""
{"message_id": 434, 
"from": {"id": 806948129, "is_bot": false, "first_name": "Андрей", "last_name": "Кристоф", "username": "kristof271", "language_code": "ru"},
 "chat": {"id": 806948129, "first_name": "Андрей", "last_name": "Кристоф", "username": "kristof271", "type": "private"},
  "date": 1734802411, "text": "/start", "entities": [{"type": "bot_command", "offset": 0, "length": 6}]}

"""






























# persons={
#     "0000": {
#         "name":"andrey",
#         "age":21
#     },
#     "0001": {
#         "name":"vasya",
#         "age":35
#     }
# }
# with open("files/users.json","w") as file:
#     json.dump(persons, file,ensure_ascii=False, indent=4)
#     """
#     persons что пишем
#     file куда
#     ensure_ascii=False для того, чтобы файл был читаем
#     indent=4  отсупы по 4 пробела
#     """
# with open("files/users.json","r") as file:
#     data=json.load(file)
#     print(data)
#
# data["0002"]={
#         "name":"petya",
#         "age":40
#     }
#
# data["0000"]["age"]=23
#
# with open("files/users.json","w") as file:
#     json.dump(data, file, ensure_ascii=False, indent=4)