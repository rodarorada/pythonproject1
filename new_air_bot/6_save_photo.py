import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor

BOT_TOKEN = '6403405667:AAEF8AQPPRDHyRkHQb-y3mjpLxpJ0odmofg' #@morfius_test2_bot
PHOTO_FOLDER = "photos"
VIDEO_FOLDER = "videos"
VOICE_FOLDER = "voice"

# Создаём папки, если их нет
os.makedirs(PHOTO_FOLDER, exist_ok=True)
os.makedirs(VIDEO_FOLDER, exist_ok=True)
os.makedirs(VOICE_FOLDER, exist_ok=True)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# Храним последние файлы каждой категории
last_photo_filename = None
last_video_filename = None
last_voice_filename = None

# Кнопки для отправки контента
photo_button = KeyboardButton("/photo")
video_button = KeyboardButton("/video")
voice_button = KeyboardButton("/voice")

# Создаём клавиатуру
keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(photo_button, video_button, voice_button)

# Обработка фото
@dp.message_handler(content_types=["photo"])
async def handle_photo(message: types.Message):
    global last_photo_filename

    # Получаем file_id и скачиваем фото
    file_id = message.photo[-1].file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path # путь в телеграмме

    # Сохраняем фото
    last_photo_filename = f"{file_id}.jpg"
    file_local_path = os.path.join(PHOTO_FOLDER, last_photo_filename)

    await bot.download_file(file_path, file_local_path)

    await message.reply(f"Фото сохранено как {last_photo_filename}!", reply_markup=keyboard)

# Обработка видео
@dp.message_handler(content_types=["video"])
async def handle_video(message: types.Message):
    global last_video_filename

    # Получаем file_id и скачиваем видео
    file_id = message.video.file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path

    # Сохраняем видео
    last_video_filename = f"{file_id}.mp4"
    file_local_path = os.path.join(VIDEO_FOLDER, last_video_filename)

    await bot.download_file(file_path, file_local_path)

    await message.reply(f"Видео сохранено как {last_video_filename}!", reply_markup=keyboard)


# Обработка голосовых сообщений
@dp.message_handler(content_types=["voice"])
async def handle_voice(message: types.Message):
    global last_voice_filename

    # Получаем file_id и скачиваем голосовое сообщение
    file_id = message.voice.file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path

    # Сохраняем голосовое сообщение
    last_voice_filename = f"{file_id}.ogg"
    file_local_path = os.path.join(VOICE_FOLDER, last_voice_filename)

    await bot.download_file(file_path, file_local_path)

    await message.reply(f"Голосовое сообщение сохранено как {last_voice_filename}!", reply_markup=keyboard)

# Кнопки для отправки последнего файла фото
@dp.message_handler(commands=["photo"])
async def send_last_photo(message: types.Message):
    if last_photo_filename:
        with open(os.path.join(PHOTO_FOLDER, last_photo_filename), "rb") as photo:
            await message.reply_photo(photo, reply_markup=keyboard)
    else:
        await message.reply("Нет сохранённых фото.", reply_markup=keyboard)

# Кнопки для отправки последнего файла видео
@dp.message_handler(commands=["video"])
async def send_last_video(message: types.Message):
    if last_video_filename:
        with open(os.path.join(VIDEO_FOLDER, last_video_filename), "rb") as video:
            await message.reply_video(video, reply_markup=keyboard)
    else:
        await message.reply("Нет сохранённых видео.", reply_markup=keyboard)


# Кнопки для отправки последнего голосового сообщения
@dp.message_handler(commands=["voice"])
async def send_last_voice(message: types.Message):
    if last_voice_filename:
        with open(os.path.join(VOICE_FOLDER, last_voice_filename), "rb") as voice:
            await message.reply_voice(voice, reply_markup=keyboard)
    else:
        await message.reply("Нет сохранённых голосовых сообщений.", reply_markup=keyboard)

if __name__ == "__main__":
    executor.start_polling(dp)
