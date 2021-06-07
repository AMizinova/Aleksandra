"""
Разработка умного помощника для выбора автомобилей ГАЗа в телеграмме
   Поключение чат бота к БД сайта ГАЗа, чтобы брать оттуда информацию по модельному ряду автомобилей (можно использовать json)
"""

import telebot
from telebot import types

bot = telebot.TeleBot('1764276505:AAH0ixmIK4HNo5yT470zagZkIwY0eaR0P8g')
    
@bot.message_handler(commands=["start"])
def Inline(message):
    key = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton(text="Перевозка грузов", callback_data="Goods")
    but_2 = types.InlineKeyboardButton(text="Перевозка людей", callback_data="People")
    but_3 = types.InlineKeyboardButton(text="Коммунальные машины", callback_data="Utility")
    but_4 = types.InlineKeyboardButton(text="Бизнес", callback_data="Business")
    key.add(but_1, but_2, but_3, but_4)
    bot.send_message(message.chat.id, "Привет, это Умный помощник! Я хочу помочь тебе с выбором! Для чего ты хочешь купить автомобиль?", reply_markup=key)
    
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == 'People':
        next_menu = types.InlineKeyboardMarkup()
        but_5 = types.InlineKeyboardButton(text='B/B1', callback_data='b')
        but_6 = types.InlineKeyboardButton(text='D', callback_data='d')
        but_7 = types.InlineKeyboardButton(text='D1', callback_data='d1')
        but_8 = types.InlineKeyboardButton(text='Не важно', callback_data='doncare')
        back = types.InlineKeyboardButton(text='Назад', callback_data='key')
        next_menu.add(but_5, but_6,but_7, but_8, back)
        bot.edit_message_text('Какая у вас категория прав?', call.message.chat.id, call.message.message_id,
                              reply_markup=next_menu)
    if call.data == 'Goods':
        next_menu1 = types.InlineKeyboardMarkup()
        but_9 = types.InlineKeyboardButton(text='Насыпной', callback_data='n1')
        but_10 = types.InlineKeyboardButton(text='Наливной', callback_data='n2')
        but_11 = types.InlineKeyboardButton(text='Опасные грузы', callback_data='n3')
        but_12 = types.InlineKeyboardButton(text='Паллетируемый', callback_data='n4')
        but_13 = types.InlineKeyboardButton(text='Спец. температура', callback_data='n5')
        back = types.InlineKeyboardButton(text='Назад', callback_data='key')
        next_menu1.add(but_9, but_10,but_11, but_12, but_13, back)
        bot.edit_message_text('Какой тип грузов Вы планируете перевозить?', call.message.chat.id, call.message.message_id,
                              reply_markup=next_menu1)
    if call.data == 'Utility':
        next_menu2 = types.InlineKeyboardMarkup()
        but_14 = types.InlineKeyboardButton(text='Уборочная', callback_data='k1')
        but_15 = types.InlineKeyboardButton(text='Техника с КМУ', callback_data='k2')
        but_16 = types.InlineKeyboardButton(text='Ассенизаторы', callback_data='k3')
        but_17 = types.InlineKeyboardButton(text='Дорожная', callback_data='k4')
        but_18 = types.InlineKeyboardButton(text='Транспортирующая', callback_data='k5')
        back = types.InlineKeyboardButton(text='Назад', callback_data='key')
        next_menu2.add(but_14, but_15,but_16, but_17, but_18, back)
        bot.edit_message_text('Какой техника Вам нужна?', call.message.chat.id, call.message.message_id,
                              reply_markup=next_menu2)
    if call.data == 'Business':
        next_menu3 = types.InlineKeyboardMarkup()
        but_19 = types.InlineKeyboardButton(text='Торговля', callback_data='b1')
        but_20 = types.InlineKeyboardButton(text='Аварийный', callback_data='b2')
        but_21 = types.InlineKeyboardButton(text='Доставка', callback_data='b3')
        but_22 = types.InlineKeyboardButton(text='Ветеринарная', callback_data='b4')
        but_23 = types.InlineKeyboardButton(text='Инкассатор', callback_data='b5')
        but_24 = types.InlineKeyboardButton(text='Спасательный', callback_data='b6')
        but_25 = types.InlineKeyboardButton(text='Ритуальный', callback_data='b7')
        but_26 = types.InlineKeyboardButton(text='Охрана', callback_data='b8')
        but_27 = types.InlineKeyboardButton(text='Логистика', callback_data='b9')
        but_28 = types.InlineKeyboardButton(text='Аэродром', callback_data='b10')
        back = types.InlineKeyboardButton(text='Назад', callback_data='key')
        next_menu3.add(but_19, but_20,but_21, but_22, but_23,but_24, but_25,but_26, but_27, but_28, back)
        bot.edit_message_text('Для какого бизнеса Вы планируете покупать автомобиль?', call.message.chat.id, call.message.message_id,
                              reply_markup=next_menu3)
                                                          
                                  

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