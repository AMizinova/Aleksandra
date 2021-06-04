"""
Разработка умного помощника для выбора автомобилей ГАЗа в телеграмме
   Поключение чат бота к БД сайта ГАЗа, чтобы брать оттуда информацию по модельному ряду автомобилей (можно использовать json)
"""

import telebot
from telebot import types

bot = telebot.TeleBot('1764276505:AAH0ixmIK4HNo5yT470zagZkIwY0eaR0P8g')

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.from_user.id, "Привет, это Умный помощник! Я хочу помочь тебе с выбором! Для чего ты хочешь купить автомобиль?", reply_markup=sign_markup)


"""

   Появляются варианты ответа:
      "Перевозка людей",
      "Первезка грузов", 
      "Коммунальные машины", 
      "Бизнес"
   Пользователь выбирает один из вариантов
"""
sign_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
people = types.KeyboardButton('Перевозка людей')
goods = types.KeyboardButton('Перевозка грузов')
utility = types.KeyboardButton('Коммунальные машины')
business = types.KeyboardButton('Бизнес')
sign_markup.add(people, goods, utility, business)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/help":
       bot.send_message(message.from_user.id, "Напиши привет")
    elif  message.text == "Перевозка людей":
       bot.send_message(message.from_user.id, "Какая у вас категория прав?")
    elif  message.text == "Перевозка грузов":
       bot.send_message(message.from_user.id, "Какой у вас тип груза?")
    elif  message.text == "Коммунальные машины":
       bot.send_message(message.from_user.id, "Предлагаю такой выбор автомобилей")
    elif  message.text == "Бизнес":
       bot.send_message(message.from_user.id, "Предлагаю такой выбор автомобилей")
       
bot.polling()



   

   
"""
   
   Модельный ряд фильтруется в соответсвии с выбранным вариантом с помощью фильтра на питоне, либо сортировки
   
   Появляется второй вопрос (который зависит от предыдущего ответа)
   
   Пользователь отвечает на вопрос
   
   Модельный ряд фильтруется в соответсвии с выбранным вариантом
   
   Появляется третий вопрос (который зависит от предыдущего ответа)
   
   Пользователь отвечает на вопрос
   
   Модельный ряд фильтруется в соответсвии с выбранным вариантом
   
   Чат бот показал нужные модели автомобиля с картинками

ВЫ МОЛОДЦЫ

библиотека например такая telegram bot
нужны подсказки))

к сожалению пока не знаю какие функции буду использовать









"""