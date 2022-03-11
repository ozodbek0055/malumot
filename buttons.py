import aiogram
from aiogram import Bot, Dispatcher, executor,types
import logging
import wikipedia
from  aiogram.types import KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup


uz = InlineKeyboardButton(text='🇺🇿UZ', callback_data='uz')
ru = InlineKeyboardButton(text='🇷🇺RU', callback_data='ru')
en = InlineKeyboardButton(text='🇬🇧EN', callback_data='en')
inl = InlineKeyboardMarkup(row_width=3).add(uz, ru, en)

qayta = ReplyKeyboardMarkup(resize_keyboard=True).add("Tilni o'zgartirish🔁")