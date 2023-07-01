#импорт нужных мудулей
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token="") #введите токин из BotFather
dp = Dispatcher(bot)

#обработчик команды /start
@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nНапиши мне что-нибудь!")

#обработчик всех сообщений (кроме /start)
@dp.message_handler()
async def echo_message(message: types.Message):
    #message - объект
    #msg.from_user.id - id пользователя от которого получили сообщение
    #message.text - содержимое сообщения от пользователя
  
    #ответить пользователю
    await message.answer(message.from_user.id, message.text)
