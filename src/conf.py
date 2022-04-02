from os.path import dirname

from yaml import safe_load

conf_file_path = f'{dirname(__file__)}/../config.yml'

try:
    with open(conf_file_path) as _f:
        conf = safe_load(_f.read())
except FileNotFoundError:
    exit('Conf file config.yml does not exist in ../ dir')
except Exception as e:
    exit(f'Cannot parse config file config.yml:\n{e.args}')


def get_users():
    return conf['twitter']['users']


def get_delay():
    return conf['check_every']


def get_telegram_bot_token():
    return conf['telegram']['bot_token']


def get_telegram_user_id():
    return conf['telegram']['user_id']
