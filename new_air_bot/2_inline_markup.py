from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor

# Токен вашего бота
BOT_TOKEN = '6403405667:AAEF8AQPPRDHyRkHQb-y3mjpLxpJ0odmofg' #@morfius_test2_bot

# Создание объекта бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# Создаем инлайн-клавиатуру
keyboard = InlineKeyboardMarkup(row_width=2)
keyboard.add(
    InlineKeyboardButton("Кнопка 1", callback_data="button1"),
    InlineKeyboardButton("Кнопка 2 (котик)", callback_data="button2"),
    InlineKeyboardButton("хочу фотку котика", url="https://avatars.mds.yandex.net/i?id=325bcdf905e6685f354011427095fa3f_l-5233671-images-thumbs&n=13")
)

# Хэндлер команды /start
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply("Привет! Это бот с инлайн-клавиатурой.", reply_markup=keyboard)

# Хэндлер нажатий кнопок (callback_data)
@dp.callback_query_handler(text = ["button1", "button2"])
async def button_handler(callback_query: types.CallbackQuery):
    if callback_query.data == "button1":
        await bot.answer_callback_query(callback_query.id) # подтверждение для телеграм что мы обработали колбак
        await bot.send_message(callback_query.from_user.id, "Вы нажали Кнопка 1!")
    elif callback_query.data == "button2":
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, "https://i.pinimg.com/736x/e8/8f/30/e88f3028afe762960b7a2c11837b34d1.jpg")

# Запуск бота
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
