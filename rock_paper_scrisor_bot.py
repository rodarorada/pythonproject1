







import random
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
API_token="7967265135:AAGeS3r3l7lftqcUwYGHwwYhlLblmuRZCtc"

bot = Bot(token=API_token)
dp = Dispatcher(bot)



kb=ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True) # kb создаём новою клав.
kb2=ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
b1=KeyboardButton('/rock_easyBot') # новая кнопка
b2=KeyboardButton('/paper_easyBot')
b3=KeyboardButton('/scrisor_easyBot')

b4=KeyboardButton('/rock_hardBot') # новая кнопка
b5=KeyboardButton('/paper_hardBot')
b6=KeyboardButton('/scrisor_hardBot')

kb.add(b1) # add новая строка
kb.insert(b2) # insert добовление в строку
kb.add(b3)

kb2.add(b4) # add новая строка
kb2.insert(b5) # insert добовление в строку
kb2.add(b6)



@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply('привет, я бот играющий в камень, ножницы, бумага. для большей информации напиши /help') # reply ответ, не использует id, reply_markup=kb встовляем клавиатуру в сообщение


@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    await bot.send_message(message.chat.id,'ты использoвал /start /help но,тут есть и /game_rull /game') # send просто сообщение, требует id

@dp.message_handler(commands=['game_rull'])
async def game_rull(message: types.Message):
    await message.reply('правила тут просты. камень бьёт ножницы, ножницы бьют бумагу,бумага бьёт камень. если хочешь играть,то у тебя есть клавиши')

@dp.message_handler(commands=['game'])
async def game(message: types.Message):
    await bot.send_message(message.chat.id,'давай начнём со сложности /easy а потом /hard')

@dp.message_handler(commands=['hard'])
async def easy(message: types.Message):
    await bot.send_message(message.chat.id,'здаров! я сложный бот, давай сыграем!', reply_markup=kb2)

    @dp.message_handler(commands=['rock_hardBot'])
    async def easy(message: types.Message):
        await bot.send_message(message.chat.id,'ха! я выбрал бумагу, я победил.может ещё разок?', reply_markup=kb2)

    @dp.message_handler(commands=['paper_hardBot'])
    async def easy(message: types.Message):
        await bot.send_message(message.chat.id,'ха! я выбрал ножницы, я победил.может ещё разок?', reply_markup=kb2)

    @dp.message_handler(commands=['scrisor_hardBot'])
    async def easy(message: types.Message):
        await bot.send_message(message.chat.id,'ха! я выбрал камень, я победил.может ещё разок?', reply_markup=kb2)

@dp.message_handler(commands=['easy'])
async def easy(message: types.Message):
    await bot.send_message(message.chat.id,'привет, я простой бот, давай сыграем?', reply_markup=kb)

    easy = ["о. я победил, ведь я использовал бумагу. может ещё раз?",
            "ничья, я тоже использовал камень. может ещё раз?", "ты выйграл, у меня ножницы. может ещё раз?"]
    easy1 = ["о. я победил, ведь я использовал ножницы. может ещё раз?",
             "ничья, я тоже использовал бумагу. может ещё раз?", "ты выйграл, у меня камень. может ещё раз?"]
    easy2 = ["о. я победил, ведь я использовал камень. может ещё раз?",
             "ничья, я тоже испозовал ножницы. может ещё раз?", "ты выйграл, у меня бумага. может ещё раз?"]

    otvet = random.choice(easy)
    otvet1 = random.choice(easy1)
    otvet2 = random.choice(easy2)

    @dp.message_handler(commands=['rock_easyBot'])
    async def easy(message: types.Message):
        await bot.send_message(message.chat.id,otvet, reply_markup=kb)

    @dp.message_handler(commands=['paper_easyBot'])
    async def easy(message: types.Message):
        await bot.send_message(message.chat.id, otvet1, reply_markup=kb)

    @dp.message_handler(commands=['scrisor_easyBot'])
    async def easy(message: types.Message):
        await bot.send_message(message.chat.id, otvet2, reply_markup=kb)

# @dp.message_handler()
# async def start(message: types.Message):
#     if message.text=='foto':
#         await bot.send_photo(message.chat.id,'https://s1.1zoom.me/big3/652/342768-sepik.jpg')
#     else:
#         await message.reply('я ваша не понимать', reply_markup=kb)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)


