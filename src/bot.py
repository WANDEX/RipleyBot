#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Main module."""
# t.me/RipleyBot
import os
import random

import telebot
from telebot.types import Message
from telebot import apihelper

file = open('src/token&proxy.txt', 'r')

TOKEN = [line for line in file if "BOT_TOKEN" in line]
PROXY = [line for line in file if "BOT_PROXY" in line]

# TOKEN = open('BOT_TOKEN')
# PROXY = os.environ.get('BOT_PROXY')
print(str(PROXY) + '\n' + str(TOKEN) + '\n')
apihelper.proxy = {'https': PROXY}

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message: Message):
    bot.reply_to(message, "Hi")


@bot.message_handler(func=lambda message: True)
def upper(message: Message):
    bot.reply_to(message, message.text.upper())


# bot.polling()
