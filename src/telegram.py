from time import ctime

from telepot import Bot as _Bot, glance
from telepot.loop import MessageLoop


class Bot:
    def __init__(self, name, token, allowed_users=()):
        self.name = name
        self._bot = _Bot(token)
        self.allowed_users = allowed_users
        MessageLoop(self._bot, self.handle).run_as_thread()

    def _log_message(self, user, message, unauthorized):
        with open(f'./{self.name}.log', 'a+') as f:
            f.write(f'{"UNAUTHORIZED|" if unauthorized else ""}{ctime()}|{user}|{message}\n')

    def handle(self, message):
        content_type, chat_type, chat_id = glance(message)
        unauthorized = chat_id not in self.allowed_users and self.allowed_users
        self._log_message(message['from'], message['text'], unauthorized)
        if unauthorized:
            self._bot.sendMessage(chat_id, text="Unauthorized")
            return
        if content_type != 'text':
            self._bot.sendMessage(chat_id, text=".-.")
            return
        self._bot.sendMessage(chat_id, text=self.get_response(chat_id, message['text']))

    def get_response(self, user, message):
        pass
