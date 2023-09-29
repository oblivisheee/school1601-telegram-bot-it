from telebot import types
import datetime
import text
import schedule  
admin_usernames = {
    'oblivisheee': '1493358684',
    'Nikita Gennadyevich': '5752567293',
    'Batyaband': '1176689897',
    'LoxKoroche1234567383': ''
}

admin_tokens = {
    '9galhmt62bu4f90dn58s0n46vb35fds': 'oblivisheee',
    '7gf5hdfeuies602meu1nsf25pa91dfe': 'Nikita Gennadyevich',
    'as5fad65gadsaafd7312fabjgwry312': 'Batyaband',
    'gafafg6NB144H17ds0432nfsd988112': 'LoxKoroche1234567383'
}

def admin_token_check(input_token: str):
    if input_token in admin_tokens:
        admin_username = admin_tokens[input_token]
        if admin_username in admin_usernames:
            print(f"Successfully logged in as admin: {admin_username} with ID: {admin_usernames[admin_username]}.\nLink to profile: https://t.me/{admin_username.replace(' ', '')}")
            return True, admin_usernames[admin_username]
    return False, None


class HeadMan():
    def check_token(input_token):
            if admin_token_check in admin_tokens:
                admin_username = admin_tokens[input_token]
                if admin_username in admin_usernames:
                    print(f"Successfully logged in as admin: {admin_username} with ID: {admin_usernames[admin_username]}.\nLink to profile: https://t.me/{admin_username.replace(' ', '')}")
                    return True, admin_usernames[admin_username]
            return False, None
    def start(message, bot):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("📚 Уроки сегодня")
        btn2 = types.KeyboardButton("❓ Информация")
        btn3 = types.KeyboardButton("😱 Список отсуствующих")
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, text=text.START_GREETING, reply_markup=markup)

    def info(message, bot):
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("Связь с создателем.", url='https://t.me/oblivisheee')
        markup.add(button1)
        bot.send_message(message.chat.id, text=text.INFO_BOT.format(message.from_user), reply_markup=markup)

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
    def managerPeople(bot, message):
        if message.text == '😱 Список отсуствующих':
            bot.send_message(message.chat.id, text.PEOPLE_WHOSE_IS_NO)

def update_today():
    today = datetime.datetime.now().strftime('%A').lower()
    return today

schedule.every().day.at("00:00").do(update_today)

import threading
thread = threading.Thread(target=lambda: schedule.every(1).seconds.do(lambda: None))
thread.start()
        
    