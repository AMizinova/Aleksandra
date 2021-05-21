"""
Разработка умного помощника для выбора автомобилей ГАЗа в телеграмме
   Поключение чат бота к БД сайта ГАЗа, чтобы брать оттуда информацию по модельному ряду автомобилей (можно использовать json)
"""
import pdfminer
#извлечение текста из пдф
import io
 
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage
 
def extract_text_by_page(pdf_path):
    with open(pdf_path, 'rb') as fh:
        for page in PDFPage.get_pages(fh, 
                                      caching=True,
                                      check_extractable=True):
            resource_manager = PDFResourceManager()
            fake_file_handle = io.StringIO()
            converter = TextConverter(resource_manager, fake_file_handle)
            page_interpreter = PDFPageInterpreter(resource_manager, converter)
            page_interpreter.process_page(page)
 
            text = fake_file_handle.getvalue()
            yield text
 
            # close open handles
            converter.close()
            fake_file_handle.close()
 
def extract_text(pdf_path):
    for page in extract_text_by_page(pdf_path):
        print(page)
        print()
 
if __name__ == '__main__':
    print(extract_text('bd.pdf'))

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