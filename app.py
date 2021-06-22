# This is a sample Python script.

from aiogram import Bot, executor, Dispatcher, types

from config import bot_token
from logic import get_weather
from config import bot_token, weather_token


bot = Bot(bot_token)
dp = Dispatcher(bot)


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет!\n Я показываю тебе текущую погоду и прогноз.")


@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")

@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)
    jsn = get_weather(weather_token)
    await message.answer(
        text=(
            f"Сегодня: {jsn['current']['date']}\n"
            f"Температура воздуха: {jsn['current']['Температура воздуха']}\n"
            f"Ощущается: {jsn['current']['temp_feel']}\n"
            f"{jsn['current']['description']}\n"
        )
    )


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)