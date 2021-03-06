from telebot import types
import telebot
import time
import re
from PIL import Image
import datetime
import threading
import json
import requests
import pickle

token = "1427693199:AAGnuGWcgwUy5tLlE7_GKyomLCHKY_T5mZI"
bot = telebot.TeleBot(token=token)
bot_id = 1427693199
difference_time = 0


class UserInBot:
    def __init__(self, user_id):
        self.__user_id = user_id
        self.__can_change = False
        self.__can_change_words = False
        self.__can_change_buttons = False
        self.__can_change_welcome_text = False
        self.__can_change_sleep_text = False
        self.__can_change_sleep_time = False
        self.__can_change_photo = False
        self.__can_change_gif = False
        self.__can_change_button_time = False
        self.__can_change_time_banned = False
        self.__can_change_group_banned = False
        self.__can_change_friend_banned = False
        self.__can_change_amount_symbols = False
        self.__can_change_amount_photo = False
        self.__can_change_amount_posts = False
        self.__number_chat = 0

    def get_user_id(self):
        return self.__user_id

    def get_can_change(self):
        return self.__can_change

    def set_can_change(self, can_change):
        self.__can_change = can_change

    def get_can_change_words(self):
        return self.__can_change_words

    def set_can_change_words(self, can_change_words):
        self.__can_change_words = can_change_words

    def get_can_change_time_banned(self):
        return self.__can_change_time_banned

    def set_can_change_time_banned(self, can_change_time_banned):
        self.__can_change_time_banned = can_change_time_banned

    def get_can_change_group_banned(self):
        return self.__can_change_group_banned

    def set_can_change_group_banned(self, can_change_group_banned):
        self.__can_change_group_banned = can_change_group_banned

    def get_can_change_friend_banned(self):
        return self.__can_change_friend_banned

    def set_can_change_friend_banned(self, can_change_friend_banned):
        self.__can_change_friend_banned = can_change_friend_banned

    def get_can_change_sleep_time(self):
        return self.__can_change_sleep_time

    def set_can_change_sleep_time(self, can_change_sleep_time):
        self.__can_change_sleep_time = can_change_sleep_time

    def get_can_change_buttons(self):
        return self.__can_change_buttons

    def set_can_change_buttons(self, can_change_buttons):
        self.__can_change_buttons = can_change_buttons

    def set_can_change_photo(self, can_change_photo):
        self.__can_change_photo = can_change_photo

    def get_can_change_photo(self):
        return self.__can_change_photo

    def set_can_change_gif(self, can_change_gif):
        self.__can_change_gif = can_change_gif

    def get_can_change_gif(self):
        return self.__can_change_gif

    def get_can_change_welcome_text(self):
        return self.__can_change_welcome_text

    def set_can_change_welcome_text(self, can_change_welcome_text):
        self.__can_change_welcome_text = can_change_welcome_text

    def get_can_change_sleep_text(self):
        return self.__can_change_sleep_text

    def set_can_change_sleep_text(self, can_change_sleep_text):
        self.__can_change_sleep_text = can_change_sleep_text

    def get_can_change_button_time(self):
        return self.__can_change_button_time

    def set_can_change_button_time(self, can_change_button_time):
        self.__can_change_button_time = can_change_button_time

    def get_can_change_amount_symbols(self):
        return self.__can_change_amount_symbols

    def set_can_change_amount_symbols(self, can_change_amount_symbols):
        self.__can_change_amount_symbols = can_change_amount_symbols

    def get_can_change_amount_photo(self):
        return self.__can_change_amount_photo

    def set_can_change_amount_photo(self, can_change_amount_photo):
        self.__can_change_amount_photo = can_change_amount_photo

    def get_can_change_amount_posts(self):
        return self.__can_change_amount_posts

    def set_can_change_amount_posts(self, can_change_amount_posts):
        self.__can_change_amount_posts = can_change_amount_posts

    def get_number_chat(self):
        return self.__number_chat

    def set_number_chat(self, number_chat):
        self.__number_chat = number_chat


class UserAdmin:
    def __init__(self, user_id):
        self.__user_id = user_id
        self.__can_input_chat = False
        self.__can_input_chat_del = False
        self.__inputted_chat = 0
        self.__inputted_del_chat = 0

    def set_can_input_chat(self, can_input_chat):
        self.__can_input_chat = can_input_chat

    def get_can_input_chat(self):
        return self.__can_input_chat

    def set_can_input_chat_del(self, can_input_chat_del):
        self.__can_input_chat_del = can_input_chat_del

    def get_can_input_chat_del(self):
        return self.__can_input_chat_del

    def set_inputted_chat(self, inputted_chat):
        self.__inputted_chat = inputted_chat

    def get_inputted_chat(self):
        return self.__inputted_chat

    def set_inputted_del_chat(self, inputted_del_chat):
        self.__inputted_del_chat = inputted_del_chat

    def get_inputted_del_chat(self):
        return self.__inputted_del_chat

    def get_user_id(self):
        return self.__user_id


yura = UserAdmin(443109443)
serg = UserAdmin(391152196)


class UserInChat:
    def __init__(self, user_id):
        self.__user_id = user_id
        self.__time_of_ban = 0
        self.__when_banned = 0
        self.__is_time_banned = False
        self.__is_group_banned = False
        self.__is_friend_banned = False
        self.__is_sleep_banned = False
        self.__is_posts_banned = False
        self.__posts_count = 0
        self.__violation = 0
        self.__when_posted = []
        self.__friends_count = 0
        self.__invited_friends = []

    def get_user_id(self):
        return self.__user_id

    def get_time_of_ban(self):
        return self.__time_of_ban

    def set_time_of_ban(self, time_of_ban):
        self.__time_of_ban = time_of_ban

    def get_when_banned(self):
        return self.__when_banned

    def set_when_banned(self, when_banned):
        self.__when_banned = when_banned

    def set_is_time_banned(self, is_time_banned):
        self.__is_time_banned = is_time_banned

    def get_is_time_banned(self):
        return self.__is_time_banned

    def set_is_group_banned(self, is_group_banned):
        self.__is_group_banned = is_group_banned

    def get_is_group_banned(self):
        return self.__is_group_banned

    def set_is_friend_banned(self, is_friend_banned):
        self.__is_friend_banned = is_friend_banned

    def get_is_friend_banned(self):
        return self.__is_friend_banned

    def set_is_sleep_banned(self, is_sleep_banned):
        self.__is_sleep_banned = is_sleep_banned

    def get_is_sleep_banned(self):
        return self.__is_sleep_banned

    def set_is_posts_banned(self, is_posts_banned):
        self.__is_posts_banned = is_posts_banned

    def get_is_posts_banned(self):
        return self.__is_posts_banned

    def set_friends_count(self, friends_count):
        self.__friends_count = friends_count

    def get_friends_count(self):
        return self.__friends_count

    def set_posts_count(self, posts_count):
        self.__posts_count = posts_count

    def get_posts_count(self):
        return self.__posts_count

    def set_when_posted(self, when_posted):
        self.__when_posted = when_posted

    def get_when_posted(self):
        return self.__when_posted

    def set_violation(self, violation):
        self.__violation = violation

    def get_violation(self):
        return self.__violation

    def add_when_posted(self, when_posted):
        self.__when_posted.append(when_posted)

    def add_invited_friends(self, friend):
        self.__invited_friends.append(friend)

    def get_invited_friends(self):
        return self.__invited_friends


class Chat:
    def __init__(self, owner_id, chat_id):
        self.__owner_id = owner_id
        self.__chat_id = chat_id
        self.__banned_words = []
        self.__buttons = []
        self.__links = True
        self.__forward = True
        self.__welcome = False
        self.__welcome_text = "Добро пожаловать"
        self.__welcome_photo = False
        self.__welcome_gif = False
        self.__buttons_new = False
        self.__buttons_time = 0
        self.__when_posted_button = 0
        self.__amount_photos = 0
        self.__amount_symbols = 0
        self.__amount_posts = 0
        self.__sleep_chat = False
        self.__sleep_time = []
        self.__sleep_text = "В чате нельзя писать"
        self.__banned_time = 0
        self.__banned_chanel = 0
        self.__banned_chanel_name = ""
        self.__banned_chanel_all = 0
        self.__banned_chanel_new = 0
        self.__banned_friend = 0
        self.__banned_friend_one = 0
        self.__banned_friend_one_new = 0
        self.__banned_friend_every = 0
        self.__previous_message = 0
        self.__previous_message_by_time = 0
        self.__previous_message_sleep = 0
        self.__previous_data = 0
        self.__previous_data_by_time = 0
        self.__users_in_chat = []
        self.__new_users_in_chat = []

    def get_owner_id(self):
        return self.__owner_id

    def get_chat_id(self):
        return self.__chat_id

    def set_banned_words(self, banned_words):
        self.__banned_words = banned_words

    def get_banned_words(self):
        return self.__banned_words

    def get_links(self):
        return self.__links

    def change_links(self):
        self.__links = not self.__links

    def get_forward(self):
        return self.__forward

    def change_forward(self):
        self.__forward = not self.__forward

    def get_welcome(self):
        return self.__welcome

    def change_welcome(self):
        self.__welcome = not self.__welcome

    def get_sleep_chat(self):
        return self.__sleep_chat

    def change_sleep_chat(self):
        self.__sleep_chat = not self.__sleep_chat

    def get_buttons_new(self):
        return self.__buttons_new

    def change_buttons_new(self):
        self.__buttons_new = not self.__buttons_new

    def get_buttons_time(self):
        return self.__buttons_time

    def set_buttons_time(self, buttons_time):
        self.__buttons_time = buttons_time

    def get_buttons(self):
        return self.__buttons

    def set_buttons(self, buttons):
        self.__buttons = buttons

    def get_welcome_photo(self):
        return self.__welcome_photo

    def set_welcome_photo(self, welcome_photo):
        self.__welcome_photo = welcome_photo

    def get_welcome_gif(self):
        return self.__welcome_gif

    def set_welcome_gif(self, welcome_gif):
        self.__welcome_gif = welcome_gif

    def get_sleep_time(self):
        return self.__sleep_time

    def set_sleep_time(self, sleep_time):
        self.__sleep_time = sleep_time

    def get_amount_photos(self):
        return self.__amount_photos

    def set_amount_photos(self, amount_photos):
        self.__amount_photos = amount_photos

    def get_amount_symbols(self):
        return self.__amount_symbols

    def set_amount_symbols(self, amount_symbols):
        self.__amount_symbols = amount_symbols

    def get_amount_posts(self):
        return self.__amount_posts

    def set_amount_posts(self, amount_posts):
        self.__amount_posts = amount_posts

    def get_users_in_chat(self):
        return self.__users_in_chat

    def set_users_in_chat(self, users_in_chat):
        self.__users_in_chat = users_in_chat

    def get_welcome_text(self):
        return self.__welcome_text

    def set_welcome_text(self, welcome_text):
        self.__welcome_text = welcome_text

    def get_sleep_text(self):
        return self.__sleep_text

    def set_sleep_text(self, sleep_text):
        self.__sleep_text = sleep_text

    def add_user_in_chat(self, user_id):
        self.__users_in_chat.append(UserInChat(user_id))

    def is_user_in_chat(self, user_id):
        for us in self.__users_in_chat:
            if us.get_user_id() == user_id:
                return True
        return False

    def set_when_posted_button(self, when_posted_button):
        self.__when_posted_button = when_posted_button

    def get_when_posted_button(self):
        return self.__when_posted_button

    def add_new_user_in_chat(self, user_id):
        self.__new_users_in_chat.append(user_id)

    def is_new_user_in_chat(self, user_id):
        return user_id in self.__new_users_in_chat

    def get_banned_time(self):
        return self.__banned_time

    def set_banned_time(self, banned_time):
        self.__banned_time = banned_time

    def get_banned_chanel(self):
        return self.__banned_chanel

    def set_banned_chanel(self, banned_chanel):
        self.__banned_chanel = banned_chanel

    def get_banned_chanel_name(self):
        return self.__banned_chanel_name

    def set_banned_chanel_name(self, banned_chanel_name):
        self.__banned_chanel_name = banned_chanel_name

    def get_banned_chanel_all(self):
        return self.__banned_chanel_all

    def set_banned_chanel_all(self, banned_chanel_all):
        self.__banned_chanel_all = banned_chanel_all

    def get_banned_chanel_new(self):
        return self.__banned_chanel_new

    def set_banned_chanel_new(self, banned_chanel_new):
        self.__banned_chanel_new = banned_chanel_new

    def get_banned_friend_one(self):
        return self.__banned_friend_one

    def set_banned_friend_one(self, banned_friend_one):
        self.__banned_friend_one = banned_friend_one

    def get_banned_friend_one_new(self):
        return self.__banned_friend_one_new

    def set_banned_friend_one_new(self, banned_friend_one_new):
        self.__banned_friend_one_new = banned_friend_one_new

    def get_banned_friend_every(self):
        return self.__banned_friend_every

    def set_banned_friend_every(self, banned_friend_every):
        self.__banned_friend_every = banned_friend_every

    def get_banned_friend(self):
        return self.__banned_friend

    def set_banned_friend(self, banned_friend):
        self.__banned_friend = banned_friend

    def get_previous_message(self):
        return self.__previous_message

    def set_previous_message(self, previous_message):
        self.__previous_message = previous_message

    def get_previous_message_by_time(self):
        return self.__previous_message_by_time

    def set_previous_message_by_time(self, previous_message_by_time):
        self.__previous_message_by_time = previous_message_by_time

    def get_previous_message_sleep(self):
        return self.__previous_message_sleep

    def set_previous_message_sleep(self, previous_message_sleep):
        self.__previous_message_sleep = previous_message_sleep

    def get_previous_data(self):
        return self.__previous_data

    def set_previous_data(self, previous_data):
        self.__previous_data = previous_data

    def get_previous_data_by_time(self):
        return self.__previous_data_by_time

    def set_previous_data_by_time(self, previous_data_by_time):
        self.__previous_data_by_time = previous_data_by_time


