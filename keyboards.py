from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

button_send_contact = KeyboardButton("Отправить номер 📲", request_contact=True)
button_send_location = KeyboardButton("Отправить локацию 📍", request_location=True)
button_order_food = KeyboardButton(text="Заказать еду 🚀")

start_button = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(
    button_send_contact, button_send_location
).row(
    button_order_food
)