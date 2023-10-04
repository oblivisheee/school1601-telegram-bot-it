import json
import os
import text

def check_user(id):
    if not os.path.exists('white_list.json'):
        with open('white_list.json', 'w') as json_file:
            json.dump([], json_file)
        print(text.localAttention.JSON_FILE_SUCCESS_MADE)
    with open('white_list.json', 'r') as json_file:
        data = json.load(json_file)
        for item in data:
            if item['user_id'] == id:
                return True
    return False

def add_user(id):
    if not check_user(id):
        if not os.path.exists('white_list.json'):
            with open('white_list.json', 'w') as json_file:
                json.dump([], json_file)
            print(text.localAttention.JSON_FILE_SUCCESS_MADE)
        with open('white_list.json', 'r+') as json_file:
            data = json.load(json_file)
            data.append({'user_id': id})
            json_file.seek(0)
            json.dump(data, json_file)
            json_file.truncate()