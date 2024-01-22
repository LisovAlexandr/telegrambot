import telebot
from currency_converter import CurrencyConverter
from telebot import types

bot = telebot.TeleBot('2120676466:AAGVrRy_TsAnFJDE1AlYktDlXCCiAmtVLks')
currency = CurrencyConverter() #create object
amount = 0

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Бот запустился, введите сумму')
    bot.register_next_step_handler(message, summ)

def summ(message):
    global amount
    try:
        amount = int(message.text.strip())
    except ValueError: # пользоваетль ввел текст вместо цифр
        bot.send_message(message.chat.id, 'Неверный формат. Введите сумму')
        bot.register_next_step_handler(message,summ)
        return  # следующее действие будет обработано этой же функцией summ

    if (amount > 0):
        markup = types.InlineKeyboardMarkup(row_width=2)  # две кнопки в ряду
        btn1 = types.InlineKeyboardButton('USD/EUR', callback_data='usd/eur')
        btn2 = types.InlineKeyboardButton('EUR/USD', callback_data='eur/usd')
        btn3 = types.InlineKeyboardButton('USD/GBP', callback_data='usd/gbp')
        btn4 = types.InlineKeyboardButton('Другое значение', callback_data='else')
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.chat.id,"Выберите пару валют", reply_markup=markup)
    else:
        bot.send_message(message.chat.id,"Число должны быть больше нуля")
        bot.register_next_step_handler(message,summ)

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data != 'else':
        values = call.data.upper().split('/')
        res = currency.convert(amount, values[0], values[1])
        bot.send_message(call.message.chat.id, f'Получается {round(res, 2)}. Можете вписать новую сумму для конвертации.')
        bot.register_next_step_handler(call.message, summ)
    else:
        bot.send_message(call.message.chat.id, 'Ввиедите пару значений через слэш / ')
        bot.register_next_step_handler(call.message, my_currency)

def my_currency(message):
    global amount
    try:
        values = message.text.upper().split('/')
        res = currency.convert(amount, values[0], values[1])
        bot.send_message(message.chat.id, f'Получается {round(res, 2)}. Можете вписать новую сумму для конвертации.')
        bot.register_next_step_handler(message, summ)
    except Exception:
        bot.send_message(message.chat.id, 'Что-то не так. Впишите значение заново')
        bot.register_next_step_handler(message, my_currency)  



bot.polling(none_stop=True)