try:
    with open('users.pickle', 'rb') as f:
        users = pickle.load(f)
except Exception:
    users = []
    with open('users.pickle', 'wb') as f:
        pickle.dump(users, f)

try:
    with open('chats.pickle', 'rb') as f:
        chats = pickle.load(f)
except Exception:
    chats = []
    with open('chats.pickle', 'wb') as f:
        pickle.dump(chats, f)


def is_user(user_id):
    for us in users:
        if user_id == us.get_user_id():
            return True
    return False


def is_chat(chat_id):
    for chat in chats:
        if chat_id == chat.get_chat_id():
            return True
    return False


def cant_change(user_id):
    try:
        for us in users:
            if us.get_user_id() == user_id:
                us.set_can_change(False)
                us.set_can_change_words(False)
                us.set_can_change_buttons(False)
                us.set_can_change_welcome_text(False)
                us.set_can_change_sleep_text(False)
                us.set_can_change_sleep_time(False)
                us.set_can_change_photo(False)
                us.set_can_change_gif(False)
                us.set_can_change_button_time(False)
                us.set_can_change_time_banned(False)
                us.set_can_change_group_banned(False)
                us.set_can_change_friend_banned(False)
                us.set_can_change_amount_symbols(False)
                us.set_can_change_amount_photo(False)
                us.set_can_change_amount_posts(False)
    except Exception:
        pass


def get_user(user_id):
    counter = 0
    for us in users:
        if us.get_user_id() == user_id:
            return counter
        counter += 1


def get_chat(chat_id):
    chat_numb = 0
    for chat in chats:
        if chat.get_chat_id() == chat_id:
            return chat_numb
        chat_numb += 1


def chat_number(user_id):
    for us in users:
        if us.get_user_id() == user_id:
            chat_numb = us.get_number_chat()

    names = 0
    counter = -1
    for chat in chats:
        if chat_numb == names:
            return counter
        if chat.get_owner_id() == user_id:
            names += 1
        counter += 1
    if chat_numb == names:
        return counter


def get_buttons(buttons_lst):
    keyboard = types.InlineKeyboardMarkup()
    for row in buttons_lst:
        buts = []
        for el in row:
            but = el.split(": ")
            buts.append(types.InlineKeyboardButton(text=but[0], url=but[1]))
        keyboard.add(*[but for but in buts])
    return keyboard


def add_slash(string):
    counter = 0
    added = 0
    for i in string:
        if i == "." or i == "!" or i == "?":
            string = string[0:counter + added] + "\\" + string[counter + added:len(string)]
            added += 1
        counter += 1

    return  string


def delete_mes(chat_id, mes_id):
    old_time = time.time()
    while True:
        if time.time() - old_time > 15:
            bot.delete_message(chat_id, mes_id)
            break


def start_buttons():
    key = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton(text="Новости", callback_data="news")
    but_2 = types.InlineKeyboardButton(text="Поддержка", url="https://t.me/Sistems_Bot")
    but_3 = types.InlineKeyboardButton(text="Настройка чатов", callback_data="my_chats")
    but_4 = types.InlineKeyboardButton(text="Как пользоваться", callback_data="info")
    key.add(but_1, but_2)
    key.add(but_3, but_4)
    return key


def settings_buttons(chat_numb):
    if chats[chat_numb].get_links():
        link_txt = "(разрешены)"
    else:
        link_txt = "(запрещены)"

    if chats[chat_numb].get_forward():
        forward_txt = "(разрешены)"
    else:
        forward_txt = "(запрещены)"

    key = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton(text="Приветствие", callback_data="welcome")
    but_2 = types.InlineKeyboardButton(text="Кнопки под приветствием", callback_data="buttons")
    but_3 = types.InlineKeyboardButton(text="Запреты постить", callback_data="banned_user")
    but_4 = types.InlineKeyboardButton(text="Запрещенные слова", callback_data="banned_words")
    but_5 = types.InlineKeyboardButton(text="Ограничения в постах", callback_data="post_restrictions")
    but_6 = types.InlineKeyboardButton(text="Сон-чат, автомат по времени", callback_data="sleep_time")
    but_7 = types.InlineKeyboardButton(text="Ссылки" + link_txt, callback_data="url")
    but_8 = types.InlineKeyboardButton(text="Пересланные сообщения" + forward_txt, callback_data="forwarded")
    but_9 = types.InlineKeyboardButton(text="Назад", callback_data="start")
    key.add(but_1)
    key.add(but_2)
    key.add(but_3)
    key.add(but_5)
    key.add(but_6)
    key.add(but_4, but_7)
    key.add(but_8)
    key.add(but_9)
    return key


@bot.message_handler(commands=["admin"])
def admin(message):
    try:
        now = datetime.datetime.now()
        txt = str(now.hour) + " " + str(now.minute)
        bot.send_message(message.chat.id, txt, parse_mode='Markdown')
        cant_change(message.chat.id)
        if message.chat.id == 443109443 or message.chat.id == 391152196:
            try:
                bot.delete_message(message.chat.id, message.message_id)
            except Exception as e:
                pass

            key = types.InlineKeyboardMarkup()
            but_1 = types.InlineKeyboardButton(text="Посмотреть все чаты ",
                                               callback_data="show_chats")

            but_2 = types.InlineKeyboardButton(text="Удалить бота из группы ",
                                               callback_data="del_bot_input")
            key.add(but_1)
            key.add(but_2)

            bot.send_message(message.chat.id, "Выберите действие", reply_markup=key, parse_mode='Markdown')
    except Exception:
        pass


@bot.callback_query_handler(func=lambda call: call.data == "admin")
def admin(call):
    try:
        cant_change(call.message.chat.id)
        if call.message.chat.id == 443109443 or call.message.chat.id == 391152196:
            try:
                bot.delete_message(call.message.chat.id, call.message.message_id)
            except Exception as e:
                pass

            key = types.InlineKeyboardMarkup()
            but_1 = types.InlineKeyboardButton(text="Посмотреть все чаты ",
                                               callback_data="show_chats")

            but_2 = types.InlineKeyboardButton(text="Удалить бота из группы ",
                                               callback_data="del_bot_input")
            key.add(but_1)
            key.add(but_2)

            bot.send_message(call.message.chat.id, "Выберите действие", reply_markup=key, parse_mode='Markdown')
    except Exception:
        pass


@bot.callback_query_handler(func=lambda call: call.data == "show_chats")
def show_chats(call):
    try:
        try:
            bot.delete_message(call.message.chat.id, call.message.message_id)
        except Exception as e:
            pass

        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Детальнее про чат",
                                           callback_data="chat_details_input")
        but_2 = types.InlineKeyboardButton(text="Назад",
                                           callback_data="admin")

        key.add(but_1)
        key.add(but_2)
        names = []
        for chat in chats:
            try:
                if bot.get_chat(chat.get_chat_id()).username:
                    names.append("@"+bot.get_chat(chat.get_chat_id()).username)
                else:
                    names.append(bot.get_chat(chat.get_chat_id()).title)
            except Exception as e:
                print(e)

        text = ""
        for i in range(len(names)):
            text += str(i + 1) + ". " + names[i] + "\n"

        bot.send_message(call.message.chat.id, text, parse_mode='Markdown')
        bot.send_message(call.message.chat.id, "Выберите действие", reply_markup=key, parse_mode='Markdown')
    except Exception as e:
        print(e)


@bot.callback_query_handler(func=lambda call: call.data == "chat_details_input")
def chat_details_input(call):
    try:
        try:
            bot.delete_message(call.message.chat.id, call.message.message_id)
        except Exception as e:
            pass

        if call.from_user.id == 443109443:
            yura.set_can_input_chat(True)

        elif call.from_user.id == 391152196:
            serg.set_can_input_chat(True)

        bot.send_message(call.from_user.id, "Введите номер чата")
    except Exception as e:
        print(e)


