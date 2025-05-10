
import json
import os
import random
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
API_token="7970142487:AAFVMLN2U2p5wZYoeSt_Q0FeoXtZEzeDjd4"

bot = Bot(token=API_token)
dp = Dispatcher(bot)

data_file="users.json"

PHOTO_FOLDER="photos"
VIDEO_FOLDER="videos"
VOICE_FOLDER="voice"

os.makedirs(PHOTO_FOLDER, exist_ok=True) #создаём директорию
os.makedirs(VIDEO_FOLDER, exist_ok=True)
os.makedirs(VOICE_FOLDER, exist_ok=True)

last_photo_filename= None
last_video_filename= None
last_voice_filename= None

kb=ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True) # kb создаём новою клав.
b1=KeyboardButton('/photo') # новая кнопка
b2=KeyboardButton('/video')
b3=KeyboardButton('/voice')

kb.add(b1) # add новая строка
kb.insert(b2) # insert добовление в строку
kb.add(b3)

@dp.message_handler(content_types=["photo"])
async def handle_foto(message: types.Message):
    global last_photo_filename

    file_id=message.photo[-1].file_id
    file=await  bot.get_file(file_id)
    file_path=file.file_path

    last_photo_filename=f"{file_id}.jpg"

    file_local_path=PHOTO_FOLDER+"/"+last_photo_filename

    await bot.download_file(file_path, file_local_path)
    await write_file_name(message.from_user.username, last_photo_filename, file_local_path)

    await message.reply(f"фото сохранино как {last_photo_filename}")

@dp.message_handler(commands=['photo'])
async def send_welcome(message: types.Message):
    if last_photo_filename:
        photo=open(PHOTO_FOLDER+"/"+last_photo_filename, "rb")
        await message.reply_photo(photo, reply_markup=kb)
    else:
        await message.reply("нет сохранённых фото", reply_markup=kb)

@dp.message_handler(content_types=["video"])
async def handle_video(message: types.Message):
    global last_video_filename

    file_id=message.video.file_id
    file=await  bot.get_file(file_id)
    file_path=file.file_path

    last_video_filename=f"{file_id}.mp4"

    file_local_path=VIDEO_FOLDER+"/"+last_video_filename

    await bot.download_file(file_path, file_local_path)
    await write_file_name(message.from_user.username, last_video_filename, file_local_path)

    await message.reply(f"видео сохранино как {last_video_filename}")

@dp.message_handler(commands=['video'])
async def send_welcome(message: types.Message):
    if last_video_filename:
        video=open(VIDEO_FOLDER+"/"+last_video_filename, "rb")
        await message.reply_video(video, reply_markup=kb)
    else:
        await message.reply("нет сохранённых видео", reply_markup=kb)

@dp.message_handler(content_types=["voice"])
async def handle_voice(message: types.Message):
    global last_voice_filename

    file_id = message.voice.file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path

    last_voice_filename = f"{file_id}.ogg"

    file_local_path=VOICE_FOLDER+"/"+last_voice_filename

    await bot.download_file(file_path, file_local_path)
    await write_file_name(message.from_user.username,last_voice_filename,file_local_path)

    await message.reply(f"голосовое сообщение сохранено как {last_voice_filename}")

async def write_file_name(user_name,file_name,file_path):
    try: #попытайся что-то сделать
        with open(data_file,"r",encoding="utf-8") as file:
            users=json.load(file)
    except: #если не получится
        users={}

    if user_name not in users:
        users[user_name]={}
    users[user_name][file_name]=file_path

    with open(data_file,"w") as file:
        json.dump(users,file, indent=4)


@dp.message_handler(commands=['voice'])
async def send_welcome(message: types.Message):
    if last_voice_filename:
        voice=open(VOICE_FOLDER+"/"+last_voice_filename, "rb")
        await message.reply_voice(voice, reply_markup=kb)
    else:
        await message.reply("нет сохранённых голосовых сообщений", reply_markup=kb)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)