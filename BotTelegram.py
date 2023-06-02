import telebot, requests, os, re, glob
from telebot import types

bot = telebot.TeleBot('6149957194:AAHvsUnLJPLMWzxHPUQik6dhqxRSZziuV0w')
requests.get('https://t.me/@TestMapInChatBot')

groups = [1158889635, -1001742179859]  # chat id
dict = {'Приморья': 'https://192.168.233.171:25443/', 'НСО': 'http://192.168.233.169:3980/',
        'Ростова': 'http://192.168.233.98:61027/', 'Курска': 'http://192.168.234.14:7280/',
        'Сахалина': 'http://192.168.233.170:8080/', 'Хабаровска': 'http://192.168.233.222:2780/',
        'Алании': 'http://192.168.234.31:1580/'}

@bot.message_handler(func=lambda message: message.chat.id not in groups)
def some(message):
    bot.send_message(message.chat.id, 'Доступ ограничен')

def remove_pic(name):
    try:
        os.remove("".join(glob.glob('./Results/'+name+'/*')))
    except Exception:
        pass

def send_pic(message, name):
    try:
        a = open('./Results/'+name+'/Авторизация.png', 'rb')
        bot.send_photo(message.chat.id, a)
    except Exception:
        pass
    try:
        b = open('./Results/'+name+'/Дневник.png', 'rb')
        bot.send_photo(message.chat.id, b)
    except Exception:
        pass
    try:
        c = open('./Results/'+name+'/Расписание.png', 'rb')
        bot.send_photo(message.chat.id, c)
    except Exception:
        pass
    try:
        d = open('./Results/'+name+'/Госпитализация.png', 'rb')
        bot.send_photo(message.chat.id, d)
    except Exception:
        pass
    try:
        i = open('./Results/'+name+'/Поиск.png', 'rb')
        bot.send_photo(message.chat.id, i)
    except Exception:
        pass

def autotest_prod(message, test_name, address):
    bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id, text="🔴Начата проверка крит. модулей продуктивного стенда <a href='"+address+"'>"'<u><b>'+test_name+'</b></u>'"</a>", parse_mode='html')
    remove_pic('Results_sc')
    os.system('pytest --testit -s '+test_name+'.py > Results/Results.log')  # команда запуска скрипта test.py и запись результата в файл logs.txt
    with open('Results/Results.log', 'r', -1, 'utf-8') as fi:
        f = fi.read()[245:1028]  # отчет о тестировании
        opt_1 = re.sub(r'\s[.]', '\n', f)  # удаление точек в логах
        opt_2 = re.sub(r'\D[=]', ' ', opt_1)  # редактирование последней строчки
        opt_3 = re.sub(r'\D[=]', ' ', opt_2)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id, text="🟢Закончена проверка крит. модулей продуктивного стенда <a href='"+address+"'><u><b>"+test_name+"🔽</b></u></a>", parse_mode='html')
    bot.send_message(message.chat.id, opt_3)
    send_pic(message, 'Results_sc')

@bot.message_handler(commands=["start"])
def any_msg(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text="Приморский край", callback_data="Приморья")
    btn2 = types.InlineKeyboardButton(text="Новосибирская область", callback_data="НСО")
    btn3 = types.InlineKeyboardButton(text="Ростовская область", callback_data="Ростова")
    btn4 = types.InlineKeyboardButton(text="Курская область", callback_data="Курска")
    btn5 = types.InlineKeyboardButton(text="РСО-Алания", callback_data="Алании")
    markup.add(btn1)
    markup.add(btn2)
    markup.add(btn3)
    markup.add(btn4)
    markup.add(btn5)
    bot.send_message(message.chat.id, "Выберите регион/отдельного клиента, для тестирования\nкрит. модулей продуктивного стенда сервиса - МИС", reply_markup=markup)

@bot.message_handler(commands=["help"])
def help_msg(message):
    bot.send_message(message.chat.id, '<b>Правила по эксплуатации бота:\n * нельзя запускать несколько тестов подряд\n * если возникла проблема во время создании записи/тестовго пациента - самостоятельно удалить запись/тестовго пациента**\n * пользоваться ботом только в чате - "PROD AUTO-TEST (DutySC)"\n * в случае возникновении вопросов/предложений обращаться через "Контакты"\n\nРазработчик - Ахтямов Тимур (@ELCUY)\nРуководитель отдела - Григорий Ефремов (@greegree)</b>', parse_mode='html')


@bot.callback_query_handler(func=lambda call: True)
def callback_inline_1(call):
    # Если сообщение из чата с ботом
    if call.message:
        if call.data == call.data:
            autotest_prod(call.message, test_name=call.data, address=dict[call.data])
        else:
            print('Не имеет функционала')
            pass


# #Тестирование кнопки назад
# @bot.message_handler(commands=["start","help"])
# def welcome(message):
#     hello = bot.send_message(message.chat.id,"Приветсвую вас меня зовут Бот!")
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     mrk = types.KeyboardButton("Каталог", callback_data='katalog')
#     mrk1 = types.KeyboardButton("Корзина", callback_data='cart')
#     markup.add(mrk,mrk1)
#     bot.send_message(message.chat.id, "Выберите в меню,что вам интересно", reply_markup=markup)
# @bot.callback_query_handler(func=lambda call: True)
# def answer(call):
#     if call.data == 'katalog':
#     markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     mar = types.KeyboardButton("Одежда", callback_data=odezda)
#     mar2 = types.KeyboardButton("Назад в меню", callback_data=back)
#     markup1.add(mar,mar2)
#     bot.send_message(message.chat.id,"Выберите,что вам нужно,если хотите вернуться в меню просто нажмите кнопку 'Назад в меню' ",reply_markup=markup1)
#     elif call.data == 'cart':
#         # Что то
#     elif call.data == 'back':
#         bot.send_message(message.chat.id, "Вы вернулись в меню",reply_markup=None)

