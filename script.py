import telebot
import webbrowser
from telebot import types
import sqlite3

bot=telebot.TeleBot("2120676466:AAGVrRy_TsAnFJDE1AlYktDlXCCiAmtVLks")

#подключение БД sqlite3 


#test
#кнопки на поле ввода 
@bot.message_handler(commands=['start'])
def start(message):
  markup = types.ReplyKeyboardMarkup()
  btn1 = types.KeyboardButton('перейти')
  btn2 = types.KeyboardButton('удалить фото')
  btn3 = types.KeyboardButton('изменить текст')
  markup.row(btn1)
  markup.row(btn2,btn3)
  file = open('./img.jpg','rb')
  bot.send_photo(message.chat.id, file, reply_markup=markup)
  bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}', reply_markup=markup)
  bot.register_next_step_handler(message, on_click)

def on_click(message):
  if message.text.lower() == 'перейти':
    bot.send_message(message.chat.id,'Перехожу на сайт...')
  elif message.text.lower() == 'удалить фото':
    bot.send_message(message.chat.id,'удалено...')

##### не работает переход на сайт по команде
@bot.message_handler(commands=["site","website"])
def site(message):
  webbrowser.open('https://google.com')
  #return redirect("http://www.google.com", code=302)


@bot.message_handler(commands=["start"])
def main(message):
  bot.send_message(message.chat.id, "you press start")
  
# кнопки возле сообщений  
@bot.message_handler(content_types=['photo'])
def get_photo(message):
  markup = types.InlineKeyboardMarkup()
  #v1
  #markup.add(types.InlineKeyboardButton('перейти', url = "https://google.com"))
  #markup.add(types.InlineKeyboardButton('удалить фото', callback_data = "delete"))
  #markup.add(types.InlineKeyboardButton('изменить текст', callback_data = "edit"))
  #v2
  btn1 = types.InlineKeyboardButton('перейти', url = "https://google.com")
  btn2 = types.InlineKeyboardButton('удалить фото', callback_data = "delete")
  btn3 = types.InlineKeyboardButton('изменить текст', callback_data = "edit")
  markup.row(btn1)
  markup.row(btn2,btn3)
  bot.reply_to(message, 'good photo', reply_markup = markup)
  
@bot.message_handler()
def info(message):
  if message.text.lower()=='привет':
    bot.send_message(message.chat.id, f'простой текст Hi, {message.from_user.first_name} {message.from_user.last_name}')
  elif message.text.lower() == 'id':
    bot.reply_to(message,f'ID: {message.from_user.id}')
  else: 
    bot.send_message(message.chat.id, message.text)

@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
  if callback.data == 'delete':
    bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
  elif callback.data == 'edit':
    bot.edit_message_text('Edit text', callback.message.chat.id, callback.message.message_id)

  
bot.polling(none_stop=True)