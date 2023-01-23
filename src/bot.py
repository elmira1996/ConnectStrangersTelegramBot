import os

import telebot
from loguru import logger
import emoji

from utils.io import write_json
from constants import keyboards




class Bot:
    def __init__(self):
        self.bot = telebot.TeleBot(os.environ['Strangers_Bot_Token'])
        self.send_welcome = self.bot.message_handler(
            commands=['start', 'help']
            )(self.send_welcome)
        self.echo_all = self.bot.message_handler(
            func=lambda message: True
            )(self.echo_all)


    def send_welcome(self, message):
        self.bot.reply_to(message, 'Hi! how can i help you?')

    def echo_all(self, message):
        write_json(message.json, 'message.json')
        print(emoji.demojize(message.text))
        self.bot.send_message(
            message.chat.id, message.text, 
            reply_markup = keyboards.main
        ) 

    def run(self):
        logger.info('Bot is runung...')
        self.bot.infinity_polling()

if __name__ == '__main__':
    logger.info('Bot Started')
    bot = Bot()
    bot.run()
