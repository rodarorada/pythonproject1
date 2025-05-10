

import random
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

API_token="7787937447:AAFD_FAlrZ3IjcF5H3-kOPTj9MZMp9IWi6c"

bot = Bot(token=API_token)
dp = Dispatcher(bot)


roomm=ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
generatorr=ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
cams=ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

gen=20

b1=KeyboardButton('/cam')
b2=KeyboardButton('/midl_door')
b3=KeyboardButton('/generator')

b4=KeyboardButton('/fill')
b5=KeyboardButton('/room')

roomm.add(b2)
roomm.insert(b1)
roomm.add(b3)

generatorr.add(b4)
generatorr.add(b5)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply('привет, я бот играющий во FNAF. для большей информации напиши /help')

@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
   await bot.send_message(message.chat.id,'привет, если тебе нужна помощь, то ты обратился по номеру. тут всё достаточно просто. следи за монстрами по камерам и одбивайся от них. но учти, нету монстров работующих одинаково и для каждого нужен свой подход. чтобы всё попробовать сейчас, /game')

@dp.message_handler(commands=['game'])
async def send_welcome(message: types.Message):
    await message.reply('ты в офисе...',reply_markup=roomm)

@dp.message_handler(commands=['room'])
async def send_welcome(message: types.Message):
    await message.reply('ты в офисе...',reply_markup=roomm)
    global gen
    gen=gen-1
    return gen

@dp.message_handler(commands=['generator'])
async def send_welcome(message: types.Message):
    await message.reply('ты в генераторной...',reply_markup=generatorr)
    global gen
    gen=gen-1
    return gen

@dp.message_handler(commands=['fill'])
async def send_welcome(message: types.Message):
    await message.reply('энергия восполнина...',reply_markup=generatorr)
    global gen
    gen=20
    return gen

@dp.message_handler(commands=['cam_room'])
async def send_welcome(message: types.Message):
    await message.reply('камера?',reply_markup=cams)
    global gen
    gen=gen-1
    return gen










if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)