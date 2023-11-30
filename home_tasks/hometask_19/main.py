import telebot
from telebot import types
import flag
import requests
from decimal import Decimal

bot = telebot.TeleBot('6964459550:AAEk0UmAZ6wEhLFKHwFVbdAx14zWuqjQlgE')  
FIXER_API_KEY = 'ed17b36278a6f11780ac0895e272d8b1'
FIXER_API_URL = f'http://data.fixer.io/api/latest?access_key={FIXER_API_KEY}'

try:
    response = requests.get(FIXER_API_URL)
    response.raise_for_status()  
    data = response.json()
    rate_usd_to_eur = Decimal(data['rates']['USD'])
    rate_uah_to_eur = Decimal(data['rates']['UAH'])
    rate_pln_to_eur = Decimal(data['rates']['PLN'])
except requests.RequestException as e:
    print(f'Failed to fetch data from API: {e}')
    raise SystemExit(1)  

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_usd = types.KeyboardButton(f'{flag.flag("US")} USD >> UAH')
    btn_eur = types.KeyboardButton(f'{flag.flag("UA")} EURO >> UAH')
    btn_pln = types.KeyboardButton(f'{flag.flag("PL")} PLN >> UAH')
    markup.row(btn_usd, btn_eur, btn_pln)
    bot.send_message(message.chat.id, 'hello )', reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def on_click(message):
    try:
        if message.text == f'{flag.flag("US")} USD >> UAH':
            rate = rate_uah_to_eur / rate_usd_to_eur
            bot.send_message(message.chat.id, f'1 USD = {rate:.2f} UAH')
        elif message.text == f'{flag.flag("UA")} EURO >> UAH':
            rate = rate_uah_to_eur
            bot.send_message(message.chat.id, f'1 EUR = {rate:.2f} UAH')
        elif message.text == f'{flag.flag("PL")} PLN >> UAH':
            rate = rate_uah_to_eur / rate_pln_to_eur
            bot.send_message(message.chat.id, f'1 PLN = {rate:.2f} UAH')
    except ZeroDivisionError:
        bot.send_message(message.chat.id, 'Error: Division by zero')

bot.polling(none_stop=True)