@bot.callback_query_handler(func=lambda call: call.data == "chat_details")
def chat_details(call):
    try:
        try:
            bot.delete_message(call.message.chat.id, call.message.message_id)
        except Exception as e:
            pass

        if call.from_user.id == 443109443:
            inputted_chat = yura.get_inputted_chat()

        elif call.from_user.id == 391152196:
            inputted_chat = serg.get_inputted_chat()

        chat = chats[inputted_chat - 1]
        chat_info = bot.get_chat(chat.get_chat_id())
        chat_id = str(chat_info.id)
        chat_type = chat_info.type
        chat_title = chat_info.title
        chat_username = chat_info.username
        amount_members = str(bot.get_chat_members_count(chat.get_chat_id()))
        chat_admins = bot.get_chat_administrators(chat.get_chat_id())
        text_admins = ""
        for adm in chat_admins:
            text_admins += f"[{adm.user.first_name}](tg://user?id={str(adm.user.id)}) "

        text = f"Название чата: {chat_title}\nЮзернэйм чата: @{chat_username}\n" \
               f"Айди чата: {chat_id}\nТип чата: {chat_type}\nКоличество участников: {amount_members}\n" \
               f"Админы чата: {text_admins}"
        bot.send_message(call.from_user.id, text, parse_mode='Markdown')
    except Exception as e:
        print(e)


@bot.callback_query_handler(func=lambda call: call.data == "del_bot_input")
def del_bot_input(call):
    try:
        try:
            bot.delete_message(call.message.chat.id, call.message.message_id)
        except Exception as e:
            pass

        if call.from_user.id == 443109443:
            yura.set_can_input_chat_del(True)

        elif call.from_user.id == 391152196:
            serg.set_can_input_chat_del(True)

        bot.send_message(call.from_user.id, "Введите номер чата")
    except Exception as e:
        print(e)


@bot.callback_query_handler(func=lambda call: call.data == "del_bot")
def del_bot(call):
    try:
        try:
            bot.delete_message(call.message.chat.id, call.message.message_id)
        except Exception as e:
            pass

        if call.from_user.id == 443109443:
            inputted_chat = yura.get_inputted_del_chat()

        elif call.from_user.id == 391152196:
            inputted_chat = serg.get_inputted_del_chat()

        chat = chats[inputted_chat - 1]
        chat_info = bot.get_chat(chat.get_chat_id())
        chat_username = chat_info.username
        if chat_username:
            text = "@"+chat_username
        else:
            text = chat_info.title

        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Да",
                                           callback_data="yes_del_bot")
        but_2 = types.InlineKeyboardButton(text="Нет, назад",
                                           callback_data="admin")

        key.add(but_1)
        key.add(but_2)

        bot.send_message(call.from_user.id, "Желаете удалить этот чат? " + text, reply_markup=key)
    except Exception as e:
        print(e)


@bot.callback_query_handler(func=lambda call: call.data == "yes_del_bot")
def yes_del_bot(call):
    try:
        try:
            bot.delete_message(call.message.chat.id, call.message.message_id)
        except Exception as e:
            pass

        if call.from_user.id == 443109443:
            inputted_chat = yura.get_inputted_del_chat()

        elif call.from_user.id == 391152196:
            inputted_chat = serg.get_inputted_del_chat()

        chat = chats[inputted_chat - 1]
        bot.leave_chat(chat.get_chat_id())
        chats.remove(chat)
        bot.send_message(call.message.chat.id, "Бот был успешно удален из чата")
        admin(call)
    except Exception as e:
        print(e)


@bot.message_handler(commands=["start"])
def start(message):
    try:
        print(len(chats))
        cant_change(message.chat.id)
        with open('users.pickle', 'wb') as f:
            pickle.dump(users, f)

        with open('chats.pickle', 'wb') as f:
            pickle.dump(chats, f)

        if message.chat.id > 0:
            key = start_buttons()
            if not is_user(message.chat.id):
                name = f"[{message.from_user.first_name}](tg://user?id={str(message.chat.id)})"
                text = f"Добро пожаловать {name}, я бот для модерации чатов. " \
                       f"Помогаю управлять чатами, в том числе удалять спам ссылки," \
                       f" сообщения с нецензурной бранью и многое другое."
                users.append(UserInBot(message.chat.id))
            else:
                text = "Выберите действие"

            bot.send_message(message.chat.id, text, reply_markup=key, parse_mode='Markdown')
    except Exception as e:
        print(e)


@bot.callback_query_handler(func=lambda call: call.data == "start")
def start(call):
    try:
        cant_change(call.message.chat.id)
        if call.message.chat.id > 0:
            try:
                bot.delete_message(call.message.chat.id, call.message.message_id)
            except Exception as e:
                pass
            key = start_buttons()
            text = "Выберите действие"
            bot.send_message(call.from_user.id, text, reply_markup=key, parse_mode='Markdown')
    except Exception:
        pass


@bot.callback_query_handler(func=lambda call: call.data == "news")
def news(call):
    try:
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.from_user.id, "Пока что новостей нет.")
        start(call)
    except Exception:
        pass


@bot.callback_query_handler(func=lambda call: call.data == "info")
def info(call):
    try:
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.from_user.id, "Добавьте бота в свою группу (важно, для это должна быть супергруппа),"
                                            " повысьте его права"
                                            " до администратора, далее можете"
                                            " настроить бота (Настройка чатов)")
        start(call)
    except Exception:
        pass


@bot.callback_query_handler(func=lambda call: call.data == "my_chats")
def my_chats(call):
    try:
        names = []
        for chat in chats:
            if chat.get_owner_id() == call.from_user.id:
                if bot.get_chat(chat.get_chat_id()).username:
                    names.append("@" + bot.get_chat(chat.get_chat_id()).username)
                else:
                    names.append(bot.get_chat(chat.get_chat_id()).title)

        if not names:
            bot.send_message(call.from_user.id, "У вас нет чатов с ботом")
        else:
            try:
                bot.delete_message(call.message.chat.id, call.message.message_id)
            except Exception as e:
                pass

            number = get_user(call.from_user.id)
            users[number].set_can_change(True)
            txt = "Введите номер чата\n"
            for i in range(len(names)):
                txt += str(i + 1) + ". " + names[i] + "\n"
            bot.send_message(call.from_user.id, txt)
    except Exception as e:
        print(e)


@bot.message_handler(commands=[""])
def chat_settings(message):
    if message.chat.id > 0:
        try:
            chat_numb = chat_number(message.chat.id)
            key = settings_buttons(chat_numb)
            bot.send_message(message.chat.id, "Выберите действие", reply_markup=key, parse_mode='Markdown')
        except Exception as e:
            print(e)


@bot.callback_query_handler(func=lambda call: call.data == "chat_settings")
def chat_settings(call):
    try:
        try:
            bot.delete_message(call.message.chat.id, call.message.message_id)
        except Exception as e:
            pass
        chat_numb = chat_number(call.from_user.id)
        key = settings_buttons(chat_numb)
        bot.send_message(call.from_user.id, "Выберите действие", reply_markup=key, parse_mode='Markdown')
    except Exception:
        pass


@bot.callback_query_handler(func=lambda call: call.data == "banned_words")
def banned_words(call):
    try:
        try:
            bot.delete_message(call.message.chat.id, call.message.message_id)
        except Exception as e:
            pass
        chat_numb = chat_number(call.from_user.id)
        banned_w = chats[chat_numb].get_banned_words()
        if banned_w:
            bot.send_message(call.from_user.id, "Запрещённые слова: " + ", ".join(banned_w))
        else:
            bot.send_message(call.from_user.id, "Запрещённых слов нет")

        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Изменить запрещённые слова", callback_data="change_banned_words")
        but_2 = types.InlineKeyboardButton(text="Назад", callback_data="chat_settings")
        key.add(but_1)
        key.add(but_2)
        bot.send_message(call.from_user.id, "Выберите действие", reply_markup=key, parse_mode='Markdown')
    except Exception:
        pass


@bot.callback_query_handler(func=lambda call: call.data == "change_banned_words")
def change_banned_words(call):
    try:
        try:
            bot.delete_message(call.message.chat.id, call.message.message_id)
        except Exception as e:
            pass
        number = get_user(call.from_user.id)
        users[number].set_can_change_words(True)
        bot.send_message(call.from_user.id, "👉 Введите запрещённые слова или фразы через запятую с "
                                            "пробелом. Например: один, дважды два, триста тридцать три, 📌 ВНИМАНИЕ!"
                                            " Запятая и пробел обязательны после каждого слова или предложения.")
    except Exception:
        pass


@bot.callback_query_handler(func=lambda call: call.data == "url")
def url(call):
    try:
        try:
            bot.delete_message(call.message.chat.id, call.message.message_id)
        except Exception as e:
            pass
        chat_numb = chat_number(call.from_user.id)
        chats[chat_numb].change_links()
        chat_settings(call)
    except Exception:
        pass


@bot.callback_query_handler(func=lambda call: call.data == "forwarded")
def forwarded(call):
    try:
        try:
            bot.delete_message(call.message.chat.id, call.message.message_id)
        except Exception as e:
            pass
        chat_numb = chat_number(call.from_user.id)
        chats[chat_numb].change_forward()
        chat_settings(call)
    except Exception:
        pass


@bot.callback_query_handler(func=lambda call: call.data == "banned_user")
def banned_user(call):
    try:
        try:
            bot.delete_message(call.message.chat.id, call.message.message_id)
        except Exception as e:
            pass
        key = types.InlineKeyboardMarkup()
        chat_numb = chat_number(call.from_user.id)
        if chats[chat_numb].get_banned_time() == 0:
            banned_time_txt = "(нет)"
        else:
            banned_time_txt = f"({chats[chat_numb].get_banned_time()} минут)"

        if chats[chat_numb].get_banned_chanel_name() == "":
            banned_chanel_txt = "(нет)"
        else:
            banned_chanel_txt = f"(@{chats[chat_numb].get_banned_chanel_name()})"

        if chats[chat_numb].get_banned_friend() == 0:
            banned_friend_txt = "(нет)"
        else:
            banned_friend_txt = f"({chats[chat_numb].get_banned_friend()} чел.)"
        but_1 = types.InlineKeyboardButton(text="Запрет писать первое время " + banned_time_txt,
                                           callback_data="banned_by_time")

        but_2 = types.InlineKeyboardButton(text="Запрет писать если не в канале " + banned_chanel_txt,
                                           callback_data="banned_by_chanel")

        but_3 = types.InlineKeyboardButton(text="Запрет писать если не добавил друга" + banned_friend_txt,
                                           callback_data="banned_by_friend")

        but_4 = types.InlineKeyboardButton(text="Назад", callback_data="chat_settings")
        key.add(but_1)
        key.add(but_2)
        key.add(but_3)
        key.add(but_4)
        bot.send_message(call.from_user.id, "Выберите действие", reply_markup=key, parse_mode='Markdown')
    except Exception:
        pass


