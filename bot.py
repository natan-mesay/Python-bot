import telebot
from telebot import types
import pandas as pd

TOKEN = '6581876666:AAGfw0C_sahN5IZc_q7ZMSFKTsYEl4-JgVM'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome_message(message):
    bot.send_message(message.chat.id, message.from_user.username)

@bot.message_handler(commands=['show'])
def handle_csv_command(message):
    data = pd.read_csv('/home/nat/Downloads/input.csv')
    print(data.iloc[0])
    bot.send_message(message.chat.id, data)


@bot.message_handler(commands=['hello'])
def send_welcome_message(message):
    user_name = message.from_user.username
    bot.send_message(message.chat.id, f"Hello, {user_name}!")

bot.polling()
