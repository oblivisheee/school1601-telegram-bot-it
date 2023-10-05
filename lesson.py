import json
import os
import datetime
import text

class ScheduleManager:
    def __init__(self, user_id):
        self.user_id = user_id
        self.schedule = self.load_schedule()

    def load_schedule(self):
        if os.path.isfile(f"{self.user_id}_schedule.json"):
            with open(f"{self.user_id}_schedule.json", "r") as json_file:
                return json.load(json_file)
        else:
            return {}

    def save_schedule(self):
        with open(f"{self.user_id}_schedule.json", "w") as json_file:
            json.dump(self.schedule, json_file, indent=4, ensure_ascii=False)

class LessonOutput:
    def __init__(self, user_id):
        self.schedule_manager = ScheduleManager(user_id)
        if not os.path.isfile(f'{user_id}_schedule.json'):
            self.schedule_manager.save_schedule()

    def get_today_schedule(self):
        today = datetime.datetime.now().strftime('%A').lower()
        if today == 'saturday' or today == 'sunday':
            return "Сегодня выходной, уроков нет."
        if today in text.DAY_MAPPING_NON_CORRECTED and text.DAY_MAPPING_NON_CORRECTED[today] in self.schedule_manager.schedule:
            today_schedule = self.schedule_manager.schedule[text.DAY_MAPPING_NON_CORRECTED[today]]
            for i, lesson in enumerate(today_schedule, start=1):
                lesson["урок"] = f"Урок {i}"
            return today_schedule
        else:
            return "На сегодня нет расписания."