@bot.callback_query_handler(func=lambda call: call.data == "banned_by_time")
def banned_by_time(call):
    try:
        try:
            bot.delete_message(call.message.chat.id, call.message.message_id)
        except Exception as e:
            pass
        key = types.InlineKeyboardMarkup()
        chat_numb = chat_number(call.from_user.id)
        if chats[chat_numb].get_banned_time() == 0:
            bot.send_message(call.from_user.id, "(Сейчас нет времени запрета писать)")
        else:
            bot.send_message(call.from_user.id, f"(Время запрета писать - {chats[chat_numb].get_banned_time()} минут)")
        but_1 = types.InlineKeyboardButton(text="Изменить время запрета",
                                           callback_data="banned_time_change")

        but_2 = types.InlineKeyboardButton(text="Назад", callback_data="banned_user")
        key.add(but_1)
        key.add(but_2)
        bot.send_message(call.from_user.id, "Выберите действие", reply_markup=key, parse_mode='Markdown')
    except Exception:
        pass


@bot.callback_query_handler(func=lambda call: call.data == "banned_time_change")
def banned_time_change(call):
    try:
        try:
            bot.delete_message(call.message.chat.id, call.message.message_id)
        except Exception as e:
            pass
        number = get_user(call.from_user.id)
        users[number].set_can_change_time_banned(True)
        bot.send_message(call.from_user.id, "👉 Введите время (в минутах, цифрами) сколько нельзя писать новым "
                                            "участники группы. Например, цифра 1, или 30, или 120 ")
    except Exception:
        pass


@bot.callback_query_handler(func=lambda call: call.data == "banned_by_chanel")
def banned_by_chanel(call):
    try:
        try:
            bot.delete_message(call.message.chat.id, call.message.message_id)
        except Exception as e:
            pass

        chat_numb = chat_number(call.from_user.id)

        if chats[chat_numb].get_banned_chanel_new() != 0 and chats[chat_numb].get_banned_chanel() != 0:
            banned_chanel_txt = "(включено)"
        else:
            banned_chanel_txt = "(выключено)"

        if chats[chat_numb].get_banned_chanel_all() != 0 and chats[chat_numb].get_banned_chanel() != 0:
            banned_friend_txt = "(включено)"
        else:
            banned_friend_txt = "(выключено)"

        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Применять ко всем участникам" + banned_friend_txt, callback_data="banned_chanel_all")
        but_2 = types.InlineKeyboardButton(text="Применять только к новым участникам" + banned_chanel_txt, callback_data="banned_chanel_new")
        if chats[chat_numb].get_banned_chanel() != 0:
            key.add(types.InlineKeyboardButton(text="Выключить", callback_data="off_chanel"))

        but_3 = types.InlineKeyboardButton(text="Назад", callback_data="banned_user")
        key.add(but_1)
        key.add(but_2)
        key.add(but_3)
        bot.send_message(call.from_user.id, "Выберите действие", reply_markup=key, parse_mode='Markdown')
    except Exception:
        pass


@bot.callback_query_handler(func=lambda call: call.data == "banned_chanel_all")
def banned_chanel_all(call):
    try:
        try:
            bot.delete_message(call.message.chat.id, call.message.message_id)
        except Exception as e:
            pass
        number = get_user(call.from_user.id)
        users[number].set_can_change_group_banned(True)
        chat_numb = chat_number(call.from_user.id)
        chats[chat_numb].set_banned_chanel_new(0)
        chats[chat_numb].set_banned_chanel_all(1)
        bot.send_message(call.from_user.id, "👉 Добавьте бота в канал администратором со всеми правами и после "
                                            "этого перешлите боту любой пост (с текстом) из канала")
    except Exception:
        pass


@bot.callback_query_handler(func=lambda call: call.data == "banned_chanel_new")
def banned_chanel_new(call):
    try:
        try:
            bot.delete_message(call.message.chat.id, call.message.message_id)
        except Exception as e:
            pass
        number = get_user(call.from_user.id)
        users[number].set_can_change_group_banned(True)
        chat_numb = chat_number(call.from_user.id)
        chats[chat_numb].set_banned_chanel_new(1)
        chats[chat_numb].set_banned_chanel_all(0)
        bot.send_message(call.from_user.id, "Добавьте бота в канал и после этого парешлите "
                                            "боту любой пост с канала где есть текст.")
    except Exception:
        pass


@bot.callback_query_handler(func=lambda call: call.data == "off_chanel")
def off_chanel(call):
    try:
        try:
            bot.delete_message(call.message.chat.id, call.message.message_id)
        except Exception as e:
            pass
        chat_numb = chat_number(call.from_user.id)
        chats[chat_numb].set_banned_chanel_new(0)
        chats[chat_numb].set_banned_chanel_all(0)
        chats[chat_numb].set_banned_chanel(0)
        banned_by_chanel(call)

    except Exception:
        pass


@bot.callback_query_handler(func=lambda call: call.data == "banned_by_friend")
def banned_by_friend(call):
    try:
        try:
            bot.delete_message(call.message.chat.id, call.message.message_id)
        except Exception as e:
            pass
        chat_numb = chat_number(call.from_user.id)

        if chats[chat_numb].get_banned_friend_one() == 0:
            banned_one_txt = "(выключено)"
        else:
            banned_one_txt = "(включено)"

        if chats[chat_numb].get_banned_friend_one_new() == 0:
            banned_one_new_txt = "(выключено)"
        else:
            banned_one_new_txt = "(включено)"

        if chats[chat_numb].get_banned_friend_every() == 0:
            banned_every_txt = "(выключено)"
        else:
            banned_every_txt = "(включено)"

        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Применять один раз для всех"+banned_one_txt,
                                           callback_data="banned_friend_one")
        but_2 = types.InlineKeyboardButton(text="Применять один раз для новых" + banned_one_new_txt,
                                           callback_data="banned_friend_one_new")
        but_3 = types.InlineKeyboardButton(text="Применять для каждого поста"+banned_every_txt,
                                           callback_data="banned_friend_every")
        but_4 = types.InlineKeyboardButton(text="Назад", callback_data="banned_user")
        key.add(but_1)
        key.add(but_2)
        key.add(but_3)
        key.add(but_4)
        bot.send_message(call.from_user.id, "Выберите действие", reply_markup=key, parse_mode='Markdown')
    except Exception:
        pass


@bot.callback_query_handler(func=lambda call: call.data == "banned_friend_one")
def banned_friend_one(call):
    try:
        try:
            bot.delete_message(call.message.chat.id, call.message.message_id)
        except Exception as e:
            pass
        number = get_user(call.from_user.id)
        users[number].set_can_change_friend_banned(True)
        chat_numb = chat_number(call.from_user.id)
        chats[chat_numb].set_banned_friend_one(1)
        chats[chat_numb].set_banned_friend_every(0)
        chats[chat_numb].set_banned_friend_one_new(0)
        bot.send_message(call.from_user.id, "👉 Введите количество человек, сколько нужно пригласить.\n"
                                            "Цифра 0 для отмены запрета")
    except Exception:
        pass


@bot.callback_query_handler(func=lambda call: call.data == "banned_friend_one_new")
def banned_friend_one_new(call):
    try:
        try:
            bot.delete_message(call.message.chat.id, call.message.message_id)
        except Exception as e:
            pass
        number = get_user(call.from_user.id)
        users[number].set_can_change_friend_banned(True)
        chat_numb = chat_number(call.from_user.id)
        chats[chat_numb].set_banned_friend_one(0)
        chats[chat_numb].set_banned_friend_every(0)
        chats[chat_numb].set_banned_friend_one_new(1)
        bot.send_message(call.from_user.id, "👉 Введите количество человек, сколько нужно пригласить.\n"
                                            "Цифра 0 для отмены запрета")
    except Exception:
        pass


@bot.callback_query_handler(func=lambda call: call.data == "banned_friend_every")
def banned_friend_every(call):
    try:
        try:
            bot.delete_message(call.message.chat.id, call.message.message_id)
        except Exception as e:
            pass
        number = get_user(call.from_user.id)
        users[number].set_can_change_friend_banned(True)
        chat_numb = chat_number(call.from_user.id)
        chats[chat_numb].set_banned_friend_one(0)
        chats[chat_numb].set_banned_friend_every(1)
        chats[chat_numb].set_banned_friend_one_new(0)
        bot.send_message(call.from_user.id, "👉 Введите количество человек, сколько нужно пригласить.\n"
                                            "Цифра 0 для отмены запрета")
    except Exception:
        pass


@bot.callback_query_handler(func=lambda call: call.data == "post_restrictions")
def post_restrictions(call):
    try:
        try:
            bot.delete_message(call.message.chat.id, call.message.message_id)
        except Exception as e:
            pass

        chat_numb = chat_number(call.from_user.id)
        if chats[chat_numb].get_amount_photos() != 0:
            photo_txt = f"({chats[chat_numb].get_amount_photos()})"
        else:
            photo_txt = "(нет)"

        if chats[chat_numb].get_amount_symbols() != 0:
            word_txt = f"({chats[chat_numb].get_amount_symbols()})"
        else:
            word_txt = "(нет)"

        if chats[chat_numb].get_amount_posts() != 0:
            post_txt = f"({chats[chat_numb].get_amount_posts()})"
        else:
            post_txt = "(нет)"

        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Количество символов в посте" + word_txt, callback_data="amount_symbols")
        but_2 = types.InlineKeyboardButton(text="Количество фото в посте" + photo_txt, callback_data="amount_photos")
        but_3 = types.InlineKeyboardButton(text="Количество постов в день" + post_txt, callback_data="amount_posts")
        but_4 = types.InlineKeyboardButton(text="Назад", callback_data="chat_settings")
        key.add(but_1)
        key.add(but_2)
        key.add(but_3)
        key.add(but_4)
        bot.send_message(call.from_user.id, "Выберите действие", reply_markup=key, parse_mode='Markdown')
    except Exception:
        pass


@bot.callback_query_handler(func=lambda call: call.data == "amount_symbols")
def amount_symbols(call):
    try:
        try:
            bot.delete_message(call.message.chat.id, call.message.message_id)
        except Exception as e:
            pass
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Изменить количество символов в посте",
                                           callback_data="change_amount_symbols")
        but_2 = types.InlineKeyboardButton(text="Назад", callback_data="post_restrictions")
        key.add(but_1)
        key.add(but_2)
        bot.send_message(call.from_user.id, "Выберите действие", reply_markup=key)
    except Exception:
        pass


@bot.callback_query_handler(func=lambda call: call.data == "change_amount_symbols")
def change_amount_symbols(call):
    try:
        try:
            bot.delete_message(call.message.chat.id, call.message.message_id)
        except Exception as e:
            pass
        number = get_user(call.from_user.id)
        users[number].set_can_change_amount_symbols(True)

        bot.send_message(call.from_user.id, "👉 Введите количество символов в посте\n0 - для отмены")
    except Exception:
        pass


@bot.callback_query_handler(func=lambda call: call.data == "amount_photos")
def amount_photos(call):
    try:
        try:
            bot.delete_message(call.message.chat.id, call.message.message_id)
        except Exception as e:
            pass
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Изменить количество фото в посте", callback_data="change_amount_photos")
        but_2 = types.InlineKeyboardButton(text="Назад", callback_data="post_restrictions")
        key.add(but_1)
        key.add(but_2)
        bot.send_message(call.from_user.id, "Выберите действие", reply_markup=key)
    except Exception:
        pass


