import telebot
import webbrowser
from telebot import types

bot=telebot.TeleBot("2120676466:AAGVrRy_TsAnFJDE1AlYktDlXCCiAmtVLks")
#test
@bot.message_handler(commands=["site","website"])
def site(message):
  webbrowser.open('https://google.com')
  #return redirect("http://www.google.com", code=302)


@bot.message_handler(commands=["start"])
def main(message):
  bot.send_message(message.chat.id, "you press start")
  
@bot.message_handler(content_types=['photo'])
def get_photo(message):
  markup = types.InlineKeyboardMarkup()
  markup.add(types.InlineKeyboardButton('перейти', url = "https://google.com"))
  markup.add(types.InlineKeyboardButton('удалить фото', callback_data = "delete"))
  markup.add(types.InlineKeyboardButton('изменить текст', callback_data = "edit"))
  bot.reply_to(message, 'good photo', reply_markup = markup)
  
@bot.message_handler()
def info(message):
  if message.text.lower()=='привет':
    bot.send_message(message.chat.id, f'простой текст Hi, {message.from_user.first_name} {message.from_user.last_name}')
  elif message.text.lower() == 'id':
    bot.reply_to(message,f'ID: {message.from_user.id}')
  else: 
    bot.send_message(message.chat.id, message.text)



  
bot.polling(none_stop=True)