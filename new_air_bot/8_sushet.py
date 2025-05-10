import json
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor

BOT_TOKEN = '6403405667:AAEF8AQPPRDHyRkHQb-y3mjpLxpJ0odmofg' #@morfius_test2_bot
DATA_FILE = "files/rpg_igra/json/suchet.json"
PHOTO_PATH = "files/rpg_igra/photos/"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

def load_data():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_data(data):
    with open(DATA_FILE, "w",encoding="utf-8") as file:
        json.dump(data, file,ensure_ascii=False, indent=4)


def create_markup(sp):
    keyboard = InlineKeyboardMarkup()
    for i in sp:
        text= list(i.keys())[0]
        callback=list(i.values())[0]
        keyboard.add(InlineKeyboardButton(text, callback_data=callback))
    return keyboard


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    user_id = str(message.from_user.id)
    await iterator(user_id, id="1")


async def iterator(user_id, id="1"):
    data = load_data()

    text=data["suchet"][id]["text"]
    photo_name=data["suchet"][id].get("photo", None)
    buttons=data["suchet"][id]["buttons"]

    if photo_name:
        photo =  open(PHOTO_PATH + photo_name, 'rb')
        await bot.send_photo(user_id, photo=photo, caption=text,reply_markup=create_markup(buttons))
    else:
        await bot.send_message(user_id,  text=text,reply_markup=create_markup(buttons))


@dp.callback_query_handler()
async def handle_callback(callback_query: types.CallbackQuery):
    user_id = str(callback_query.from_user.id)
    if callback_query.data.startswith("id"):
        await iterator(user_id, id=callback_query.data[2:])
        await callback_query.answer()



if __name__ == "__main__":
    executor.start_polling(dp)