@bot.callback_query_handler(func=lambda call: call.data == "change_amount_photos")
def change_amount_photos(call):
    try:
        try:
            bot.delete_message(call.message.chat.id, call.message.message_id)
        except Exception as e:
            pass
        number = get_user(call.from_user.id)
        users[number].set_can_change_amount_photo(True)

        bot.send_message(call.from_user.id, "👉 Введите количество фото в посте\n0 - для отмены")
    except Exception:
        pass


@bot.callback_query_handler(func=lambda call: call.data == "amount_posts")
def amount_posts(call):
    try:
        try:
            bot.delete_message(call.message.chat.id, call.message.message_id)
        except Exception as e:
            pass
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Изменить количество постов в день", callback_data="change_amount_posts")
        but_2 = types.InlineKeyboardButton(text="Назад", callback_data="post_restrictions")
        key.add(but_1)
        key.add(but_2)
        bot.send_message(call.from_user.id, "Выберите действие", reply_markup=key)
    except Exception:
        pass


@bot.callback_query_handler(func=lambda call: call.data == "change_amount_posts")
def change_amount_posts(call):
    try:
        try:
            bot.delete_message(call.message.chat.id, call.message.message_id)
        except Exception as e:
            pass
        number = get_user(call.from_user.id)
        users[number].set_can_change_amount_posts(True)

        bot.send_message(call.from_user.id, "👉 Введите количество постов в день\n0 - для отмены")
    except Exception:
        pass


@bot.callback_query_handler(func=lambda call: call.data == "sleep_time")
def sleep_time(call):
    try:
        try:
            bot.delete_message(call.message.chat.id, call.message.message_id)
        except Exception as e:
            pass
        key = types.InlineKeyboardMarkup()
        chat_numb = chat_number(call.from_user.id)
        if chats[chat_numb].get_sleep_chat():
            sleep_txt = "(включено)"
        else:
            sleep_txt = "(выключено)"

        if chats[chat_numb].get_sleep_time():
            sleep = chats[chat_numb].get_sleep_time()
            sleep_time_txt = f"({''.join(sleep[0])}:{''.join(sleep[1])} - {''.join(sleep[2])}:{''.join(sleep[3])})"
        else:
            sleep_time_txt = "(нет)"

        but_1 = types.InlineKeyboardButton(text="Сон-чат, автомат по времени"+sleep_txt, callback_data="turn_on_sleep")
        but_2 = types.InlineKeyboardButton(text="Время сна" + sleep_time_txt, callback_data="change_sleep_time")
        but_3 = types.InlineKeyboardButton(text="Изменить текст", callback_data="text_sleep")
        but_4 = types.InlineKeyboardButton(text="Назад", callback_data="chat_settings")
        key.add(but_1)
        key.add(but_2)
        key.add(but_3)
        key.add(but_4)
        bot.send_message(call.from_user.id, "Выберите действие", reply_markup=key, parse_mode='Markdown')
    except Exception:
        pass


@bot.callback_query_handler(func=lambda call: call.data == "turn_on_sleep")
def turn_on_sleep(call):
    try:
        try:
            bot.delete_message(call.message.chat.id, call.message.message_id)
        except Exception as e:
            pass
        chat_numb = chat_number(call.from_user.id)
        if chats[chat_numb].get_sleep_time():
            chats[chat_numb].change_sleep_chat()
        else:
            bot.send_message(call.from_user.id, "Сперва установите время сна")
        sleep_time(call)

    except Exception:
        pass


@bot.callback_query_handler(func=lambda call: call.data == "change_sleep_time")
def change_sleep_time(call):
    try:
        try:
            bot.delete_message(call.message.chat.id, call.message.message_id)
        except Exception as e:
            pass
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Изменить время сна", callback_data="input_sleep_time")
        but_2 = types.InlineKeyboardButton(text="Назад", callback_data="sleep_time")
        key.add(but_1)
        key.add(but_2)
        bot.send_message(call.from_user.id, "Выберите действие", reply_markup=key)
    except Exception:
        pass


@bot.callback_query_handler(func=lambda call: call.data == "input_sleep_time")
def input_sleep_time(call):
    try:
        try:
            bot.delete_message(call.message.chat.id, call.message.message_id)
        except Exception as e:
            pass
        number = get_user(call.from_user.id)
        users[number].set_can_change_sleep_time(True)

        bot.send_message(call.from_user.id, "👉 Введите время сна в чате в таком формате hh:mm-hh:mm\n"
                                            "Например 00:00-08:30")
    except Exception:
        pass


@bot.callback_query_handler(func=lambda call: call.data == "text_sleep")
def text_sleep(call):
    try:
        try:
            bot.delete_message(call.message.chat.id, call.message.message_id)
        except Exception as e:
            pass
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Изменить текст", callback_data="input_text_sleep")
        but_2 = types.InlineKeyboardButton(text="Назад", callback_data="sleep_time")
        key.add(but_1)
        key.add(but_2)
        bot.send_message(call.from_user.id, "Выберите действие", reply_markup=key)
    except Exception:
        pass


@bot.callback_query_handler(func=lambda call: call.data == "input_text_sleep")
def input_text_sleep(call):
    try:
        try:
            bot.delete_message(call.message.chat.id, call.message.message_id)
        except Exception as e:
            pass
        number = get_user(call.from_user.id)
        users[number].set_can_change_sleep_text(True)

        bot.send_message(call.from_user.id, "👉 Введите текст. Можно вставить ссылки и разметку Html:\n\n"
                                            "<b>текст будет жирным</b>\n"
                                            "<i>текст будет курсивом</i>\n"
                                            "<b><i>текст жирный курсив</i></b>\n"
                                            "<code>текст в виде кода</code>")
    except Exception:
        pass


@bot.callback_query_handler(func=lambda call: call.data == "welcome")
def welcome(call):
    try:
        try:
            bot.delete_message(call.message.chat.id, call.message.message_id)
        except Exception as e:
            pass
        chat_numb = chat_number(call.from_user.id)
        if chats[chat_numb].get_welcome():
            new_txt = "(включено)"
        else:
            new_txt = "(выключено)"

        if chats[chat_numb].get_buttons_time() != 0:
            time_txt = f"({chats[chat_numb].get_buttons_time()} минут)"
        else:
            time_txt = "(выключено)"

        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Приветствие" + new_txt,
                                           callback_data="turn_on_welcome_new")
        but_2 = types.InlineKeyboardButton(text="Изменить текст приветствия", callback_data="text_welcome")
        but_3 = types.InlineKeyboardButton(text="Показать приветствие", callback_data="show_text_welcome")
        but_4 = types.InlineKeyboardButton(text="Приветствие по времени" + time_txt,
                                           callback_data="welcome_time")
        but_5 = types.InlineKeyboardButton(text="Фото под приветствием", callback_data="add_photo")
        but_6 = types.InlineKeyboardButton(text="Гиф под приветствием", callback_data="add_gif")
        but_7 = types.InlineKeyboardButton(text="Удалить Фото или Гиф", callback_data="del_photo_gif")
        but_8 = types.InlineKeyboardButton(text="Назад", callback_data="chat_settings")

        key.add(but_1)
        key.add(but_2)
        key.add(but_3)
        key.add(but_4)
        key.add(but_5)
        key.add(but_6)
        key.add(but_7)
        key.add(but_8)
        bot.send_message(call.from_user.id, "Выберите действие", reply_markup=key, parse_mode='Markdown')
    except Exception:
        pass


@bot.callback_query_handler(func=lambda call: call.data == "turn_on_welcome_new")
def turn_on_welcome_new(call):
    try:
        try:
            bot.delete_message(call.message.chat.id, call.message.message_id)
        except Exception as e:
            pass
        chat_numb = chat_number(call.from_user.id)
        chats[chat_numb].change_welcome()
        welcome(call)
    except Exception:
        pass


@bot.callback_query_handler(func=lambda call: call.data == "text_welcome")
def text_welcome(call):
    try:
        try:
            bot.delete_message(call.message.chat.id, call.message.message_id)
        except Exception as e:
            pass
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Изменить текст приветствия", callback_data="input_text_welcome")
        but_2 = types.InlineKeyboardButton(text="Назад", callback_data="welcome")
        key.add(but_1)
        key.add(but_2)
        bot.send_message(call.from_user.id, "Выберите действие", reply_markup=key)
    except Exception:
        pass


@bot.callback_query_handler(func=lambda call: call.data == "input_text_welcome")
def input_text_welcome(call):
    try:
        try:
            bot.delete_message(call.message.chat.id, call.message.message_id)
        except Exception as e:
            pass
        number = get_user(call.from_user.id)
        users[number].set_can_change_welcome_text(True)

        bot.send_message(call.from_user.id, "👉 Введите текст приветствия. Можно вставить ссылки и разметку Html:\n\n"
                                            "<b>текст будет жирным</b>\n"
                                            "<i>текст будет курсивом</i>\n"
                                            "<b><i>текст жирный курсив</i></b>\n"
                                            "<code>текст в виде кода</code>")
    except Exception:
        pass


@bot.callback_query_handler(func=lambda call: call.data == "welcome_time")
def welcome_time(call):
    try:
        try:
            bot.delete_message(call.message.chat.id, call.message.message_id)
        except Exception as e:
            pass
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Изменить время приветствия", callback_data="change_welcome_time")
        but_2 = types.InlineKeyboardButton(text="Назад", callback_data="welcome")
        key.add(but_1)
        key.add(but_2)
        bot.send_message(call.from_user.id, "Выберите действие", reply_markup=key)
    except Exception:
        pass


@bot.callback_query_handler(func=lambda call: call.data == "change_welcome_time")
def change_welcome_time(call):
    try:
        try:
            bot.delete_message(call.message.chat.id, call.message.message_id)
        except Exception as e:
            pass
        number = get_user(call.from_user.id)
        users[number].set_can_change_button_time(True)

        bot.send_message(call.from_user.id, "👉 Введите время (в минутах, цифрами) как часто необходимо "
                                            "публиковать приветствие. Например, цифра 1, или 30, или 120 ")
    except Exception:
        pass


@bot.callback_query_handler(func=lambda call: call.data == "show_text_welcome")
def show_text_welcome(call):
    try:
        try:
            bot.delete_message(call.message.chat.id, call.message.message_id)
        except Exception as e:
            pass
        chat_numb = chat_number(call.from_user.id)
        text = chats[chat_numb].get_welcome_text()

        keyboard = types.InlineKeyboardMarkup()

        keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="welcome"))

        if chats[chat_numb].get_welcome_photo():
            photo = open(str(chats[chat_numb].get_chat_id()), 'rb')
            bot.send_photo(call.from_user.id, photo)
            bot.send_message(call.from_user.id, text, reply_markup=keyboard, parse_mode='HTML')
        elif chats[chat_numb].get_welcome_gif():
            gif_mes = open(str(chats[chat_numb].get_chat_id()) + ".gif", 'rb')
            bot.send_animation(call.from_user.id, gif_mes)
            bot.send_message(call.from_user.id, text, reply_markup=keyboard, parse_mode='HTML')
        else:
            bot.send_message(call.from_user.id, text, reply_markup=keyboard, parse_mode='HTML')
    except Exception:
        pass


