from web import init, get_last_n_tweets


def main():
    init()
    tweets = get_last_n_tweets()


if __name__ == '__main__':
    main()
