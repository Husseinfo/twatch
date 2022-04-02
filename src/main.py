from conf import get_users
from telegram import send_message
from web import get_last_n_tweets


def main():
    for user in get_users():
        tweets = get_last_n_tweets(user, 1)
        send_message('\n\n\n'.join(tweets))


if __name__ == '__main__':
    main()
