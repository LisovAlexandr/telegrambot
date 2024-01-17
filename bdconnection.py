import sqlite3
import telebot

bot = telebot.TeleBot('2120676466:AAGVrRy_TsAnFJDE1AlYktDlXCCiAmtVLks')
name = ""

@bot.message_handler(commands=['start'])
def start(message):
    conn = sqlite3.connect('bdusers.sql')   #открыть БД
    cur = conn.cursor()   #установить курсор

    cur.execute('CREATE TABLE IF NOT EXISTS users (id int auto_increment primary key, name varchar(50), pass varchar(50))') #подготовка запроса для создания бд
    conn.commit()  #команда фиксирует изменения
    cur.close()  #close cur
    conn.close()  #cloae BD

    bot.send_message(message.chat.id,"Регистрация пользователя, введите имя")
    bot.register_next_step_handler(message, user_name)

def user_name(message):
    global name
    name = message.text.strip()
    bot.send_message(message.chat.id,"Введите пароль")
    bot.register_next_step_handler(message, user_pass)

def user_pass(message):
    password = message.text.strip()
    conn = sqlite3.connect('bdusers.sql')   #connect bd
    cur = conn.cursor()

    cur.execute("INSERT INTO users (name, pass) VALUES ('%s', '%s')" % (name, password))
    conn.commit()
    cur.close()
    conn.close()
    
    markup = telebot.types.InlineKeyboardMarkup()  #не импортируем types, а используем telebot
    markup.add(telebot.types.InlineKeyboardButton('Список пользователей', callback_data='users'))
    bot.send_message(message.chat.id,"Пользователь зарегистрирован", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    conn = sqlite3.connect('bdusers.sql')   #connect bd
    cur = conn.cursor()

    cur.execute("SELECT * FROM users")
    users = cur.fetchall()  # вернуть все значения

    info = ""
    for el in users:
        info += f'Имя: {el[1]}, пароль: {el[2]}\n' # формируется список

    cur.close()
    conn.close()

    bot.send_message(call.message.chat.id, info)   # вывод списка пользователей

bot.polling(none_stop=True)