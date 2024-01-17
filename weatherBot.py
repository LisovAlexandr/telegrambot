import telebot
import requests
import json

#https://openweathermap.org/current#name
bot = telebot.TeleBot('2120676466:AAGVrRy_TsAnFJDE1AlYktDlXCCiAmtVLks')
API = 'b9882b177436c8de9d84710b9d2d3bd1'

@bot.message_handler(commands='start')
def start(message):
    bot.send_message(message.chat.id,'Привет Зема')

@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    #bot.send_message(message.chat.id, f'Выбран город {city}')
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    #Способ 1
    #bot.reply_to(message, f'Сейчас погода: {res.json()}')
    #Способ 2
    if res.status_code == 200:
        data = json.loads(res.text)
        temp = data["main"]["temp"]
        bot.reply_to(message, f'Сейчас погода: {temp}')

        image = 'sunny.png' if temp < 5.0 else 'overcast.png'
        file = open('./' + image, 'rb')
        bot.send_photo(message.chat.id, file)
    else:
        bot.reply_to(message, 'Город указан неверно')


bot.polling(none_stop=True)