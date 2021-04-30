import telebot
import os
from dotenv import load_dotenv, find_dotenv
from google_trans_new import google_translator
import google_trans_new

from connect_db import update_language_target_for_user, add_new_user, get_language_target, get_all_users,\
                update_language_from_for_user, get_language_from
translator = google_translator()


load_dotenv(find_dotenv())
bot = telebot.TeleBot(os.environ.get("TOKEN"))


@bot.message_handler(commands=['all_lang'])
def print_all_language(message):
    bot.send_message(message.chat.id, "This language I do not know( Please,choose from the list below)")
    all_lang = '\n'.join(str(item) for item in google_trans_new.LANGUAGES.items())
    bot.send_message(message.chat.id, all_lang)


@bot.message_handler(commands=['lang_target'])
def request_on_change_language_target(message):
    bot.send_message(message.chat.id, "Please, select the language you want to translate your messages into")
    bot.register_next_step_handler(message, change_language_target)


def change_language_target(message):
    if message.text in google_trans_new.LANGUAGES.keys():
        update_language_target_for_user(message.from_user.id, message.text)
    else:
        print_all_language(message)
        request_on_change_language_target(message)


@bot.message_handler(commands=['lang_from'])
def request_on_change_language_from(message):
    bot.send_message(message.chat.id, "Please select the language from which you want to translate your messages.")
    bot.register_next_step_handler(message, change_language_from)


def change_language_from(message):
    if message.text in google_trans_new.LANGUAGES.keys():
        update_language_from_for_user(message.from_user.id, message.text)
    else:
        print_all_language(message)
        request_on_change_language_from(message)


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, f"Hello, {message.from_user.first_name}, I'm bot_translator")
    if message.from_user.id not in get_all_users():
        add_new_user(message.from_user.id)
        print_info(message)
        help_msg(message)


@bot.message_handler(commands=['info'])
def print_info(message):
    bot.send_message(message.chat.id, f"you are currently translating from {get_language_from(message.from_user.id)}"
                                           f" to {get_language_target(message.from_user.id)}")


@bot.message_handler(commands=['help'])
def help_msg(message):
    bot.send_message(message.chat.id, "/start if you are using the bot for the first time, then type this command")
    bot.send_message(message.chat.id, "/lang_target if you want to change the language you're translating into,"
                                      " then type this command")
    bot.send_message(message.chat.id, "/lang_from if you want to change the language you're translating from, "
                                      "then type this command")
    bot.send_message(message.chat.id, "/all_lang show all available languages")
    bot.send_message(message.chat.id, "/info getting information about a translating")
    bot.send_message(message.chat.id, "/translate if you want, then type this command or type you message")


def translate(message):
    bot.send_message(message.chat.id, translator.translate(message.text,
                                                           lang_tgt=get_language_target(message.from_user.id)))


@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.from_user.id not in get_all_users():
        welcome(message)
    translate(message)


bot.polling(none_stop=True)
