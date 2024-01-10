import telebot
import webbrowser

bot=telebot.TeleBot("2120676466:AAGVrRy_TsAnFJDE1AlYktDlXCCiAmtVLks")

@bot.message_handler(commands=['site','website'])
def site(message):
  webbrowser.open('https://vk.com')


@bot.message_handler(commands=["start"])
def main(message):
  bot.send_message(message.chat.id, "you press start")
  
@bot.message_handler()
def info(message):
  if message.text.lower()=='привет':
    bot.send_message(message.chat.id, f'простой текст Hi, {message.from_user.first_name} {message.from_user.last_name}')
  elif message.text.lower() == 'id':
    bot.reply_to(message,f'ID: {message.from_user.id}')



  
bot.polling(none_stop=True)