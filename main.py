import telebot
import config
import admin
from lesson import LessonOutput
import os
from telebot import types
from handlers import SimpleUser

bot = telebot.TeleBot(config.BOT_TOKEN)

@bot.message_handler(commands=['start'])
def handle_start(message):
    SimpleUser.start(message, bot)

lesson_output = LessonOutput()

@bot.message_handler(content_types=['text'])
def handle_text_message(message):
    if message.text == '❓ Информация':
        SimpleUser.info(message, bot)
    elif message.text == '📚 Уроки сегодня':
        SimpleUser.lesson_day(message, bot, lesson_output)
print('Bot working...')
try:
    bot.polling(none_stop=True)
except Exception as e:
    print(f'Error: {e}')
print('Bot has finished its work...') 