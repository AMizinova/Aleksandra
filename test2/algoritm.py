"""
Разработка умного помощника для выбора автомобилей ГАЗа в телеграмме
   Поключение чат бота к БД сайта ГАЗа, чтобы брать оттуда информацию по модельному ряду автомобилей (можно использовать json)
"""
import pdfminer.six
#извлечение текста из пдф
import PyPDF2
with open('bd.pdf', 'rb') as pdf_file: pdf_reader = PyPDF2.PdfFileReader(pdf_file)
# printing first page contents 
pdf_page = pdf_reader.getPage(0) 
print(pdf_page.extractText()) 
# reading all the pages content one by one 
for page_num in range(pdf_reader.numPages): pdf_page = pdf_reader.getPage(page_num) 
print(pdf_page.extractText())

import telebot

bot = telebot.TeleBot('1814213523:AAFn5L9HQH6De-S7fQxbQTsJbTKaPxupN1M')

@bot.message_handler(commands=['start'])
def start_message(message):
    if message.text == "Привет":
       bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    elif message.text == "/help":
       bot.send_message(message.from_user.id, "Напиши привет")
    else:
       bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
print(message)

"""
   Пользователь заходит в чат бот
   
   Появляется вопрос "Какая цель покупки автомобиля?" 
   """
def start_message(message):
	bot.send_message(message.chat.id, 'Какая цель покупки автомобиля?')
print(message)


"""
 пока не знаю как сделать варианты ответа на питоне
   Появляются варианты ответа:
      "Перевозка людей",
      "Первезка грузов", 
      "Коммунальные машины", 
      "Бизнес"
   Пользователь выбирает один из вариантов
   
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