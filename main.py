import random
from aiogram import Bot, Dispatcher, types, executor
from token_1 import token

bot = Bot(token=token)
dp = Dispatcher(bot)
random_number = random.randint(1, 3)
    
def generate_menu_keyboard():
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(types.KeyboardButton("Угадай число"))
        return keyboard

@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer("Здравствуйте! Этот бот создан GVNZO.", reply_markup=generate_menu_keyboard())

@dp.message_handler(text='Угадай число')
async def on_start(message: types.Message):
    global random_number
    random_number = random.randint(1, 3)
    await message.answer("Я загадал число от 1 до 3. Попробуйте угадать.")

@dp.message_handler(content_types=types.ContentType.TEXT)
async def check_number(message: types.Message):
    global random_number
    try:
        guessed_number = int(message.text)
        if guessed_number == random_number:
            await message.answer("Правильно! Вы угадали.")
            random_number = random.randint(1, 3)
            await message.answer("Спасибо за игру. До новых встреч.")
        else:
            await message.answer("Неправильно. Попробуйте еще раз.")
    except ValueError:
        await message.answer("Пожалуйста, введите число от 1 до 3.")

executor.start_polling(dp, skip_updates=True)