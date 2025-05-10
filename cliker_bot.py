


import json
import os
import random
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
API_token="7677225240:AAEvi5kt009BLUYgj-44kIbVdHHT5vc_Rkw"

bot = Bot(token=API_token)
dp = Dispatcher(bot)

data_file="fle/cliker_data.json"

def load_data():
    try:
        with open(data_file,"r", encoding="utf-8") as file:
            return json.load(file)
    except:
        return {}

def save_data(data):
    with open(data_file,"w") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

default_user_data={
    "balance": 0,
    "profit_per_clik": 1,
    "upgrade_cost": 10,
    "name": "anonim"
}

def get_reply_keybort(user_id):
    kb=ReplyKeyboardMarkup(resize_keyboard=True)
    data=load_data()
    stoimost=data[user_id]["upgrade_cost"]
    kb.add(KeyboardButton("Вывести баланс"), KeyboardButton(f"улучшить клик за {stoimost}"))
    return kb

def get_extend_keybort():
    kb=InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton("когда листинг?", callback_data="listing"))
    return kb

def get_inline_keybort(user_id):
    kb=InlineKeyboardMarkup()
    data=load_data()
    balance=data[user_id]["balance"]
    kb.add(InlineKeyboardButton("клик", callback_data="clik"))
    if balance>=20:
        kb.add(InlineKeyboardButton("мегаклик", callback_data="clik2"))
    return kb

@dp.message_handler(commands=['start'])
async def send_welcom(message: types.Message):
    user_id=str(message.from_user.id)
    data=load_data()

    if user_id not in data:
        data[user_id]=default_user_data.copy()
        data[user_id]["name"]=message.from_user.first_name
        save_data(data)

    await message.answer(f"Добро пожаловать {data[user_id]['name']} в кликер!", reply_markup=get_reply_keybort(user_id))
    await message.answer(f"ваш баланс: {data[user_id]['balance']}", reply_markup=get_inline_keybort(user_id))

@dp.message_handler(lambda message: message.text=="Вывести баланс")
async def show_balance(message: types.Message):
    user_id=str(message.from_user.id)
    data = load_data()
    balance=data.get(user_id,default_user_data["balance"])
    await message.answer(f"ваш баланс: {balance}", reply_markup=get_inline_keybort(user_id))

@dp.callback_query_handler()
async def show_balance(callback_query: types.CallbackQuery):
    user_id=str(callback_query.from_user.id)
    data = load_data()
    user_data = data.get(user_id, default_user_data)

    if callback_query.data=="clik":

        user_data["balance"]=user_data["balance"]+user_data["profit_per_clik"]
        data[user_id]=user_data
        save_data(data)
    if callback_query.data=="clik2":
        user_data=data.get(user_id,default_user_data)
        user_data["balance"]=user_data["balance"]+100
        data[user_id]=user_data
        save_data(data)

    text = f"ваш текущий баланс: {user_data['balance']}"
    await callback_query.message.edit_text(text, reply_markup=get_inline_keybort(user_id))

    # if user_data["balance"] >= 20:
    #     print("когда листинг? - OK")
    #     await callback_query.message.edit_text(text, reply_markup=get_extend_keybort())
    # else:
    #     print("когда листинг? - NOT")
    #     await callback_query.message.edit_text(text, reply_markup=get_inline_keybort(user_id))

    await callback_query.answer()

@dp.message_handler()
async def show_balance(message: types.Message):
    global kb
    user_id=str(message.from_user.id)
    data = load_data()

    if message.text.startswith("улучшить клик"):
        user_data=data.get(user_id,default_user_data)
        if user_data["balance"]>=user_data["upgrade_cost"]:
            user_data["balance"]-=user_data["upgrade_cost"]
            user_data["profit_per_clik"] += 1
            user_data["upgrade_cost"] *=2
            data[user_id]=user_data
            save_data(data)
            await message.answer(
                f"ваш клик улучшен! теперь вы получаете {user_data['profit_per_clik']} за клик. следующий апгрейт стоит {user_data['upgrade_cost']} кликов.", reply_markup=get_reply_keybort(user_id)
            )
        else:
            await message.answer(f"недостаточно средств для улучшения клика! нужно {user_data['upgrade_cost']} клилов.")


# @dp.message_handler(lambda message: message.text=="listing")
@dp.callback_query_handler(lambda callback_query: callback_query.data=="listing")
async def show_balance(callback_query: types.CallbackQuery):
    user_id = str(callback_query.from_user.id)
    await callback_query.message.edit_text("никогда мухахаха, я тебя затролил!\nты реально поверил? ЛОЛ!", reply_markup=get_inline_keybort(user_id))
    await callback_query.answer()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)