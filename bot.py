








from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
API_token="7653439755:AAGrBSXnmcXIr8o-bCgQDcjMoyujn8431QQ"

bot = Bot(token=API_token)
dp = Dispatcher(bot)

kb=ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True) # kb создаём новою клав.
b1=KeyboardButton('/help') # новая кнопка
b2=KeyboardButton('/description')
b3=KeyboardButton('/foto')

kb.add(b1) # add новая строка
kb.insert(b2) # insert добовление в строку
kb.add(b3)



@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    print(message)
    await message.reply('тут чтото написали', reply_markup=kb) # reply ответ, не использует id, reply_markup=kb встовляем клавиатуру в сообщение


@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    await bot.send_message(message.chat.id,'помощи нэ будэт, но /start /help', reply_markup=kb) # send просто сообщение, требует id

@dp.message_handler()
async def start(message: types.Message):
    if message.text=='foto':
        await bot.send_photo(message.chat.id,'https://s1.1zoom.me/big3/652/342768-sepik.jpg')
    else:
        await message.reply('я ваша не понимать', reply_markup=kb)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)


""""
{"message_id": 67,
 "from": {"id": 6402241967, "is_bot": false, "first_name": "Rodarorada", "username": "Dio_comunist", "language_code": "ru"}, 
 "chat": {"id": 6402241967, "first_name": "Rodarorada", "username": "Dio_comunist", "type": "private"},
  "date": 1729359856, "text": "/start",
   "entities": [{"type": "bot_command", "offset": 0, "length": 6}]}
"""