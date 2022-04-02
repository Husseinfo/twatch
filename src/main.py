from conf import get_users
from web import get_last_n_tweets


def main():
    for user in get_users():
        tweets = get_last_n_tweets(user)


if __name__ == '__main__':
    main()
