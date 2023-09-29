from telebot import types
import datetime
import text
import schedule


class SimpleUser:
    @staticmethod
    def start(message, bot):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("📚 Уроки сегодня")
        btn2 = types.KeyboardButton("❓ Информация")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, text=text.START_GREETING, reply_markup=markup)

    @staticmethod
    def info(message, bot):
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("Связь с создателем.", url='https://t.me/oblivisheee')
        markup.add(button1)
        bot.send_message(message.chat.id, text=text.INFO_BOT.format(message.from_user), reply_markup=markup)

    @staticmethod
    def lesson_day(message, bot, lesson_output):
        today_schedule = lesson_output.get_today_schedule()
        if isinstance(today_schedule, list):
            if today_schedule:
                schedule_message = f"Расписание на {text.DAY_MAPPING_CORRECTED[datetime.datetime.now().strftime('%A').lower()]}:\n"
                for lesson in today_schedule:
                    lesson_number = lesson.get('урок', 'Урок не найден').split()[-1]
                    lesson_name = lesson.get(f"урок {lesson_number}", 'Урок не найден')
                    schedule_message += f"Урок {lesson_number}: {lesson_name} ({lesson['время']})\n"
                bot.send_message(message.chat.id, schedule_message)
            else:
                bot.send_message(message.chat.id, "Уроки не были найдены.")
        else:
            bot.send_message(message.chat.id, text.ERROR_LESSON_NOT_FOUND)


def update_today():
    today = datetime.datetime.now().strftime('%A').lower()
    return today


schedule.every().day.at("00:00").do(update_today)

import threading

thread = threading.Thread(target=lambda: schedule.every(1).seconds.do(lambda: None))
thread.start()