import telebot
import json

bot = telebot.TeleBot('6424132062:AAFrP6sJdsl1zYaPOR6O_swC18hWeYU5hdM')

# Создаем пустой словарь для хранения информации о пользователях
users_data = {}

# Функция для сохранения данных в JSON-файл
def save_data_to_json(data):
    with open('users_data.json', 'w') as file:
        json.dump(data, file, indent=4)

@bot.message_handler(commands=['start'])
def start(message):
    # Получаем информацию о пользователе
    user_id = message.from_user.id
    username = message.from_user.username

    # Проверяем, есть ли пользователь уже в базе данных
    if username not in users_data:
        # Если пользователя нет, добавляем его
        users_data[username] = user_id
        save_data_to_json(users_data)
        bot.send_message(message.chat.id, f'Привет, {username}! Твои данные сохранены в базе, в скором времени ты будешь включен в доступ к боту.')
    else:
        # Если пользователь уже есть, отправляем сообщение
        bot.send_message(message.chat.id, f'Привет, {username}! Твой ID уже сохранен.')
print('Bot working...')
bot.polling(non_stop=True)
