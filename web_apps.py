#import telebot
#Не устанавливается aiogram, требуется vs tools
from aiogram import Bot, Dispatcher, executor, types


#bot = telebot.TeleBot('2120676466:AAGVrRy_TsAnFJDE1AlYktDlXCCiAmtVLks')

bot = Bot('2120676466:AAGVrRy_TsAnFJDE1AlYktDlXCCiAmtVLks')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.ass(types.KeyboardButton('Открыть вебстраницу', web_app=WebAppInfo))

########### в разработке.............