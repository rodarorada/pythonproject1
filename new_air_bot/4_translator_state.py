from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


from translate import Translator


# Включаем логирование


# Токен вашего бота
API_TOKEN = '6403405667:AAEF8AQPPRDHyRkHQb-y3mjpLxpJ0odmofg' #@morfius_test2_bot

# Инициализируем бота и диспетчер с состоянием в памяти
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


# Создаем классы состояний
class TranslateState(StatesGroup):
    ToEnglish = State()  # Состояние перевода с русского на английский
    ToRussian = State()  # Состояние перевода с английского на русский

# Создаем клавиатуру для выбора направления перевода
def get_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    b1 = KeyboardButton("На английский")
    b2 = KeyboardButton("На русский")
    keyboard.add(b1, b2)
    return keyboard

# Обработчик команды /start
@dp.message_handler(commands=['start'], state='*')
async def send_welcome(message: types.Message):
    await message.reply("Привет! Выбери направление перевода:", reply_markup=get_keyboard())
    await TranslateState.ToEnglish.set()  # Начинаем с перевода на английский

# Обработчик выбора "На английский"
@dp.message_handler(lambda message: message.text == "На английский", state='*')
async def set_to_english(message: types.Message):
    await message.reply("Теперь вводите текст для перевода с русского на английский.")
    await TranslateState.ToEnglish.set()

# Обработчик выбора "На русский"
@dp.message_handler(lambda message: message.text == "На русский", state='*')
async def set_to_russian(message: types.Message):
    await message.reply("Теперь вводите текст для перевода с английского на русский.")
    await TranslateState.ToRussian.set()

# Обработчик перевода на английский
@dp.message_handler(state=TranslateState.ToEnglish)
async def translate_to_english(message: types.Message):
    translator = Translator(to_lang="en", from_lang="ru")
    translation = translator.translate(message.text)
    await message.reply(f"Перевод на английский: {translation}")

# Обработчик перевода на русский
@dp.message_handler(state=TranslateState.ToRussian)
async def translate_to_russian(message: types.Message):
    translator = Translator(to_lang="ru", from_lang="en")
    translation = translator.translate(message.text)
    await message.reply(f"Перевод на русский: {translation}")

# Запуск бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
