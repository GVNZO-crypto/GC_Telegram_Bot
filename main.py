from aiogram import Bot, Dispatcher, types, executor
from dotenv import load_dotenv
import os, time, logging

from keyboards import start_button
from database import cursor

load_dotenv('.env')

bot = Bot(token=str(os.environ.get('token')))
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands='start')
async def start(message: types.Message):
    user_id = message.from_user.id
    cursor.execute("SELECT * FROM users WHERE ID = ?", (user_id,))
    result = cursor.fetchall()
    print(result)
    if not result:
        first_name = message.from_user.first_name
        last_name = message.from_user.last_name
        username = message.from_user.username
        cursor.execute("INSERT INTO users (First_name, Last_name, Username, ID) VALUES (?, ?, ?, ?)",
                       (first_name, last_name, username, user_id))
        cursor.connection.commit()
    await message.answer(f"Здравствуйте, {message.from_user.full_name}!\nВас приветствует сервис доставки GVNZO_Food! 🛵\nДля совершения заказа вам необходимо предоставить нам информацию о вашем месторасположении и номер телефона для подтверждения заказа.\nНажмите на соответствующие кнопки в меню Бота 👇", reply_markup=start_button)


@dp.message_handler(content_types=types.ContentType.CONTACT)
async def process_contact(message: types.Message):
    user_id = message.from_user.id
    phone_number = message.contact.phone_number
    cursor.execute("UPDATE users SET Phone_number=? WHERE ID=?", (phone_number, user_id))
    cursor.connection.commit()
    await message.answer("Спасибо, ваш номер телефона успешно записан в базу данных!",reply_markup=start_button)


@dp.message_handler(content_types=types.ContentType.LOCATION)
async def process_location(message: types.Message):
    user_id = message.from_user.id
    address_longitude = message.location.longitude
    address_latitude = message.location.latitude
    cursor.execute("INSERT INTO address (ID, Address_longitude, Address_latitude) VALUES (?, ?, ?)",
                   (user_id, address_longitude, address_latitude))
    cursor.connection.commit()
    await message.answer("Спасибо, ваша локация успешно добавлена в базу данных!",reply_markup=start_button)


@dp.message_handler(text='Заказать еду 🚀')
async def order_food(message: types.Message):
    await message.answer("Введите название еды для заказа:\n 1. Поджаристый Python 🥩\n 2. Американский Javaгриль 🍗\n 3. Fullstack Гамбургер 🍔\n 4. UX пицца с UI дизайном 🍕")
    dp.register_message_handler(process_order_message)
async def process_order_message(message: types.Message):
    user_id = message.from_user.id
    title = message.text
    date_time_order = time.strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute("INSERT INTO orders (ID, Title, Address_destination, Date_time_order) "
                   "VALUES (?, ?, ?, ?)", (user_id, title, "г.Ош, ул.Мырзалы Аматова, 1Б стр, БЦ “Томирис”", date_time_order))
    cursor.connection.commit()
    await message.answer("Ваш заказ принят и будет обработан в ближайшее время.")

executor.start_polling(dp, skip_updates=True)

#Coding by GVNZO