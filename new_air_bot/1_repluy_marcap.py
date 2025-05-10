from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor

# Токен вашего бота
BOT_TOKEN = '6403405667:AAEF8AQPPRDHyRkHQb-y3mjpLxpJ0odmofg' #@morfius_test2_bot

# Создание объекта бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# Создаем реплай-клавиатуру
keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(KeyboardButton("Кнопка 1"), KeyboardButton("Кнопка 2"))

# Хэндлер команды /start
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply("Привет! Это бот с клавиатурой.", reply_markup=keyboard)

# Хэндлер нажатий на кнопки
@dp.message_handler()
async def button_handler(message: types.Message):
    if message.text == "Кнопка 1":
        await message.reply("Вы нажали Кнопка 1!")
    elif message.text == "Кнопка 2":
        await  bot.send_message(message.chat.id, "Вы нажали Кнопка 2!")


# Запуск бота
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)


"""

## pip install --force-reinstall -v "aiogram==2.23.1"

"""