#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Main module."""
# t.me/RipleyBot
import os
import random

import telebot
from telebot.types import Message
from telebot import apihelper

file = open('temp/token&proxy.txt', 'r')

TOKEN = file.readline()[10:-1]  # BOT_TOKEN=
PROXY = file.readline()[10:-1]  # BOT_PROXY=
print("\nTOKEN:{0}\nPROXY:{1}".format(TOKEN, PROXY))

apihelper.proxy = {'https': PROXY}
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message: Message):
    bot.reply_to(message, "Hi")


@bot.message_handler(func=lambda message: True)
def upper(message: Message):
    bot.reply_to(message, message.text.upper())


bot.polling()
