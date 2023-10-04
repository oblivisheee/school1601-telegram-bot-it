from telebot import types
import datetime
import text
import schedule
import os
import json
import telebot
import config
import white_list
bot = telebot.TeleBot(config.BOT_TOKEN)



class SimpleUser:
    @staticmethod
    def start(message, bot, greeting=True):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("📚 Уроки сегодня")
        btn2 = types.KeyboardButton("❓ Информация")
        btn3 = types.KeyboardButton("⚙️ Настройки")
        markup.add(btn1, btn2, btn3)
        if greeting == True:
            bot.send_message(message.chat.id, text=text.START_GREETING, reply_markup=markup)
        elif greeting == False:
            bot.send_message(message.chat.id, text='Главное меню.', reply_markup=markup)           
    @staticmethod
    def info(message, bot):
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("Связь с создателем.", url='https://t.me/oblivisheee')
        markup.add(button1)
        bot.send_message(message.chat.id, text=text.INFO_BOT.format(message.from_user), reply_markup=markup)
    @staticmethod
    def lesson_day(message, bot, lesson_output):
            print('Does not working.')
    @staticmethod
    def choose_group(message, bot):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("1")
        btn2 = types.KeyboardButton("2")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, text.GROUP_CHOOSE, reply_markup=markup)
        # Update the 'choosing_group' flag in the user data
        if not os.path.isfile('users_data.json'):
            with open('users_data.json', 'w') as json_file:
                json.dump([], json_file)
        with open('users_data.json', 'r+') as json_file:
            data = json.load(json_file)
            for item in data:
                if item['username'] == message.from_user.username and item['user_id'] == message.from_user.id:
                    item['choosing_group'] = True
                    break
            else:
                data.append({
                    'username': message.from_user.username,
                    'user_id': message.from_user.id,
                    'choosing_group': True
                })
            json_file.seek(0)
            json_file.truncate()
            json.dump(data, json_file)

    @staticmethod
    def group_choice(message, bot):
        if message.text == '1' or message.text == '2':
            with open('users_data.json', 'r+') as json_file:
                data = json.load(json_file)
                for item in data:
                    if item['username'] == message.from_user.username and item['user_id'] == message.from_user.id:
                        if item.get('choosing_group', False):
                            item['group_choice'] = message.text
                            item['choosing_group'] = False  # Reset the flag
                            bot.send_message(message.chat.id, text.GROUP_CHOOSE_CHOICES[message.text])
                            SimpleUser.start(message, bot, greeting=False)  # Return to main menu
                            break
                json_file.seek(0)
                json.dump(data, json_file)
        else:
            bot.send_message(message.chat.id, text.GROUP_CHOOSE)
def update_today():
    today = datetime.datetime.now().strftime('%A').lower()
    return today


schedule.every().day.at("00:00").do(update_today)

import threading

thread = threading.Thread(target=lambda: schedule.every(30).seconds.do(lambda: None))
thread.start()