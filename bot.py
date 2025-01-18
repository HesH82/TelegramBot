
import logging
from aiogram import Bot, Dispatcher, executor, types
import openai

# Токен Telegram-бота
TELEGRAM_TOKEN = "вставь_свой_токен"
# Токен OpenAI GPT
OPENAI_API_KEY = "вставь_свой_GPT_токен"

# Настройка OpenAI
openai.api_key = OPENAI_API_KEY

# Логирование
logging.basicConfig(level=logging.INFO)

# Инициализация бота
bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)

# Обработка текстовых сообщений
@dp.message_handler()
async def handle_message(message: types.Message):
    user_message = message.text  # Сообщение от пользователя

    try:
        # Отправка текста в GPT
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_message}]
        )
        bot_reply = response['choices'][0]['message']['content']

        # Отправка ответа обратно пользователю
        await message.answer(bot_reply)
    except Exception as e:
        await message.answer("Произошла ошибка: " + str(e))

# Запуск бота
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
