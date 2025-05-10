import json
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

BOT_TOKEN = '6403405667:AAEF8AQPPRDHyRkHQb-y3mjpLxpJ0odmofg' #@morfius_test2_bot
PATH_SUSHET = "files/rpg_igra/json/suchet2.json"
PATH_IGROKI = "files/rpg_igra/json/igroki.json"
PATH_PHOTO = "files/rpg_igra/photos/"

bot = Bot(token=BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot,storage=storage)


class IgraState(StatesGroup):
    SetName = State()


def load_data(DATA):
    try:
        with open(DATA, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_data(DATA, data):
    with open(DATA, "w", encoding="utf-8") as file:
        json.dump(data, file,ensure_ascii=False, indent=4)


def create_markup(sp):
    keyboard = InlineKeyboardMarkup()
    for i in sp:
        text= list(i.keys())[0]
        callback=list(i.values())[0]
        keyboard.add(InlineKeyboardButton(text, callback_data=callback))
    return keyboard

def create_markup_Set_name():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("да", callback_data="да"),InlineKeyboardButton("нет", callback_data="нет"))
    return keyboard


async def Set_Name1(user_id):
    await bot.send_message(user_id, "введи свое имя, странник")
    await IgraState.SetName.set()


@dp.message_handler(state=IgraState.SetName)
async def Set_Name(message: types.Message):
    user_id = str(message.from_user.id)
    await message.reply(f"Ваше имя {message.text}?",reply_markup=create_markup_Set_name())
    data_igroki = load_data(PATH_IGROKI)
    data_igroki[user_id]["nickname"] = message.text
    save_data(PATH_IGROKI, data_igroki)



@dp.callback_query_handler(state=IgraState.SetName)
async def handle_callback(callback_query: types.CallbackQuery,state: FSMContext):
    user_id = str(callback_query.from_user.id)
    if callback_query.data=="да":
        await state.finish()
        await iterator(user_id,"2")
    elif callback_query.data=="нет":
        data_igroki = load_data(PATH_IGROKI)
        data_igroki[user_id]["nickname"] = "########"
        save_data(PATH_IGROKI, data_igroki)
        await Set_Name1(user_id)






@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    user_id = str(message.from_user.id)
    data_igroki =load_data(PATH_IGROKI)
    if user_id not in data_igroki:
        data_igroki[user_id]={}
        data_igroki[user_id]["username"] = message.from_user.username
        data_igroki[user_id]["nickname"] = "########"
        save_data(PATH_IGROKI, data_igroki)
    await iterator(user_id, id="1")


async def iterator(user_id, id="1"):
    data = load_data(PATH_SUSHET)

    text=data["suchet"][id]["text"]
    photo_name=data["suchet"][id].get("photo", None)
    buttons=data["suchet"][id]["buttons"]

    if photo_name:
        photo =  open(PATH_PHOTO + photo_name, 'rb')
        await bot.send_photo(user_id, photo=photo, caption=text,reply_markup=create_markup(buttons))
    else:
        await bot.send_message(user_id,  text=text,reply_markup=create_markup(buttons))


@dp.callback_query_handler()
async def handle_callback(callback_query: types.CallbackQuery):
    user_id = str(callback_query.from_user.id)

    if callback_query.data.startswith("id"):
        await iterator(user_id, id=callback_query.data[2:])
        await callback_query.answer()
    elif callback_query.data =="SetName":
        await Set_Name1(user_id)








if __name__ == "__main__":
    executor.start_polling(dp)