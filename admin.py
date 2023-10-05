from telebot import types
import json
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
        else:
            return False, None
