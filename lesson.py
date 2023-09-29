import json
import os
import datetime
import text
day_mapping_cor = text.DAY_MAPPING_CORRECTED
class ScheduleManager:
    def __init__(self):
        self.schedule = self.load_schedule()

    def load_schedule(self):
        if os.path.isfile("schedule.json"):
            with open("schedule.json", "r") as json_file:
                return json.load(json_file)
        else:
            return {
                 "понедельник": [
                    {"урок 1": "Разговоры о важном", "время": "8:30-9:10"},
                    {"урок 2": "Инженерный практикум", "время": "9:30-10:10"},
                    {"урок 3": "Физика", "время": "10:30-11:10"},
                    {"урок 4": "Вероятность и статистика", "время": "11:30-12:10"},
                    {"урок 5": "Английский язык", "время": "12:30-13:10"},
                    {"урок 6": "Алгебра", "время": "13:30-14:10"},
                    {"урок 7": "История", "время": "14:30-15:10"},
                    {"урок 8": "Литература", "время": "15:30-16:10"},
                ],
                "вторник": [
                    {"урок 1": "Русский язык", "время": "8:30-9:10"},
                    {"урок 2": "Информатика", "время": "9:30-10:10"},
                    {"урок 3": "История", "время": "10:30-11:10"},
                    {"урок 4": "Алгебра", "время": "11:30-12:10"},
                    {"урок 5": "География", "время": "12:30-13:10"},
                    {"урок 6": "Русский язык", "время": "13:30-14:10"},
                    {"урок 7": "Физическая культура", "время": "14:30-15:10"},
                ],
                "среда": [
                    {"урок 1": "Русский язык", "время": "8:30-9:10"},
                    {"урок 2": "Литература", "время": "9:30-10:10"},
                    {"урок 3": "Геометрия", "время": "10:30-11:10"},
                    {"урок 4": "Классный час", "время": "11:30-12:10"},
                    {"урок 5": "География", "время": "12:30-13:10"},
                    {"урок 6": "Алгебра", "время": "13:30-14:10"},
                    {"урок 7": "Аддитивные технологии", "время": "14:30-15:10"},
                ],
                "четверг": [
                    {"урок 1": "Английский язык", "время": "8:30-9:10"},
                    {"урок 2": "Биология", "время": "9:30-10:10"},
                    {"урок 3": "Геометрия", "время": "10:30-11:10"},
                    {"урок 4": "Физика", "время": "11:30-12:10"},
                    {"урок 5": "Физическая культура", "время": "12:30-13:10"},
                    {"урок 6": "Технология", "время": "13:30-14:10"},
                    {"урок 7": "Обществознание", "время": "14:30-15:10"},
                    {"урок 8": "Информатика", "время": "15:30-16:10"},
                ],
                "пятница": [
                    {"урок 1": "Физика", "время": "8:30-9:10"},
                    {"урок 2": "Программирование", "время": "9:30-10:10"},
                    {"урок 3": "Английский язык", "время": "10:30-11:10"},
                    {"урок 4": "Русский язык", "время": "11:30-12:10"},
                    {"урок 5": "Алгебра", "время": "12:30-13:10"},
                    {"урок 6": "Технология", "время": "13:30-14:10"},
                    {"урок 7": "Английский", "время": "14:30-15:10"},
                ],
            }

    def add_homework(self, day, lesson, homework, time):
        if day in self.schedule:
            self.schedule[day].append({"урок": lesson, "дз": homework, "время": time})
        else:
            self.schedule[day] = [{"урок": lesson, "дз": homework, "время": time}]

    def save_schedule(self):
        with open("schedule.json", "w") as json_file:
            json.dump(self.schedule, json_file, indent=4, ensure_ascii=False)

class LessonNotificator:
    def __init__(self):
        print('Lesson notifications initialized.')

    def send_notification(self, lesson):
        print(f"Notification: It's time for {lesson}.")

class LessonOutput:
    def __init__(self):
        self.schedule_manager = ScheduleManager()
        if not os.path.isfile('schedule.json'):
            self.schedule_manager.save_schedule()

    def get_today_schedule(self):
        today = datetime.datetime.now().strftime('%A').lower()
        if today == 'saturday' or today == 'sunday':
            return "Today is a weekend, no lessons."
        if today in day_mapping_cor and day_mapping_cor[today] in self.schedule_manager.schedule:
            today_schedule = self.schedule_manager.schedule[day_mapping_cor[today]]
            # Replace lesson names with their numbers
            for i, lesson in enumerate(today_schedule, start=1):
                lesson["урок"] = f"Урок {i}"
            return today_schedule
        else:
            return "No schedule for today."