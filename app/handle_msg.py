import telebot
import os
from dotenv import load_dotenv, find_dotenv
from google_trans_new import google_translator
import google_trans_new

translator = google_translator()

load_dotenv(find_dotenv())
bot = telebot.TeleBot(os.environ.get("TOKEN"))


def print_all_language(message):
    all_lang = '\n'.join([str(item) for item in google_trans_new.LANGUAGES.items()])
    bot.send_message(message.chat.id, f"{all_lang}")


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, f"Hello, {message.from_user.first_name}, I'm bot_translator")


@bot.message_handler(commands=['help'])
def help_msg(message):
    bot.send_message(message.chat.id, "/translate if you want, then type this command or type you message")


@bot.message_handler(commands=['translate'])
def choose_language(message):
    bot.send_message(message.chat.id, "What language do you want to translate into")
    bot.register_next_step_handler(message, get_text)


def get_text(message):
    global language_target
    if message.text in google_trans_new.LANGUAGES.keys():
        bot.send_message(message.chat.id, "what do you want me to translate for you")
        bot.register_next_step_handler(message, translate, message.text)
    else:
        print_all_language(message)
        choose_language(message)


def translate(message, language_taget):
    bot.send_message(message.chat.id, translator.translate(message.text, lang_tgt=language_taget))


@bot.message_handler(content_types=['text'])
def handle_text(message):
    welcome(message)


bot.polling(none_stop=True)
