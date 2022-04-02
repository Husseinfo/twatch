from telepot import Bot

from conf import get_telegram_bot_token, get_telegram_user_id

bot = Bot(get_telegram_bot_token())


def send_message(text):
    bot.sendMessage(get_telegram_user_id(), text)
