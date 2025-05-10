import json
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor

BOT_TOKEN = '6403405667:AAEF8AQPPRDHyRkHQb-y3mjpLxpJ0odmofg' #@morfius_test2_bot
DATA_FILE = "files/clicker_data.json"

# Инициализация бота
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# Загрузка или создание JSON файла с данными пользователей
def load_data():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

# Начальные данные пользователя
DEFAULT_USER_DATA = {
    "balance": 0,
    "profit_per_click": 1,
    "upgrade_cost": 10
}

# Генерация реплай клавиатуры
def get_reply_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton("Вывести баланс"), KeyboardButton("Улучшить клик"))
    return keyboard

# Генерация инлайн клавиатуры для клика
def get_inline_keyboard():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("Клик", callback_data="click"))
    return keyboard

# Обработка команды /start
@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    user_id = str(message.from_user.id)
    data = load_data()

    # Если пользователь новый, добавляем его в базу
    if user_id not in data:
        data[user_id] = DEFAULT_USER_DATA.copy()
        save_data(data)

    await message.answer(
        "Добро пожаловать в кликер!", reply_markup=get_reply_keyboard()
    )
    await message.answer(
        f"Ваш текущий баланс: {data[user_id]['balance']}", reply_markup=get_inline_keyboard()
    )

# Обработка команды "Вывести баланс"
@dp.message_handler(lambda message: message.text == "Вывести баланс")
async def show_balance(message: types.Message):
    user_id = str(message.from_user.id)
    data = load_data()
    balance = data.get(user_id, DEFAULT_USER_DATA)["balance"]
    await message.answer(f"Ваш баланс: {balance}", reply_markup=get_inline_keyboard())

# Обработка команды "Улучшить клик"
@dp.message_handler(lambda message: message.text == "Улучшить клик")
async def upgrade_click(message: types.Message):
    user_id = str(message.from_user.id)
    data = load_data()

    user_data = data.get(user_id, DEFAULT_USER_DATA)
    if user_data["balance"] >= user_data["upgrade_cost"]:
        user_data["balance"] -= user_data["upgrade_cost"]
        user_data["profit_per_click"] += 1
        user_data["upgrade_cost"] *= 2
        data[user_id] = user_data
        save_data(data)
        await message.answer(
            f"Клик улучшен! Теперь вы получаете {user_data['profit_per_click']} за клик."
        )
    else:
        await message.answer("Недостаточно средств для улучшения клика!")

# Обработка клика по кнопке "Клик"
@dp.callback_query_handler(lambda callback_query: callback_query.data == "click")
async def handle_click(callback_query: types.CallbackQuery):
    user_id = str(callback_query.from_user.id)
    data = load_data()

    user_data = data.get(user_id, DEFAULT_USER_DATA)
    user_data["balance"] += user_data["profit_per_click"]
    data[user_id] = user_data
    save_data(data)

    await callback_query.message.edit_text(
        f"Ваш текущий баланс: {user_data['balance']}", reply_markup=get_inline_keyboard()
    )
    await callback_query.answer()

if __name__ == "__main__":
    executor.start_polling(dp)
