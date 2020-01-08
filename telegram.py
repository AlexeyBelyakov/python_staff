# import pytelegrambotapi
import telebot
import os

key_msg = "хуй"
short_key_msg = "ху"


def make_hui(str):
    words = str.split()
    if len(words) == 0:
        return key_msg
    word_to_return = words[-1]
    if len(word_to_return) < 3:
        return key_msg
    vowels = "АЕЁИОУЫЭЮЯ".lower()
    word_to_return = word_to_return.lower()
    if word_to_return[-3] in vowels:
        return short_key_msg + word_to_return[-3:]
    else:
        return key_msg + word_to_return[-2:]


if __name__ == '__main__':
    print(os.environ['BENDER_TOKEN'])
    bot = telebot.TeleBot(os.environ['BENDER_TOKEN'])

    @bot.message_handler(commands=['start'])
    def start_message(message):
        bot.send_message(message.chat.id, 'Привет, ты написал мне /start')

    @bot.message_handler(content_types=['text'])
    def send_text(message):
        print(message.chat.id, message.text)
        bot.send_message(message.chat.id, make_hui(message.text))

    bot.polling()
