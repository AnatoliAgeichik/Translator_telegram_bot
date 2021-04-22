import telebot
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

SECRET_KEY = os.environ.get("TOKEN")
bot = telebot.TeleBot(SECRET_KEY)


@bot.message_handler(commands=['start'])
def welcome(message):
    if message.from_user.language_code == 'ru':
        bot.send_message(message.chat.id, f"Привет, {message.from_user.first_name}, я бот переводчик")
    else:
        bot.send_message(message.chat.id, f"Hello, {message.from_user.first_name}, I'm bot_translator")


@bot.message_handler(commands=['help'])
def help_msg(message):
    bot.send_message(message.chat.id, "I can't do anything yet, but I'll soon learn how to translate messages)")


@bot.message_handler(content_types=['text'])
def handle_text(message):
    welcome(message)


bot.polling(none_stop=True)
