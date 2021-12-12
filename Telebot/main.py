import telebot
import os

API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['Greet'])

def greet(message):
    bot.reply_to(message, 'Hey! hows it going!! ')
    
bot.polling()