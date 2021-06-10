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
    but_1 = types.InlineKeyboardButton(text="Грузы", callback_data="Goods")
    but_2 = types.InlineKeyboardButton(text="Люди", callback_data="People")
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
        next_menu.add(but_5, but_6,but_7, but_8)
        bot.edit_message_text('Какая у вас категория прав?', call.message.chat.id, call.message.message_id,
                              reply_markup=next_menu)
		
    if call.data == 'Goods':
        next_menu1 = types.InlineKeyboardMarkup()
        but_9 = types.InlineKeyboardButton(text='Насыпной', callback_data='n1')
        but_10 = types.InlineKeyboardButton(text='Наливной', callback_data='n2')
        but_11 = types.InlineKeyboardButton(text='Опасные грузы', callback_data='n3')
        but_12 = types.InlineKeyboardButton(text='Паллетируемый', callback_data='n4')
        but_13 = types.InlineKeyboardButton(text='Спец. температура', callback_data='n5')
        next_menu1.add(but_9, but_10,but_11, but_12, but_13)
        bot.edit_message_text('Какой тип грузов Вы планируете перевозить?', call.message.chat.id, call.message.message_id,
                              reply_markup=next_menu1)
    if call.data == 'n3':
        bot.send_photo(call.message.chat.id, open('C:/Users/Alexandra/rudn/test2/уп/опасныегрузы.png', 'rb'))
        bot.send_message(call.message.chat.id, 'Для Вас подойдет автомобиль для перевозки газовых балонов на базе ГАЗЕЛЬ NEXT')
		
    if call.data == 'Utility':
        next_menu2 = types.InlineKeyboardMarkup()
        but_14 = types.InlineKeyboardButton(text='Уборочная', callback_data='k1')
        but_15 = types.InlineKeyboardButton(text='Техника с КМУ', callback_data='k2')
        but_16 = types.InlineKeyboardButton(text='Ассенизаторы', callback_data='k3')
        but_17 = types.InlineKeyboardButton(text='Дорожная', callback_data='k4')
        but_18 = types.InlineKeyboardButton(text='Транспортирующая', callback_data='k5')
        next_menu2.add(but_14, but_15,but_16, but_17, but_18)
        bot.edit_message_text('Какой техника Вам нужна?', call.message.chat.id, call.message.message_id,
                              reply_markup=next_menu2)
    if call.data == 'k1':
        bot.send_photo(call.message.chat.id, open('C:/Users/Alexandra/rudn/test2/уп/снегоуборщик.png', 'rb'))
        bot.send_message(call.message.chat.id, 'Для Вас подойдет АВТОМОБИЛЬ СНЕГОУБОРОЧНЫЙ НА БАЗЕ ГАЗЕЛЬ VALDAI')
    if call.data == 'k2':
        bot.send_photo(call.message.chat.id, open('C:/Users/Alexandra/rudn/test2/уп/кму.png', 'rb'))
        bot.send_message(call.message.chat.id, 'Для Вас подойдет АВТОМОБИЛЬ С КМУ ГАЗЕЛЬ NEXT')
    if call.data == 'k3':
        bot.send_photo(call.message.chat.id, open('C:/Users/Alexandra/rudn/test2/уп/ассенизатор.png', 'rb'))
        bot.send_message(call.message.chat.id, 'Для Вас подойдет АВТОМОБИЛЬ АССЕНИЗАТОР НА БАЗЕ ГАЗЕЛЬ СОБОЛЬ')
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
        next_menu3.add(but_19, but_20,but_21, but_22, but_23,but_24, but_25,but_26, but_27, but_28)
        bot.edit_message_text('Для какого бизнеса Вы планируете покупать автомобиль?', call.message.chat.id, call.message.message_id,
                              reply_markup=next_menu3)
    if call.data == 'b2':
        bot.send_photo(call.message.chat.id, open('C:/Users/Alexandra/rudn/test2/уп/эвакуатор.png', 'rb'))
        bot.send_message(call.message.chat.id, 'Для Вас подойдет ЭВАКУАТОР С ЛОМАНОЙ ПЛАТФОРМОЙ ГАЗЕЛЬ NEXT ')
    if call.data == 'b4':
        bot.send_photo(call.message.chat.id, open('C:/Users/Alexandra/rudn/test2/уп/вет.png', 'rb'))
        bot.send_message(call.message.chat.id, 'Для Вас подойдет автомобиль скорой ветеринарной помощи на шасси ГАЗЕЛЬ NEXT ')
    if call.data == 'b5':
        bot.send_photo(call.message.chat.id, open('C:/Users/Alexandra/rudn/test2/уп/инкас.png', 'rb'))
        bot.send_message(call.message.chat.id, 'Для Вас подойдет АВТОМОБИЛЬ ИНКАССАЦИЯ ГАЗЕЛЬ NEXT ')
    if call.data == 'b8':
        bot.send_photo(call.message.chat.id, open('C:/Users/Alexandra/rudn/test2/уп/брон.png', 'rb'))
        bot.send_message(call.message.chat.id, 'Для Вас подойдет БРОНИРОВАННЫЙ АВТОМОБИЛЬ ГАЗЕЛЬ NEXT ')
    if call.data == 'b10':
        bot.send_photo(call.message.chat.id, open('C:/Users/Alexandra/rudn/test2/уп/аэродром.png', 'rb'))
        bot.send_message(call.message.chat.id, 'Для Вас подойдет АЭРОДРОМНЫЙ АВТОМОБИЛЬ НА БАЗЕ ГАЗЕЛЬ NEXT ')
		
		
    if call.data == 'n1':
        level2 = types.InlineKeyboardMarkup()
        but_29 = types.InlineKeyboardButton(text='Промышленный', callback_data='prom')
        but_30 = types.InlineKeyboardButton(text='Строительный', callback_data='stroi')
        but_31 = types.InlineKeyboardButton(text='Продовольственный', callback_data='prod')
        level2.add(but_29, but_30,but_31)
        bot.edit_message_text('Уточните тип насыпного груза', call.message.chat.id, call.message.message_id,
                              reply_markup=level2)  
    if call.data == 'prom':
        bot.send_photo(call.message.chat.id, open('C:/Users/Alexandra/rudn/test2/уп/насыпной,промышл.png', 'rb'))
        bot.send_message(call.message.chat.id, 'Для Вас подойдет бортовой заднеприводный автомобиль Соболь Бизнес')  
    if call.data == 'stroi':
        bot.send_photo(call.message.chat.id, open('C:/Users/Alexandra/rudn/test2/уп/насыпнойстроит.png', 'rb'))
        bot.send_message(call.message.chat.id, 'Для Вас подойдет бортовой заднеприводный автомобиль Газель Next')  
    if call.data == 'prod':
        bot.send_photo(call.message.chat.id, open('C:/Users/Alexandra/rudn/test2/уп/насыпной,продов.png', 'rb'))
        bot.send_message(call.message.chat.id, 'Для Вас подойдет бортовой заднеприводный автомобиль Газель Next')  
        
    if call.data == 'n2':
        level22 = types.InlineKeyboardMarkup()
        but_32 = types.InlineKeyboardButton(text='Товары питания', callback_data='pit')
        but_33 = types.InlineKeyboardButton(text='Топливо', callback_data='toplivo')
        level22.add(but_32, but_33)
        bot.edit_message_text('Уточните тип наливного груза', call.message.chat.id, call.message.message_id,
                              reply_markup=level22)   
    if call.data == 'pit':
        bot.send_photo(call.message.chat.id, open('C:/Users/Alexandra/rudn/test2/уп/товары питания.png', 'rb'))
        bot.send_message(call.message.chat.id, 'Для Вас подойдет автоцистерна для молока ГАЗЕЛЬ БИЗНЕС')  
    if call.data == 'toplivo':
        bot.send_photo(call.message.chat.id, open('C:/Users/Alexandra/rudn/test2/уп/топливо.png', 'rb'))
        bot.send_message(call.message.chat.id, 'Для Вас подойдет автоцистерна для перевозки топлива ГАЗЕЛЬ БИЗНЕС и ГАЗЕЛЬ NEXT')  
        
    if call.data == 'n4':
        level23 = types.InlineKeyboardMarkup()
        but_34 = types.InlineKeyboardButton(text='Закрытый кузов', callback_data='Close')
        but_35 = types.InlineKeyboardButton(text='Открытый кузов', callback_data='Open')
        level23.add(but_34, but_35)
        bot.edit_message_text('Уточните тип паллетируемого груза', call.message.chat.id, call.message.message_id,
                              reply_markup=level23)   
    if call.data == 'Close':
        bot.send_photo(call.message.chat.id, open('C:/Users/Alexandra/rudn/test2/уп/закрытый.png', 'rb'))
        bot.send_message(call.message.chat.id, 'Для Вас подойдет европлатформа ГАЗЕЛЬ БИЗНЕС')   
    if call.data == 'Open':
        bot.send_photo(call.message.chat.id, open('C:/Users/Alexandra/rudn/test2/уп/открытый.png', 'rb'))
        bot.send_message(call.message.chat.id, 'Для Вас подойдет бортовой автомобиль ГАЗЕЛЬ БИЗНЕС')    
        
    if call.data == 'n5':
        level24 = types.InlineKeyboardMarkup()
        but_36 = types.InlineKeyboardButton(text='Продукты', callback_data='Product')
        but_37 = types.InlineKeyboardButton(text='Лекарства', callback_data='Drug')
        but_38 = types.InlineKeyboardButton(text='Цветы', callback_data='Flowers')
        level24.add(but_36, but_37, but_38)
        bot.edit_message_text('Для какого груза Вам необходима определенная температура?', call.message.chat.id, call.message.message_id,
                              reply_markup=level24) 
    if call.data == 'Product':
        bot.send_photo(call.message.chat.id, open('C:/Users/Alexandra/rudn/test2/уп/продукты.png', 'rb'))
        bot.send_message(call.message.chat.id, 'Для Вас подойдет изотермический фургон ГАЗЕЛЬ БИЗНЕС') 
    if call.data == 'Drug':
        bot.send_photo(call.message.chat.id, open('C:/Users/Alexandra/rudn/test2/уп/лекарства.png', 'rb'))
        bot.send_message(call.message.chat.id, 'Для Вас подойдет ГАЗЕЛЬ NEXT рефрижератор') 
    if call.data == 'Flowers':
        bot.send_photo(call.message.chat.id, open('C:/Users/Alexandra/rudn/test2/уп/цветы.png', 'rb'))
        bot.send_message(call.message.chat.id, 'Для Вас подойдет ГАЗЕЛЬ NEXT рефрижератор') 
        
    if call.data == 'k5':
        level25 = types.InlineKeyboardMarkup()
        but_39 = types.InlineKeyboardButton(text='Самосвал', callback_data='samosval')
        but_40 = types.InlineKeyboardButton(text='Мусоровоз', callback_data='trash')
        level25.add(but_39, but_40)
        bot.edit_message_text('Какой тип транспортирующих машин Вам нужен?', call.message.chat.id, call.message.message_id,
                              reply_markup=level25)
    if call.data == 'samosval':
        bot.send_photo(call.message.chat.id, open('C:/Users/Alexandra/rudn/test2/уп/самосвал.png', 'rb'))
        bot.send_message(call.message.chat.id, 'Для Вас подойдет АВТОСАМОСВАЛ С 3-Х СТОРОННЕЙ РАЗГРУЗКОЙ НА БАЗЕ ГАЗЕЛЬ-НЕКСТ 35127/35128') 
    if call.data == 'trash':
        bot.send_photo(call.message.chat.id, open('C:/Users/Alexandra/rudn/test2/уп/мусоровоз.png', 'rb'))
        bot.send_message(call.message.chat.id, 'Для Вас подойдет мусоровоз ГАЗЕЛЬ NEXT') 
		
    if call.data == 'k4':
        level26 = types.InlineKeyboardMarkup()
        but_41 = types.InlineKeyboardButton(text='Разметочная', callback_data='razmetka')
        but_42 = types.InlineKeyboardButton(text='Путеуборочная', callback_data='noway')
        level26.add(but_41, but_42)
        bot.edit_message_text('Какой тип дорожных машин Вам нужен?', call.message.chat.id, call.message.message_id,
                              reply_markup=level26)
    if call.data == 'razmetka':
        bot.send_photo(call.message.chat.id, open('C:/Users/Alexandra/rudn/test2/уп/разметочная.png', 'rb'))
        bot.send_message(call.message.chat.id, 'Для Вас подойдет маркировочный автомобиль Газель Бизнес') 
    if call.data == 'noway':
        bot.send_photo(call.message.chat.id, open('C:/Users/Alexandra/rudn/test2/уп/путеуборочная.png', 'rb'))
        bot.send_message(call.message.chat.id, 'Для Вас подойдет путеуборочный автомобиль Газель Бизнес') 
		
    if call.data == 'b1':
        level27 = types.InlineKeyboardMarkup()
        but_43 = types.InlineKeyboardButton(text='Автомагазин', callback_data='autoshop')
        but_44 = types.InlineKeyboardButton(text='Автокухня', callback_data='autokitchen')
        but_45 = types.InlineKeyboardButton(text='Мороженница', callback_data='icecream')
        but_46 = types.InlineKeyboardButton(text='Фудтрак', callback_data='Foodtrack')
        level27.add(but_43, but_44, but_45, but_46)
        bot.edit_message_text('Какая разновидность машины для торговли Вам нужна?', call.message.chat.id, call.message.message_id,
                              reply_markup=level27)
    if call.data == 'autoshop':
        bot.send_photo(call.message.chat.id, open('C:/Users/Alexandra/rudn/test2/уп/автомагазин.png', 'rb'))
        bot.send_message(call.message.chat.id, 'Для Вас подойдет АВТОМАГАЗИН ГАЗЕЛЬ NEXT')
    if call.data == 'autokitchen':
        bot.send_photo(call.message.chat.id, open('C:/Users/Alexandra/rudn/test2/уп/автокухня.png', 'rb'))
        bot.send_message(call.message.chat.id, 'Для Вас подойдет автокухня Газель Бизнес')
    if call.data == 'icecream':
        bot.send_photo(call.message.chat.id, open('C:/Users/Alexandra/rudn/test2/уп/морож.png', 'rb'))
        bot.send_message(call.message.chat.id, 'Для Вас подойдет мороженица Газель Бизнес')
    if call.data == 'Foodtrack':
        bot.send_photo(call.message.chat.id, open('C:/Users/Alexandra/rudn/test2/уп/фудтрак.png', 'rb'))
        bot.send_message(call.message.chat.id, 'Для Вас подойдет ДЛЯ МОБИЛЬНОЙ ТОРГОВЛИ ГАЗЕЛЬ NEXT')
		
		
    if call.data == 'b3':
        level28 = types.InlineKeyboardMarkup()
        but_47 = types.InlineKeyboardButton(text='Почта', callback_data='mail')
        but_48 = types.InlineKeyboardButton(text='Курьерская доставка', callback_data='delivery')
        level28.add(but_47, but_48)
        bot.edit_message_text('Какая разновидность машин для доставки Вам нужна?', call.message.chat.id, call.message.message_id,
                              reply_markup=level28)
    if call.data == 'mail':
        bot.send_photo(call.message.chat.id, open('C:/Users/Alexandra/rudn/test2/уп/почта.png', 'rb'))
        bot.send_message(call.message.chat.id, 'Для Вас подойдет почтовый автомобиль на базе Газель NEXT')
    if call.data == 'delivery':
        bot.send_photo(call.message.chat.id, open('C:/Users/Alexandra/rudn/test2/уп/курьер.png', 'rb'))
        bot.send_message(call.message.chat.id, 'Для Вас подойдет ЦЕЛЬНОМЕТАЛИЧЕСКИЙ ФУРГОН НА БАЗЕ ГАЗЕЛЬ NEXT и ГАЗЕЛЬ СОБОЛЬ')
    if call.data == 'b6':
        level29 = types.InlineKeyboardMarkup()
        but_49 = types.InlineKeyboardButton(text='Скорая', callback_data='emergency')
        but_50 = types.InlineKeyboardButton(text='Пожарная', callback_data='fire')
        but_51 = types.InlineKeyboardButton(text='Полиция', callback_data='police')
        level29.add(but_49, but_50, but_51)
        bot.edit_message_text('Какая тип машин Вам нужен??', call.message.chat.id, call.message.message_id,
                              reply_markup=level29)
    if call.data == 'emergency':
        bot.send_photo(call.message.chat.id, open('C:/Users/Alexandra/rudn/test2/уп/скорая.png', 'rb'))
        bot.send_message(call.message.chat.id, 'Для Вас подойдет АВТОМОБИЛЬ СКОРОЙ ПОМОЩИ ГАЗЕЛЬ NEXT КЛАССА B и АВТОМОБИЛЬ СКОРОЙ МЕДИЦИНСКОЙ ПОМОЩИ КЛАССА С')
    if call.data == 'fire':
        bot.send_photo(call.message.chat.id, open('C:/Users/Alexandra/rudn/test2/уп/пожарная.png', 'rb'))
        bot.send_message(call.message.chat.id, 'ПОЖАРНЫЙ АВТОМОБИЛЬ ГАЗЕЛЬ NEXT')
    if call.data == 'police':
        bot.send_photo(call.message.chat.id, open('C:/Users/Alexandra/rudn/test2/уп/полиция.png', 'rb'))
        bot.send_message(call.message.chat.id, 'Для Вас подойдет АВТОМОБИЛЬ ДЕЖУРНОЙ ЧАСТИ ГАЗЕЛЬ NEXT')

    if call.data == 'b7':
        level3 = types.InlineKeyboardMarkup()
        but_52 = types.InlineKeyboardButton(text='Труповоз', callback_data='body')
        but_53 = types.InlineKeyboardButton(text='Катафалк', callback_data='grave')
        level3.add(but_52, but_53)
        bot.edit_message_text('Какой тип машин Вам нужен??', call.message.chat.id, call.message.message_id,
                              reply_markup=level3)
    if call.data == 'body':
        bot.send_photo(call.message.chat.id, open('C:/Users/Alexandra/rudn/test2/уп/труп.png', 'rb'))
        bot.send_message(call.message.chat.id, 'Для Вас подойдет Санитарный автомобиль труповоз на шасси ГАЗЕЛЬ NEXT')
    if call.data == 'grave':
        bot.send_photo(call.message.chat.id, open('C:/Users/Alexandra/rudn/test2/уп/катаф.png', 'rb'))
        bot.send_message(call.message.chat.id, 'Для Вас подойдет катафалк на базе ГАЗЕЛЬ Соболь ')
                              
    if call.data == 'b9': 
        next_menu1 = types.InlineKeyboardMarkup()
        but_9 = types.InlineKeyboardButton(text='Насыпной', callback_data='n1')
        but_10 = types.InlineKeyboardButton(text='Наливной', callback_data='n2')
        but_11 = types.InlineKeyboardButton(text='Опасные грузы', callback_data='n3')
        but_12 = types.InlineKeyboardButton(text='Паллетируемый', callback_data='n4')
        but_13 = types.InlineKeyboardButton(text='Спец. температура', callback_data='n5')
        next_menu1.add(but_9, but_10,but_11, but_12, but_13)
        bot.edit_message_text('Какой тип грузов Вы планируете перевозить?', call.message.chat.id, call.message.message_id,
                              reply_markup=next_menu1)
    if call.data == 'b':
        level4 = types.InlineKeyboardMarkup()
        but_54 = types.InlineKeyboardButton(text='до 10 человек', callback_data='10')
        but_55 = types.InlineKeyboardButton(text='10-17 человек', callback_data='do17')
        level4.add(but_54, but_55)
        bot.edit_message_text('Сколько человек Вы планируете перевозить?', call.message.chat.id, call.message.message_id,
                              reply_markup=level4)
    if call.data == '10':
        level16 = types.InlineKeyboardMarkup()
        but_66 = types.InlineKeyboardButton(text='да', callback_data='da1')
        but_67 = types.InlineKeyboardButton(text='нет', callback_data='net1')
        level16.add(but_66, but_67)
        bot.edit_message_text('Планируете ли Вы перевозить детей?', call.message.chat.id, call.message.message_id,
                              reply_markup=level16)
    if call.data == 'da1':
        bot.send_photo(call.message.chat.id, open('C:/Users/Alexandra/rudn/test2/уп/до10длядетей.png', 'rb'))
        bot.send_message(call.message.chat.id, 'Для Вас подойдет ШКОЛЬНЫЙ АВТОБУС МАЛОГО КЛАССА СОБОЛЬ БИЗНЕС')
    if call.data == 'net1':
        bot.send_photo(call.message.chat.id, open('C:/Users/Alexandra/rudn/test2/уп/до10недлядетей.png', 'rb'))
        bot.send_message(call.message.chat.id, 'Для Вас подойдет автобусы НА БАЗЕ ГАЗЕЛЬ NEXT и ГАЗЕЛЬ СОБОЛЬ')
    if call.data == 'do17':
        level177 = types.InlineKeyboardMarkup()
        but_77 = types.InlineKeyboardButton(text='да', callback_data='da11')
        but_78 = types.InlineKeyboardButton(text='нет', callback_data='net11')
        level177.add(but_77, but_78)
        bot.edit_message_text('Планируете ли Вы перевозить детей?', call.message.chat.id, call.message.message_id,
                              reply_markup=level177)
    if call.data == 'da11':
        bot.send_photo(call.message.chat.id, open('C:/Users/Alexandra/rudn/test2/уп/17дети.png', 'rb'))
        bot.send_message(call.message.chat.id, 'Для Вас подойдет ШКОЛЬНЫЙ МИКРОАВТОБУС ГАЗЕЛЬ NEXT')
    if call.data == 'net11':
        bot.send_photo(call.message.chat.id, open('C:/Users/Alexandra/rudn/test2/уп/17недлядетей.png', 'rb'))
        bot.send_message(call.message.chat.id, 'Для Вас подойдет ПРИГОРОДНЫЙ И ГОРОДСКОЙ АВТОБУСЫ ГАЗЕЛЬ NEXT')
    
		
    if call.data == 'd':
        level5 = types.InlineKeyboardMarkup()
        but_56 = types.InlineKeyboardButton(text='18-30 человек', callback_data='ot18')
        but_57 = types.InlineKeyboardButton(text='более 30 человек', callback_data='posle30')
        level5.add(but_56, but_57)
        bot.edit_message_text('Сколько человек Вы планируете перевозить?', call.message.chat.id, call.message.message_id,
                              reply_markup=level5)
    if call.data == 'd1':
        level177 = types.InlineKeyboardMarkup()
        but_77 = types.InlineKeyboardButton(text='да', callback_data='da11')
        but_78 = types.InlineKeyboardButton(text='нет', callback_data='net11')
        level177.add(but_77, but_78)
        bot.edit_message_text('Планируется перевозка 10-17 человек. Планируете ли Вы перевозить детей?', call.message.chat.id, call.message.message_id,
                              reply_markup=level177)
							  
    if call.data == 'ot18':
        level7 = types.InlineKeyboardMarkup()
        but_60 = types.InlineKeyboardButton(text='да', callback_data='da11')
        but_61 = types.InlineKeyboardButton(text='нет', callback_data='net11')
        level7.add(but_60, but_61)
        bot.edit_message_text('Планируете ли Вы перевозить детей?', call.message.chat.id, call.message.message_id,
                              reply_markup=level7)
    
		
    if call.data == 'posle30':
        level8 = types.InlineKeyboardMarkup()
        but_62 = types.InlineKeyboardButton(text='да', callback_data='da13')
        but_63 = types.InlineKeyboardButton(text='нет', callback_data='net13')
        level8.add(but_62, but_63)
        bot.edit_message_text('Планируете ли Вы перевозить детей?', call.message.chat.id, call.message.message_id,
                              reply_markup=level8)
    if call.data == 'da13':
        bot.send_photo(call.message.chat.id, open('C:/Users/Alexandra/rudn/test2/уп/30дети.png', 'rb'))
        bot.send_message(call.message.chat.id, 'Для Вас подойдет АВТОБУС КАВЗ-4235/4238 ШКОЛЬНЫЙ')
    
    if call.data == 'net13':
        level9 = types.InlineKeyboardMarkup()
        but_64 = types.InlineKeyboardButton(text='Междугородние перевозки', callback_data='betweencity')
        but_65 = types.InlineKeyboardButton(text='Перевозки по городу', callback_data='incity')
        level9.add(but_64, but_65)
        bot.edit_message_text('Выберете назначение автобусов?', call.message.chat.id, call.message.message_id,
                              reply_markup=level9)
    if call.data == 'betweencity':
        bot.send_photo(call.message.chat.id, open('C:/Users/Alexandra/rudn/test2/уп/междугородний.png', 'rb'))
        bot.send_message(call.message.chat.id, 'Для Вас подойдет автобус ЛИАЗ ВОЯЖ 525110')
    if call.data == 'incity':
        bot.send_photo(call.message.chat.id, open('C:/Users/Alexandra/rudn/test2/уп/городской.png', 'rb'))
        bot.send_message(call.message.chat.id, 'Для Вас подойдет автобус ЛИАЗ-5292 РЕСТАЙЛИНГ')
							  
	
    
    if call.data == 'doncare':
        level20 = types.InlineKeyboardMarkup()
        but_54 = types.InlineKeyboardButton(text='до 10 человек', callback_data='10')
        but_55 = types.InlineKeyboardButton(text='10-17 человек', callback_data='do17')
        but_56 = types.InlineKeyboardButton(text='18-30 человек', callback_data='ot18')
        but_57 = types.InlineKeyboardButton(text='более 30 человек', callback_data='posle30')       
        level20.add(but_54, but_55, but_56, but_57)
        bot.edit_message_text('Выберете количество человек?', call.message.chat.id, call.message.message_id,
                              reply_markup=level20)
        
        
bot.polling()


   
  