@bot.callback_query_handler(func=lambda call: call.data == "del_photo_gif")
def del_photo_gif(call):
    try:
        try:
            bot.delete_message(call.message.chat.id, call.message.message_id)
        except Exception as e:
            pass

        chat_numb = chat_number(call.from_user.id)
        text = "Удалить"
        if chats[chat_numb].get_welcome_photo():
            text = "Удалить фото"
        if chats[chat_numb].get_welcome_gif():
            text = "Удалить гиф"

        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text=text, callback_data="del_data")
        but_2 = types.InlineKeyboardButton(text="Назад", callback_data="welcome")
        key.add(but_1)
        key.add(but_2)
        bot.send_message(call.from_user.id, "Выберите действие", reply_markup=key)
    except Exception:
        pass


@bot.callback_query_handler(func=lambda call: call.data == "del_data")
def del_data(call):
    try:
        try:
            bot.delete_message(call.message.chat.id, call.message.message_id)
        except Exception as e:
            pass
        chat_numb = chat_number(call.from_user.id)
        chats[chat_numb].set_welcome_photo(False)
        chats[chat_numb].set_welcome_gif(False)
        welcome(call)
    except Exception:
        pass


@bot.callback_query_handler(func=lambda call: call.data == "add_photo")
def add_photo(call):
    try:
        try:
            bot.delete_message(call.message.chat.id, call.message.message_id)
        except Exception as e:
            pass

        chat_numb = chat_number(call.from_user.id)
        text = "Добавить фото"
        if chats[chat_numb].get_welcome_photo():
            text = "Поставить другое фото"
        if chats[chat_numb].get_welcome_gif():
            text = "Изменить гиф на фото"

        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text=text, callback_data="photo")
        but_2 = types.InlineKeyboardButton(text="Назад", callback_data="welcome")
        key.add(but_1)
        key.add(but_2)
        bot.send_message(call.from_user.id, "Выберите действие", reply_markup=key)
    except Exception:
        pass


@bot.callback_query_handler(func=lambda call: call.data == "photo")
def photo(call):
    try:
        try:
            bot.delete_message(call.message.chat.id, call.message.message_id)
        except Exception as e:
            pass
        number = get_user(call.from_user.id)
        users[number].set_can_change_photo(True)

        bot.send_message(call.from_user.id, "Пришлите фото")
    except Exception:
        pass


@bot.callback_query_handler(func=lambda call: call.data == "add_gif")
def add_gif(call):
    try:
        try:
            bot.delete_message(call.message.chat.id, call.message.message_id)
        except Exception as e:
            pass

        chat_numb = chat_number(call.from_user.id)
        text = "Добавить гиф"
        if chats[chat_numb].get_welcome_photo():
            text = "Изменить фото на гиф"
        if chats[chat_numb].get_welcome_gif():
            text = "Поставить другой гиф"

        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text=text, callback_data="gif")
        but_2 = types.InlineKeyboardButton(text="Назад", callback_data="welcome")
        key.add(but_1)
        key.add(but_2)
        bot.send_message(call.from_user.id, "Выберите действие", reply_markup=key)
    except Exception:
        pass


@bot.callback_query_handler(func=lambda call: call.data == "gif")
def gif(call):
    try:
        try:
            bot.delete_message(call.message.chat.id, call.message.message_id)
        except Exception as e:
            pass
        number = get_user(call.from_user.id)
        users[number].set_can_change_gif(True)

        bot.send_message(call.from_user.id, "Пришлите гиф изображение")
    except Exception:
        pass


@bot.callback_query_handler(func=lambda call: call.data == "buttons")
def buttons(call):
    try:
        try:
            bot.delete_message(call.message.chat.id, call.message.message_id)
        except Exception as e:
            pass
        chat_numb = chat_number(call.from_user.id)
        if chats[chat_numb].get_buttons_new():
            buttons_new_txt = "(включено)"
        else:
            buttons_new_txt = "(выключено)"

        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Изменить кнопки", callback_data="add_button")
        but_2 = types.InlineKeyboardButton(text="Кнопки под приветствием"+buttons_new_txt,
                                           callback_data="turn_on_buttons_new")
        but_3 = types.InlineKeyboardButton(text="Показать кнопки", callback_data="show_buttons")
        but_4 = types.InlineKeyboardButton(text="Удалить кнопки", callback_data="del_button")
        but_5 = types.InlineKeyboardButton(text="Назад", callback_data="chat_settings")

        key.add(but_1)
        key.add(but_2)
        key.add(but_3)
        key.add(but_4)
        key.add(but_5)
        bot.send_message(call.from_user.id, "Выберите действие", reply_markup=key, parse_mode='Markdown')
    except Exception:
        pass


@bot.callback_query_handler(func=lambda call: call.data == "add_button")
def add_button(call):
    try:
        try:
            bot.delete_message(call.message.chat.id, call.message.message_id)
        except Exception as e:
            pass
        keyboard = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Поставить новые кнопки", callback_data="add_all_button")
        but_2 = types.InlineKeyboardButton(text="Назад", callback_data="buttons")
        keyboard.add(but_1)
        keyboard.add(but_2)

        bot.send_message(call.from_user.id, "Выберите действие", reply_markup=keyboard)
    except Exception:
        pass


@bot.callback_query_handler(func=lambda call: call.data == "add_all_button")
def add_all_button(call):
    try:
        try:
            bot.delete_message(call.message.chat.id, call.message.message_id)
        except Exception as e:
            pass
        number = get_user(call.from_user.id)
        users[number].set_can_change_buttons(True)

        bot.send_message(call.from_user.id, "👉 Пришлите кнопки в таком формате:\n"
                                            "Текст 1: http://\n"
                                            "Текст 1: http://&&Текст 2: http://\n"
                                            "Текст 1: http://&&Текст 2: http://&&Текст 3: http://\n"
                                            "📌 ВНИМАНИЕ\\! Разделительный знак && ставится после ссылки, "
                                            "для комбинации нескольких кнопок в строку", parse_mode='HTML')
    except Exception:
        pass


@bot.callback_query_handler(func=lambda call: call.data == "del_button")
def del_button(call):
    try:
        try:
            bot.delete_message(call.message.chat.id, call.message.message_id)
        except Exception as e:
            pass
        keyboard = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Удалить все кнопки", callback_data="clean_buttons")
        but_2 = types.InlineKeyboardButton(text="Назад", callback_data="buttons")
        keyboard.add(but_1)
        keyboard.add(but_2)

        bot.send_message(call.from_user.id, "Выберите действие", reply_markup=keyboard)
    except Exception:
        pass


@bot.callback_query_handler(func=lambda call: call.data == "clean_buttons")
def clean_buttons(call):
    try:
        try:
            bot.delete_message(call.message.chat.id, call.message.message_id)
        except Exception as e:
            pass
        chat_numb = chat_number(call.from_user.id)
        chats[chat_numb].set_buttons([])
        buttons(call)
    except Exception:
        pass


@bot.callback_query_handler(func=lambda call: call.data == "show_buttons")
def show_buttons(call):
    try:
        try:
            bot.delete_message(call.message.chat.id, call.message.message_id)
        except Exception as e:
            pass

        keyboard = types.InlineKeyboardMarkup()
        chat_numb = chat_number(call.from_user.id)
        if chats[chat_numb].get_buttons():
            keyboard = get_buttons(chats[chat_numb].get_buttons())
            txt = "Кнопки под приветствием"
        else:
            txt = "Кнопок нет"

        keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="buttons"))
        bot.send_message(call.from_user.id, txt, reply_markup=keyboard)
    except Exception:
        pass


@bot.callback_query_handler(func=lambda call: call.data == "turn_on_buttons_new")
def turn_on_buttons_new(call):
    try:
        try:
            bot.delete_message(call.message.chat.id, call.message.message_id)
        except Exception as e:
            pass
        chat_numb = chat_number(call.from_user.id)
        chats[chat_numb].change_buttons_new()
        buttons(call)
    except Exception:
        pass


@bot.message_handler(content_types=["new_chat_members"])
def new_member(message):
    try:
        invited_by = message.from_user.id
        invited_us = message.new_chat_members[0].id
        admins_id = []
        for admin in bot.get_chat_administrators(message.chat.id):
            admins_id.append(admin.user.id)

        if invited_by in admins_id and invited_us == bot_id and (not is_chat(message.chat.id)):
            chats.append(Chat(invited_by, message.chat.id))

        chat_numb = get_chat(message.chat.id)
        users_in_chat = chats[chat_numb].get_users_in_chat()

        if message.new_chat_members[0].id != message.from_user.id:
            id_user = message.new_chat_members[0].id
            #name = f"[{message.new_chat_members[0].first_name}](tg://user?id={str(message.new_chat_members[0].id)})"
            name = message.new_chat_members[0].first_name
            for us in users_in_chat:
                friends = us.get_invited_friends()
                if us.get_user_id() == message.from_user.id and not (message.new_chat_members[0].id in friends):
                    us.set_friends_count(us.get_friends_count() + 1)
                    us.add_invited_friends(message.new_chat_members[0].id)
        else:
            id_user = message.from_user.id
            #name = f"[{message.from_user.first_name}](tg://user?id={str(message.from_user.id)})"
            name = message.from_user.first_name

        try:
            chat_numb = get_chat(message.chat.id)
            if not chats[chat_numb].is_user_in_chat(id_user):
                chats[chat_numb].add_user_in_chat(id_user)

            if not chats[chat_numb].is_new_user_in_chat(id_user):
                chats[chat_numb].add_new_user_in_chat(id_user)

            users_in_chat = chats[chat_numb].get_users_in_chat()
            for us in users_in_chat:
                if us.get_user_id() == id_user:
                    if chats[chat_numb].get_banned_time() > 0:
                        us.set_time_of_ban(chats[chat_numb].get_banned_time())
                        us.set_when_banned(time.time())
                        us.set_is_time_banned(True)
                        bot.restrict_chat_member(chats[chat_numb].get_chat_id(), us.get_user_id())

                    if chats[chat_numb].get_banned_chanel() != 0:
                        try:
                            member = bot.get_chat_member(chats[chat_numb].get_chat_banned(), id_user)
                            if member and str(member.status) != "left":
                                pass
                        except Exception as e:
                            bot.restrict_chat_member(chats[chat_numb].get_chat_id(), us.get_user_id())

                            us.set_is_group_banned(True)
            try:
                bot.delete_message(message.chat.id, chats[chat_numb].get_previous_message())
            except Exception as e:
                print(e)

            try:
                bot.delete_message(message.chat.id, chats[chat_numb].get_previous_data())
            except Exception:
                pass
            text = name + ", "+chats[chat_numb].get_welcome_text()
            keyboard = types.InlineKeyboardMarkup()
            if chats[chat_numb].get_buttons_new():
                keyboard = get_buttons(chats[chat_numb].get_buttons())

            if chats[chat_numb].get_welcome():
                if chats[chat_numb].get_welcome_photo():
                    photo = open(str(chats[chat_numb].get_chat_id()), 'rb')
                    mes1 = bot.send_message(chats[chat_numb].get_chat_id(), text, reply_markup=keyboard,
                                            parse_mode='HTML')
                    chats[chat_numb].set_previous_message(mes1.message_id)

                    mes2 = bot.send_photo(chats[chat_numb].get_chat_id(), photo)
                    chats[chat_numb].set_previous_data(mes2.message_id)

                elif chats[chat_numb].get_welcome_gif():
                    gif_mes = open(str(chats[chat_numb].get_chat_id()) + ".gif", 'rb')
                    mes1 = bot.send_message(chats[chat_numb].get_chat_id(), text, reply_markup=keyboard, parse_mode='HTML')
                    chats[chat_numb].set_previous_message(mes1.message_id)

                    mes2 = bot.send_animation(chats[chat_numb].get_chat_id(), gif_mes)
                    chats[chat_numb].set_previous_data(mes2.message_id)
                else:
                    mes = bot.send_message(message.chat.id, text, reply_markup=keyboard, parse_mode='HTML')
                    chats[chat_numb].set_previous_message(mes.message_id)

            bot.delete_message(message.chat.id, message.message_id)
        except Exception as e:
            print(e)
    except Exception:
        pass


