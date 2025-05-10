



from fle.rpg_game.work_with_predmeti import *
import json
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

BOT_TOKEN = '8059621407:AAH-qpRLUs6Xfn5DNt1FWegnMasSPJ0ITFQ'

PATH_SUCHET= "fle/rpg_game/json/suget.json"
PHOTO_PATH="fle/rpg_game/photos/"
PATH_IGROKI="fle/rpg_game/json/igroki.json"

bot = Bot(token=BOT_TOKEN)
storage=MemoryStorage()
dp = Dispatcher(bot, storage=storage)

class IgraState(StatesGroup):
    SetName=State()
    Find=State()

def load_data(DATA):
    try:
        with open(DATA, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_data(DATA, data):
    with open(DATA, "w",encoding="utf-8") as file:
        json.dump(data, file,ensure_ascii=False, indent=4)

def create_reply_markup():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)  # kb создаём новою клав.
    b1 = KeyboardButton('inventar')
    kb.add(b1)
    return kb
def create_markup(sp):
    keyboard = InlineKeyboardMarkup()
    for i in sp:
        text = list(i.keys())[0]
        callback = list(i.values())[0]
        keyboard.add(InlineKeyboardButton(text, callback_data=callback))
    return keyboard
"""
функции для поиска сокровищ
"""

def create_markup_Find():
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton("искать", callback_data="искать"), InlineKeyboardButton("прекратить поиски", callback_data="прекратить поиски"))
    return kb

async def Find(user_id):
    await bot.send_message(user_id, "ты находишься в ппещере.", reply_markup=create_markup_Find())
    await IgraState.Find.set()

@dp.callback_query_handler(state=IgraState.Find)
async def find_callback(callback_query: types.CallbackQuery, state: FSMContext):
    user_id = str(callback_query.from_user.id)

    if callback_query.data=="прекратить поиски":
        await iterator(user_id, id="3")
        await state.finish()

        await callback_query.answer()
    elif callback_query.data=="искать":
        id_predmet=get_choice_random_id_predmet(50)

        if id_predmet==None:
            await bot.send_message(user_id, "ты потратил время на поиски, но ничего не нашёл.")
            await Find(user_id)

        else:
            set_predmet_to_igrok(id_predmet, user_id)
            predmet=get_predmet_by_id(id_predmet)

            try:
                photo = open(PHOTO_PATH + "predmeti/" + id_predmet + ".jpg", 'rb')
                await bot.send_photo(user_id, photo=photo, caption=f"ты нашёл  {predmet.get('name')} \n {predmet.get('name')} - {predmet.get('opisanie')}.")
            except:
                await bot.send_message(user_id, f"ты нашёл  {predmet.get('name')} \n {predmet.get('name')} - {predmet.get('opisanie')}.")

            await Find(user_id)

"""
функции для установки никнейма
"""

async def SetName1(user_id):
    await bot.send_message(user_id, "назови своё имя, страник.")
    await IgraState.SetName.set() #установка стейта

@dp.message_handler(state=IgraState.SetName)
async def Set_Name(message: types.Message):
    user_id = str(message.from_user.id)
    await message.reply(f"Ваше имя {message.text}?", reply_markup=create_markup_Set_name())
    data_igroki=load_data(PATH_IGROKI)
    data_igroki[user_id]["nickname"]=message.text
    save_data(PATH_IGROKI, data_igroki)

def create_markup_Set_name():
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton("да", callback_data="да"), InlineKeyboardButton("нет", callback_data="нет"))
    return kb

@dp.callback_query_handler(state=IgraState.SetName)
async def callback_handler(callback_query: types.CallbackQuery, state: FSMContext):
    user_id = str(callback_query.from_user.id)
    if callback_query.data=="да":
        await state.finish()
        await iterator(user_id, "2")
    elif callback_query.data=="нет":
        igroki = load_data(PATH_IGROKI)
        igroki[user_id]["nickname"] = "##############"
        save_data(PATH_IGROKI, igroki)
        await SetName1(user_id)


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    user_id = str(message.from_user.id)
    data=load_data(PATH_IGROKI)
    if user_id not in data:
        data[user_id]={}
        data[user_id]["username"]=message.from_user.username
        save_data(PATH_IGROKI, data)

    await bot.send_message(user_id, "привет", reply_markup=create_reply_markup())

    await iterator(user_id, id="1")

async def iterator(user_id, id="1"):
    data = load_data(PATH_SUCHET)

    text=data["suget"][id]["text"]
    photo_name=data["suget"][id].get("photo", None)
    buttons=data["suget"][id]["buttons"]


    if photo_name:
        photo =  open(PHOTO_PATH + photo_name, 'rb')
        await bot.send_photo(user_id, photo=photo, caption=text,reply_markup=create_markup(buttons))
    else:
        await bot.send_message(user_id,  text=text, reply_markup=create_markup(buttons))

@dp.message_handler(commands=["inventar"])
async def start_command(message: types.Message):
    user_id = str(message.from_user.id)
    data=load_data()
    st=f"у вас есть; \n"
    if message.text=="inventar":
        predmeti=get_inventar(user_id)
    for keys in predmeti.values():
        st=st+f"{keys}\n"
    await bot.send_message(user_id, st)

@dp.callback_query_handler()
async def handle_callback(callback_query: types.CallbackQuery):
    user_id = str(callback_query.from_user.id)
    if callback_query.data.startswith("id"):
        await iterator(user_id, id=callback_query.data[2:])
        await callback_query.answer()
    elif callback_query.data=="SetName":
        await SetName1(user_id)
    elif callback_query.data=="Find":
        await Find(user_id)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)