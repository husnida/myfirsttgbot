import logging

from aiogram import Bot, Dispatcher, executor, types
API_TOKEN = '6008994775:AAFeJK5NbKgdqlkRSiV3-60iZQItmLgLt5I'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply(f"Salom!  {message.from_user.first_name} \nBizning Botga hush kelibsiz!")
    
@dp.message_handler(content_types=['text'])
async def malumot_ber(message: types.Message):
    if message.text == "Assalomu alaykum":
        await message.reply("Va alaykum assalom!\nBizning botga hush kelibsiz!")
    else:
        await message.reply("Sizga qanday yordam bera olamiz?")
        
@dp.message_handler()
async def Chet_tillari(message: types.Message):
    if message.text == "Men chet tillarini o'rganmoqchiman.":
        await message.reply("Sizni tushundim.\nBizda Ingliz, Kareys tillarini o'rganish imkoniyatingiz mavjud!")
    else:
        await message.reply("Siz so'ragan savolga javob qoldiramiz.\nltimos aloqada bo'ling! ")

    # old style:``
    # await bot.send_message(message.chat.id, message.text)

    await message.answer(message.text)
    
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
    #o'quv markazi uchun ro'yxatga oluvchi bot
# ism familya so'raladi
# telefon raqam so'raladi
# qaysi kursga qatnashmoqchi ekanligi so'raladi
# qaysi vaqt u uchun qulay ekanligi so'raladi
    