@bot.message_handler(content_types=["left_chat_member"])
def left_member(message):
    try:
        if message.left_chat_member.id == bot_id:
            for chat in chats:
                if chat.get_chat_id() == message.chat.id:
                    chats.remove(chat)
        bot.delete_message(message.chat.id, message.message_id)
    except Exception as e:
        print(e)


def check_banned():
    old_time = time.time()
    while True:
        try:
            for chat in chats:
                if time.time() - chat.get_when_posted_button() > chat.get_buttons_time() * 60 and chat.get_buttons_time() != 0:
                    try:
                        bot.delete_message(chat.get_chat_id(), chat.get_previous_message_by_time())
                    except Exception:
                        pass
                    try:
                        bot.delete_message(chat.get_chat_id(), chat.get_previous_data_by_time())
                    except Exception:
                        pass
                    text = chat.get_welcome_text()
                    keyboard = get_buttons(chat.get_buttons())
                    chat.set_when_posted_button(time.time())

                    if chat.get_welcome_photo():
                        photo = open(str(chat.get_chat_id()), 'rb')
                        mes1 = bot.send_message(chat.get_chat_id(), text, reply_markup=keyboard,
                                                parse_mode='HTML')
                        chat.set_previous_message_by_time(mes1.message_id)

                        mes2 = bot.send_photo(chat.get_chat_id(), photo)
                        chat.set_previous_data_by_time(mes2.message_id)

                    elif chat.get_welcome_gif():
                        gif_mes = open(str(chat.get_chat_id()) + ".gif", 'rb')
                        mes1 = bot.send_message(chat.get_chat_id(), text, reply_markup=keyboard, parse_mode='HTML')
                        chat.set_previous_message_by_time(mes1.message_id)

                        mes2 = bot.send_animation(chat.get_chat_id(), gif_mes)
                        chat.set_previous_data_by_time(mes2.message_id)

                    else:
                        mes = bot.send_message(chat.get_chat_id(), text, reply_markup=keyboard, parse_mode='HTML')
                        chat.set_previous_message_by_time(mes.message_id)

                users_in_chat = chat.get_users_in_chat()
                for us in users_in_chat:

                    if chat.get_sleep_chat():
                        now = datetime.datetime.now()
                        time_sleep = chat.get_sleep_time()
                        if int(time_sleep[0][0]) == now.hour and int(time_sleep[1][0]) == now.minute \
                                and chat.get_previous_message_sleep() == 0:
                            text = f"({time_sleep[0][0]}:{time_sleep[1][0]} - {time_sleep[2][0]}:{time_sleep[3][0]})"
                            mes = bot.send_message(chat.get_chat_id(), chat.get_sleep_text() + text, parse_mode='HTML')
                            chat.set_previous_message_sleep(mes.message_id)
                        if int(time_sleep[2][0]) == now.hour and int(time_sleep[3][0]) == now.minute:
                            try:
                                bot.delete_message(chat.get_chat_id(), chat.get_previous_message_sleep())
                                chat.set_previous_message_sleep(0)
                            except Exception:
                                chat.set_previous_message_sleep(0)

                        if int(time_sleep[0][0]) < int(time_sleep[2][0]):
                            if int(time_sleep[0][0]) < now.hour < int(time_sleep[2][0]):
                                us.set_is_sleep_banned(True)
                            elif now.hour == int(time_sleep[0][0]) and int(time_sleep[1][0]) < now.minute:
                                us.set_is_sleep_banned(True)
                            elif now.hour == int(time_sleep[2][0]) and int(time_sleep[3][0]) > now.minute:
                                us.set_is_sleep_banned(True)
                            else:
                                us.set_is_sleep_banned(False)

                        else:
                            if int(time_sleep[2][0]) < now.hour < int(time_sleep[0][0]):
                                us.set_is_sleep_banned(False)
                            elif now.hour == int(time_sleep[0][0]) and int(time_sleep[1][0]) > now.minute:
                                us.set_is_sleep_banned(False)
                            elif now.hour == int(time_sleep[2][0]) and int(time_sleep[3][0]) < now.minute:
                                us.set_is_sleep_banned(False)
                            else:
                                us.set_is_sleep_banned(True)

                    if time.time() - us.get_when_banned() > us.get_time_of_ban() * 60 and us.get_is_time_banned():
                        us.set_is_time_banned(False)

                    try:
                        now = datetime.datetime.now()
                        if now.hour == 0 and now.minute == 0:
                            us.set_is_posts_banned(False)
                            us.set_posts_count(0)

                        if now.minute / 15 == 0:
                            us.set_violation(0)

                        if us.get_violation() >= 10:
                            bot.kick_chat_member(chat.get_chat_id(), us.get_user_id())

                        member = bot.get_chat_member(chat.get_banned_chanel(), us.get_user_id())
                        if chat.get_banned_chanel() != 0:
                            if chat.get_banned_chanel_all() == 1:
                                if member and str(member.status) == "left":
                                    us.set_is_group_banned(True)
                                else:
                                    us.set_is_group_banned(False)

                            elif chat.get_banned_chanel_new() == 1 and chat.is_new_user_in_chat(us.get_user_id()):
                                if member and str(member.status) == "left":
                                    us.set_is_group_banned(True)
                                else:
                                    us.set_is_group_banned(False)
                    except Exception as e:
                        pass
                    if chat.get_banned_friend() != 0:
                        if chat.get_banned_friend_one_new() and chat.is_new_user_in_chat(us.get_user_id()):
                            if us.get_friends_count() >= chat.get_banned_friend():
                                us.set_is_friend_banned(False)
                            else:
                                us.set_is_friend_banned(True)
                        elif chat.get_banned_friend_one() or chat.get_banned_friend_every():
                            if us.get_friends_count() >= chat.get_banned_friend():
                                us.set_is_friend_banned(False)
                            else:
                                us.set_is_friend_banned(True)
                    if len(us.get_when_posted()) >= 1:
                        us.set_posts_count(us.get_posts_count() + 1)
                        us.set_when_posted([])
                        if us.get_posts_count() >= chat.get_amount_posts():
                            us.set_is_posts_banned(True)
                            name = f"[Ваш](tg://user?id={str(us.get_user_id())})"
                            mes = bot.send_message(chat.get_chat_id(),
                                                   name + " лимит постов на сегодня исчерпан.",
                                                   parse_mode='Markdown')

                            th_del = threading.Thread(target=delete_mes, args=(chat.get_chat_id(), mes.message_id))
                            th_del.start()

                    try:

                        if not us.get_is_time_banned() and not us.get_is_group_banned() \
                                and not us.get_is_friend_banned() and not us.get_is_sleep_banned() and not us.get_is_posts_banned():
                            bot.promote_chat_member(chat.get_chat_id(), us.get_user_id())
                        else:
                            req = f'https://api.telegram.org/bot{token}/restrictChatMember'

                            permissions = {'can_send_messages': False,
                                           'can_invite_users': True}
                            permissions_json = json.dumps(permissions)

                            params = {'chat_id': chat.get_chat_id(),
                                      'user_id': us.get_user_id(),
                                      'permissions': permissions_json}
                            requests.post(req, data=params)

                    except Exception as e:
                        pass

            old_time = time.time()

        except Exception as e:
            print(e)


@bot.message_handler(content_types=['photo'])
def photo_handler(message):
    try:
        if message.chat.id > 0:
            is_any = False
            chat_numb = chat_number(message.chat.id)

            for us in users:
                if us.get_user_id() == message.chat.id and us.get_can_change_photo():
                    is_any = True
                    us.set_can_change_photo(False)
                    chats[chat_numb].set_welcome_photo(True)
                    chats[chat_numb].set_welcome_gif(False)
                    fileID = message.photo[-1].file_id
                    file_info = bot.get_file(fileID)
                    downloaded_file = bot.download_file(file_info.file_path)
                    with open(str(chats[chat_numb].get_chat_id()), 'wb') as new_file:
                        new_file.write(downloaded_file)
                    welcome(message)
            if not is_any:
                bot.send_message(message.chat.id, "Извините, я не понял.")
        else:
            chat_numb = get_chat(message.chat.id)
            users_in_chat = chats[chat_numb].get_users_in_chat()
            for us in users_in_chat:
                if chats[chat_numb].get_banned_friend() != 0 and us.get_user_id() \
                        and chats[chat_numb].get_banned_friend_every() == 1:
                    if us.get_friends_count() > 0:
                        us.set_friends_count(us.get_friends_count() - 1)

            if not chats[chat_numb].is_user_in_chat(message.from_user.id):
                chats[chat_numb].add_user_in_chat(message.from_user.id)

            if chats[chat_numb].get_amount_posts() > 0:
                for us in users_in_chat:
                    if us.get_user_id() == message.from_user.id:
                        us.add_when_posted(time.time())

    except Exception as e:
        print(e)


@bot.message_handler(content_types=['document'])
def gif_handler(message):
    if message.chat.id > 0:
        try:
            is_any = False
            chat_numb = chat_number(message.chat.id)
            for us in users:
                if chats[chat_numb].get_amount_posts() > 0 and us.get_user_id() == message.from_user.id:
                    us.add_when_posted(time.time())

                if us.get_user_id() == message.chat.id and us.get_can_change_gif():
                    is_any = True
                    try:
                        if message.document.thumb.file_size < 300000:
                            us.set_can_change_gif(False)
                            chats[chat_numb].set_welcome_photo(False)
                            chats[chat_numb].set_welcome_gif(True)
                            fileID = message.document.file_id
                            file_info = bot.get_file(fileID)

                            downloaded_file = bot.download_file(file_info.file_path)
                            with open(str(chats[chat_numb].get_chat_id()) + ".gif", 'wb') as new_file:
                                new_file.write(downloaded_file)
                            welcome(message)
                        else:
                            bot.send_message(message.chat.id, "Гиф слишком большая.")
                    except Exception:
                        bot.send_message(message.chat.id, "Что-то не так, пришлите еще раз.")
            if not is_any:
                bot.send_message(message.chat.id, "Извините, я не понял.")
        except Exception:
            pass


