




from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

API_token="7653439755:AAGrBSXnmcXIr8o-bCgQDcjMoyujn8431QQ"

bot = Bot(token=API_token)
dp = Dispatcher(bot)


ikb=InlineKeyboardMarkup(row_width=3)

ib1=InlineKeyboardButton('silka', url='https://yandex.ru/images/search?lr=213&text=рикролл')
ib2=InlineKeyboardButton('hjyguy', callback_data='1')

ikb.add(ib1,ib2)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    print(message)
    await message.reply('тут чтото написали' ) # reply ответ, не использует id


@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    await bot.send_message(message.chat.id,'помощи нэ будэт, но /start /help', reply_markup=ikb) # send просто сообщение, требует id

@dp.message_handler()
async def start(message: types.Message):
    if message.text=='foto':
        await bot.send_photo(message.chat.id,'https://s1.1zoom.me/big3/652/342768-sepik.jpg')
    else:
        await message.reply('я ваша не понимать')


@dp.callback_query_handler()
async def ooo(callback: types.callback_query):
    if callback.data == '1':
        await callback.answer(text="не нажимай")




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)


""""
{"message_id": 67,
 "from": {"id": 6402241967, "is_bot": false, "first_name": "Rodarorada", "username": "Dio_comunist", "language_code": "ru"}, 
 "chat": {"id": 6402241967, "first_name": "Rodarorada", "username": "Dio_comunist", "type": "private"},
  "date": 1729359856, "text": "/start",
   "entities": [{"type": "bot_command", "offset": 0, "length": 6}]}



"""