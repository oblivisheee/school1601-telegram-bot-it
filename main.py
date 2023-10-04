import telebot
import config
from telebot import types
from handlers import SimpleUser
import white_list
import text
bot = telebot.TeleBot(config.BOT_TOKEN)

@bot.message_handler(commands=['start'])
def handle_start(message):
    if white_list.check_user(id=message.from_user.id) == True:
        SimpleUser.start(message, bot)
    else:
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("Написать администратору.", url='https://t.me/oblivisheee')
        markup.add(button1)
        bot.send_message(message.chat.id, text.YOU_ARE_NOT_AUTHORIZED.format(message.from_user), reply_markup=markup)

"""lesson_output = 'test'()"""

"""elif message.text == '📚 Уроки сегодня':
        SimpleUser.lesson_day(message, bot)"""

@bot.message_handler(content_types=['text'])
def handle_text_message(message):
    if white_list.check_user(id=message.from_user.id) == True:
        if message.text == '❓ Информация':
            SimpleUser.info(message, bot)

        elif message.text == '⚙️ Настройки':
            SimpleUser.choose_group(message, bot)
        elif message.text in ['1', '2']:
            SimpleUser.group_choice(message, bot)
    else:
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("Написать администратору.", url='https://t.me/oblivisheee')
        markup.add(button1)
        bot.send_message(message.chat.id, text.YOU_ARE_NOT_AUTHORIZED.format(message.from_user), reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data in ['1', '2']:
            SimpleUser.group_choice(call.message, bot)

print('Bot working...')
bot.polling(non_stop=True)
print('Bot stopped...')