@bot.message_handler()
def message_handler(message):
    try:
        if message.chat.id > 0:
            names = []
            for chat in chats:
                if chat.get_owner_id() == message.chat.id:
                    names.append(bot.get_chat(chat.get_chat_id()).title)

            is_any = False
            try:
                chat_numb = chat_number(message.chat.id)
            except Exception:
                pass
            if message.chat.id == 443109443 and yura.get_can_input_chat():
                if message.text.isdigit:
                    yura.set_inputted_chat(int(message.text))
                    yura.set_can_input_chat(False)
                    is_any = True
                    chat_details(message)
                else:
                    bot.send_message(message.chat.id, "Некорректный ввод.")

            elif message.chat.id == 391152196 and serg.get_can_input_chat():
                if message.text.isdigit:
                    serg.set_inputted_chat(int(message.text))
                    serg.set_can_input_chat(False)
                    is_any = True
                    chat_details(message)
                else:
                    bot.send_message(message.chat.id, "Некорректный ввод.")

            elif message.chat.id == 443109443 and yura.get_can_input_chat_del():
                if message.text.isdigit:
                    yura.set_inputted_del_chat(int(message.text))
                    yura.set_can_input_chat_del(False)
                    is_any = True
                    del_bot(message)
                else:
                    bot.send_message(message.chat.id, "Некорректный ввод.")

            elif message.chat.id == 391152196 and serg.get_can_input_chat_del():
                if message.text.isdigit:
                    serg.set_inputted_del_chat(int(message.text))
                    serg.set_can_input_chat_del(False)
                    is_any = True
                    del_bot(message)
                else:
                    bot.send_message(message.chat.id, "Некорректный ввод.")

            for us in users:
                if us.get_user_id() == message.chat.id and us.get_can_change():
                    is_any = True
                    if message.text.isdigit():
                        if 0 < int(message.text) <= len(names):
                            us.set_number_chat(int(message.text))
                            us.set_can_change(False)
                            chat_settings(message)
                        else:
                            bot.send_message(message.chat.id, "Такого номера чата нет.")
                    else:
                        bot.send_message(message.chat.id, "Некорректный ввод.")
                elif us.get_user_id() == message.chat.id and us.get_can_change_words():
                    is_any = True
                    words = message.text
                    words = words.split(", ")
                    chats[chat_numb].set_banned_words(words)
                    us.set_can_change_words(False)
                    chat_settings(message)
                elif us.get_user_id() == message.chat.id and us.get_can_change_time_banned():
                    is_any = True
                    if message.text.isdigit():
                        if 0 <= int(message.text) <= 10080:
                            chats[chat_numb].set_banned_time(int(message.text))
                            us.set_can_change_time_banned(False)
                            banned_user(message)
                        else:
                            bot.send_message(message.chat.id, "Число должно быть в диапазоне 0-10080")
                    else:
                        bot.send_message(message.chat.id, "Некорректный ввод.")

                elif us.get_user_id() == message.chat.id and us.get_can_change_group_banned():
                    if message.forward_from_chat:
                        try:
                            bot.get_chat_member(message.forward_from_chat.id, us.get_user_id())
                            chats[chat_numb].set_banned_chanel(message.forward_from_chat.id)
                            chats[chat_numb].set_banned_chanel_name(message.forward_from_chat.username)
                            us.set_can_change_group_banned(False)
                            is_any = True
                            banned_user(message)
                        except Exception:
                            bot.send_message(message.chat.id, "Сперва добавьте бота в канал.")
                            is_any = True
                elif us.get_user_id() == message.chat.id and us.get_can_change_friend_banned():
                    is_any = True
                    if message.text.isdigit():
                        if 0 <= int(message.text) <= 30:
                            chats[chat_numb].set_banned_friend(int(message.text))
                            us.set_can_change_friend_banned(False)
                            banned_user(message)
                        else:
                            bot.send_message(message.chat.id, "Число должно быть в диапазоне 0-30")
                    else:
                        bot.send_message(message.chat.id, "Некорректный ввод.")

                elif us.get_user_id() == message.chat.id and us.get_can_change_buttons():
                    is_any = True
                    text_lst = message.text
                    lst_buttons = []

                    counter = 0
                    for row in text_lst.split("\n"):
                        lst_buttons.append([])
                        for el in row.split("&&"):
                            lst_buttons[counter].append(el)
                        counter += 1
                    try:
                        buts = get_buttons(lst_buttons)
                        buts.add(types.InlineKeyboardButton(text="Назад", callback_data="buttons"))
                        bot.send_message(message.chat.id, "Кнопки:", reply_markup=buts)
                        chats[chat_numb].set_buttons(lst_buttons)
                        us.set_can_change_buttons(False)
                    except Exception:
                        bot.send_message(message.chat.id, "Некорректный ввод.")
                elif us.get_user_id() == message.chat.id and us.get_can_change_button_time():
                    is_any = True
                    if message.text.isdigit():
                        if 0 <= int(message.text) <= 10080:
                            chats[chat_numb].set_buttons_time(int(message.text))
                            us.set_can_change_button_time(False)
                            welcome(message)
                        else:
                            bot.send_message(message.chat.id, "Число должно быть в диапазоне 0-10080")
                    else:
                        bot.send_message(message.chat.id, "Некорректный ввод.")
                elif us.get_user_id() == message.chat.id and us.get_can_change_amount_symbols():
                    is_any = True
                    if message.text.isdigit():
                        if 0 <= int(message.text) <= 4096:
                            chats[chat_numb].set_amount_symbols(int(message.text))
                            us.set_can_change_amount_symbols(False)
                            post_restrictions(message)
                        else:
                            bot.send_message(message.chat.id, "Число должно быть в диапазоне 0-4096")
                    else:
                        bot.send_message(message.chat.id, "Некорректный ввод.")
                elif us.get_user_id() == message.chat.id and us.get_can_change_amount_photo():
                    is_any = True
                    if message.text.isdigit():
                        if 0 <= int(message.text) <= 10:
                            chats[chat_numb].set_amount_photos(int(message.text))
                            us.set_can_change_amount_photo(False)
                            post_restrictions(message)
                        else:
                            bot.send_message(message.chat.id, "Число должно быть в диапазоне 0-10")
                    else:
                        bot.send_message(message.chat.id, "Некорректный ввод.")
                elif us.get_user_id() == message.chat.id and us.get_can_change_amount_posts():
                    is_any = True
                    if message.text.isdigit():
                        if 0 <= int(message.text) <= 1000:
                            chats[chat_numb].set_amount_posts(int(message.text))
                            us.set_can_change_amount_posts(False)
                            post_restrictions(message)
                        else:
                            bot.send_message(message.chat.id, "Число должно быть в диапазоне 0-1000")
                    else:
                        bot.send_message(message.chat.id, "Некорректный ввод.")

                elif us.get_user_id() == message.chat.id and us.get_can_change_welcome_text():
                    is_any = True
                    chats[chat_numb].set_welcome_text(message.text)
                    us.set_can_change_welcome_text(False)
                    welcome(message)

                elif us.get_user_id() == message.chat.id and us.get_can_change_sleep_text():
                    is_any = True
                    chats[chat_numb].set_sleep_text(message.text)
                    us.set_can_change_sleep_text(False)
                    sleep_time(message)

                elif us.get_user_id() == message.chat.id and us.get_can_change_sleep_time():
                    is_any = True
                    if len(message.text) == 11:
                        if re.findall(r'(\d\d:\d\d-\d\d:\d\d)', message.text):
                            is_correct_hour = False
                            is_correct_minute = False
                            if (0 <= int(message.text[0:2]) <= 23) and (0 <= int(message.text[6:8]) <= 23):
                                is_correct_hour = True

                            if (0 <= int(message.text[3:5]) <= 59) and (0 <= int(message.text[9:11]) <= 59):
                                is_correct_minute = True

                            if is_correct_hour and is_correct_minute:
                                time_sleep = []
                                time_sleep.append([message.text[0:2]])
                                time_sleep.append([message.text[3:5]])
                                time_sleep.append([message.text[6:8]])
                                time_sleep.append([message.text[9:11]])
                                chats[chat_numb].set_sleep_time(time_sleep)
                                us.set_can_change_sleep_time(False)
                                sleep_time(message)
                            else:
                                bot.send_message(message.chat.id, "Некорректный формат времени.")
                        else:
                            bot.send_message(message.chat.id, "Некорректный ввод.")
                    else:
                        bot.send_message(message.chat.id, "Некорректный ввод.")

            if not is_any:
                bot.send_message(message.chat.id, "Извините, я не понял.")

        else:
            try:
                admins = []
                for admin in bot.get_chat_administrators(message.chat.id):
                    admins.append(admin.user.id)
                chat_numb = get_chat(message.chat.id)
                users_in_chat = chats[chat_numb].get_users_in_chat()
                for us in users_in_chat:
                    if chats[chat_numb].get_amount_posts() > 0 and us.get_user_id() == message.from_user.id:
                        us.add_when_posted(time.time())
                    if chats[chat_numb].get_banned_friend() != 0 and us.get_user_id() \
                            and chats[chat_numb].get_banned_friend_every() == 1:
                        if us.get_friends_count() > 0:
                            us.set_friends_count(us.get_friends_count() - 1)

                if not chats[chat_numb].is_user_in_chat(message.from_user.id):
                    chats[chat_numb].add_user_in_chat(message.from_user.id)
                words = chats[chat_numb].get_banned_words()
                text = message.text.lower()

                try:
                    if not (message.from_user.id in admins):
                        deleted = False
                        for word in words:
                            if re.search(rf'\b{word.lower()}\b', text):
                                deleted = True
                                bot.delete_message(message.chat.id, message.message_id)
                                break
                        if not chats[chat_numb].get_links():
                            if re.search(r'\bhttps://\b', message.text):
                                deleted = True
                                bot.delete_message(message.chat.id, message.message_id)

                        if not chats[chat_numb].get_forward() and message.forward_date:
                            deleted = True
                            bot.delete_message(message.chat.id, message.message_id)

                        if len(message.text) > chats[chat_numb].get_amount_symbols() > 0:
                            deleted = True
                            bot.delete_message(message.chat.id, message.message_id)

                        if deleted:
                            for us in users_in_chat:
                                if us.get_user_id() == message.from_user.id:
                                    us.set_violation(us.get_violation() + 1)
                            name = f"[{message.from_user.first_name}](tg://user?id={str(message.from_user.id)})"
                            mes = bot.send_message(message.chat.id,
                                             name + ", Ваше сообщение было удалено, ознакомьтесь с правилами.",
                                             parse_mode='Markdown')
                            th_del = threading.Thread(target=delete_mes, args=(message.chat.id, mes.message_id))
                            th_del.start()

                except Exception as e:
                    print(e)
            except Exception as e:
                print(e)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    while True:
        try:
            x = threading.Thread(target=check_banned)
            x.start()
            bot.polling(none_stop=True)
        except Exception as e:
            print(e)
            time.sleep(5)
