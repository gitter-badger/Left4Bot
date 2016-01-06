#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Импортируем библиотеки
import config
import messages
import telebot
import time

# Создаём объект бота
Left4Bot = telebot.TeleBot(config.telegramToken)

# Ракция на стартовую команду
@Left4Bot.message_handler(commands=['start'])
def send_welcome(message):
	Left4Bot.send_message(message.chat.id, messages.start)

# Реакция на команду помощи
@Left4Bot.message_handler(commands=['help'])
def send_help(message):
	Left4Bot.send_message(message.chat.id, messages.help)

# Не спать!
Left4Bot.polling()
if __name__ == '__main__':
	Left4Bot.polling(none_stop = True)