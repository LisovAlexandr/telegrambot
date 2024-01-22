#import telebot
#Не устанавливается aiogram, требуется vs tools
from aiogram import Bot, Dispatcher, executor, types

#bot = telebot.TeleBot('2120676466:AAGVrRy_TsAnFJDE1AlYktDlXCCiAmtVLks')

bot = Bot('2120676466:AAGVrRy_TsAnFJDE1AlYktDlXCCiAmtVLks')
dp = Dispatcher(bot)

@dp.message_handler(content_types=['text'])#(commands=['start'])#если оставить с пустыми параметрами, то на любое сообщение будет ответ hello
async def start(message: types.Message):
    #await bot.send_message(message.chat.id, 'Hello') # старый способ
    #await message.answer('hello') #новый короткий способ
    await message.reply('heeelo')
    #file = open('/some.png','rb')
    #await message.answer_photo()

@dp.message_handler(commands=['inline'])#(commands=['start'])#если оставить с пустыми параметрами, то на любое сообщение будет ответ hello
async def info(message: types.Message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('button1', url='https://google.com/'))
    markup.add(types.InlineKeyboardButton('button2', callback_data='hi'))
    await message.reply('hihi',reply_markup=markup)

@dp.callback_query_handler()#что будет просиходить при нажатии на кнопку button2
async def callback(call):
    await call.message.answer(call.data)

@dp.message_handler(commands=['reply']) #кнопки под полем ввода, скрываются после нажатия
async def info(message: types.Message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add(types.KeyboardButton('site'))
    markup.add(types.KeyboardButton('website'))
    await message.answer('hello', reply_markup=markup)


executor.start_polling(dp)