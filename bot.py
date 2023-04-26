import os
import requests
import telebot
import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

BOT_TOKEN = os.environ.get('6227110303:AAGQxtr1OCXC_iddfxrorR08K0LmhXHF3Zw')
bot = telebot.TeleBot('6227110303:AAGQxtr1OCXC_iddfxrorR08K0LmhXHF3Zw')

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")
    
@bot.message_handler(commands=['bye', 'byee'])
def send_welcome(message):
    bot.reply_to(message, "Have a nice day !!s")
    
@bot.message_handler(commands=['joke'])
def get_random_joke(message):
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)
    if response.status_code == 200:
        joke = response.json()
        bot.reply_to(message, f"{joke['setup']}\n\n{joke['punchline']}")
    else:
        bot.reply_to(message.chat.id, "Failed to retrieve joke")

@bot.message_handler(commands=['bitcoin'])
def bitcone(message):
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        time = data['time']['updated']
        bpi = data['bpi']

        # Construct the message to send back to the user
        response_message = f"Time: {time}\n\n"

        for currency, details in bpi.items():
            rate = details['rate']
            desc = details['description']
            response_message += f"{currency}:  {rate}  ({desc})\n"

        # Send the message back to the user
        bot.send_message(chat_id=message.chat.id, text=response_message)

    else:
        bot.send_message(chat_id=message.chat.id, text="Error: Failed to retrieve data")

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)
    


    

bot.infinity_polling()