# @bot.message_handler(commands=['start'])
# def start(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     btn1 = types.KeyboardButton('Начать работу')
#     btn2 = types.KeyboardButton('Не, попозже')
#     markup.add(btn1, btn2)
#     bot.send_message(message.chat.id, f'🤚🏻Привет, <b>{message.from_user.first_name} {message.from_user.last_name}</b>, стартуем?)', parse_mode='html', reply_markup=markup)

# @bot.message_handler(content_types=['text'])
# def get_text_messages(message):
#     if message.text == 'Начать работу':
#         markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
#         btn1 = types.KeyboardButton('Тест Приморья')
#         btn2 = types.KeyboardButton('Тест Новосибирска')
#         btn3 = types.KeyboardButton('Тест Курска')
#         btn4 = types.KeyboardButton('Тест Ростова')
#         btn5 = types.KeyboardButton('Coming soon')
#         # btn3 = types.KeyboardButton('Coming soon')
#         markup.add(btn1, btn2, btn3, btn4, btn5)
#         bot.send_message(message.chat.id, 'Выберите Регион', reply_markup=markup) #ответ бота
#
#     elif message.text == 'Не, попозже':
#         bot.send_message(message.chat.id, 'Тогда иди работай) или может...', parse_mode='Markdown')
# ########################################################################################################################
#     elif message.text == 'Тест Приморья':
#         remove_pic('PK_sc')
#         bot.send_message(message.chat.id, '🔴Начата проверка крит. модулей продуктивного стенда - Приморья 🔽')
#         os.system('pytest -s Приморья.py > Results/PK.log')  # команда запуска скрипта Приморья.py и запись результата в файл logs.txt
#         with open('Results/PK.log', 'r', -1, 'utf-8') as fi:
#             f = fi.read()[186:1100]  # отчет о тестировании
#             opt_1 = re.sub(r'\s[.]', '\n', f) #удаление точек в логах
#             opt_2 = re.sub(r'\D[=]', '', opt_1)  # редактирование последней строчки
#             opt_3 = re.sub(r'\D[=]', '', opt_2)
#         bot.send_message(message.chat.id, opt_3)  # ответ бота с выводом результата тестирования
#         send_pic(message, 'PK_sc')
# ########################################################################################################################
#     elif message.text == 'Тест Новосибирска':
#         remove_pic('NSO_sc')
#         bot.send_message(message.chat.id, '🔴Начата проверка крит. модулей продуктивного стенда - НСО 🔽')
#         os.system('pytest -s НСО.py > Results/NSO.log')  # команда запуска скрипта НСО.py и запись результата в файл logs.txt
#         with open('Results/NSO.log', 'r', -1, 'utf-8') as fi:
#             f = fi.read()[186:1100]  # отчет о тестировании
#             opt_1 = re.sub(r'\s[.]', '\n', f)
#             opt_2 = re.sub(r'\D[=]', '', opt_1) #редактирование последней строчки
#             opt_3 = re.sub(r'\D[=]', '', opt_2)
#         bot.send_message(message.chat.id, opt_3)  # ответ бота с выводом результата тестирования
#         send_pic(message, 'NSO_sc')
# ########################################################################################################################
#     elif message.text == 'Тест Курска':
#         remove_pic('KURO_sc')
#         bot.send_message(message.chat.id, '🔴Начата проверка крит. модулей продуктивного стенда - Курска 🔽')
#         os.system('pytest -s Курска.py > Results/KURO.log')  # команда запуска скрипта Курска.py и запись результата в файл logs.txt
#         with open('Results/KURO.log', 'r', -1, 'utf-8') as fi:
#             f = fi.read()[186:1100]  # отчет о тестировании
#             opt_1 = re.sub(r'\s[.]', '\n', f)
#             opt_2 = re.sub(r'\D[=]', '', opt_1) #редактирование последней строчки
#             opt_3 = re.sub(r'\D[=]', '', opt_2)
#         bot.send_message(message.chat.id, opt_3)  # ответ бота с выводом результата тестирования
#         send_pic(message, 'KURO_sc')
# ########################################################################################################################
#     elif message.text == 'Тест Ростова':
#         remove_pic('RO_sc')
#         bot.send_message(message.chat.id, '🔴Начата проверка крит. модулей продуктивного стенда - Ростова 🔽')
#         os.system('pytest -s Ростова.py > Results/RO.log')  # команда запуска скрипта Ростова.py и запись результата в файл logs.txt
#         with open('Results/RO.log', 'r', -1, 'utf-8') as fi:
#             f = fi.read()[186:1100]  # отчет о тестировании
#             opt_1 = re.sub(r'\s[.]', '\n', f)
#             opt_2 = re.sub(r'\D[=]', '', opt_1) #редактирование последней строчки
#             opt_3 = re.sub(r'\D[=]', '', opt_2)
#         bot.send_message(message.chat.id, opt_3)  # ответ бота с выводом результата тестирования
#         send_pic(message, 'RO_sc')
# ########################################################################################################################
#     elif message.text == 'Coming soon':
#         bot.send_message(message.chat.id, 'Данный тест еще не готов', parse_mode='Markdown')

    # elif message.text == 'Будущие стенды':
    #     bot.send_message(message.from_user.id, 'Будущие стенды', parse_mode='Markdown')

# bot.polling(none_stop=True, interval=0)
bot.infinity_polling(none_stop=True)
# bot.polling(none_stop=True, timeout=123)