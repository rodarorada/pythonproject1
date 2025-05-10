from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils import executor

# Токен бота
BOT_TOKEN = '6403405667:AAEF8AQPPRDHyRkHQb-y3mjpLxpJ0odmofg' #@morfius_test2_bot

# Создание бота, диспетчера и хранилища состояний
bot = Bot(token=BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# Определение машины состояний
class Form(StatesGroup):
    waiting_for_name = State()
    waiting_for_age = State()

# Хэндлер команды /start
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply("Привет! Как тебя зовут?")
    await Form.waiting_for_name.set()  # Устанавливаем состояние

# Хэндлер для получения имени
@dp.message_handler(state=Form.waiting_for_name)
async def get_name(message: types.Message, state: FSMContext):
    name = message.text
    await state.update_data(name=name)  # Сохраняем имя в состоянии
    await message.reply(f"Приятно познакомиться, {name}! Сколько тебе лет?")
    await Form.waiting_for_age.set()  # Переходим к следующему состоянию

# Хэндлер для получения возраста
@dp.message_handler(state=Form.waiting_for_age)
async def get_age(message: types.Message, state: FSMContext):
    age = message.text
    if not age.isdigit():
        await message.reply("Пожалуйста, введи корректный возраст (число).")
        return
    await state.update_data(age=age)  # Сохраняем возраст
    data = await state.get_data()  # Получаем все данные
    name = data['name']
    await message.reply(f"Отлично, {name}! Тебе {age} лет.")
    await state.finish()  # Сбрасываем состояние

# Запуск бота
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
