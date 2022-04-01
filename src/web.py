from os import environ
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait

driver: WebDriver
username: str = 'fifacom'


def init():
    global driver
    environ['PATH'] += f':{Path(__file__).parent.parent}/driver/'

    options = Options()
    options.add_argument(f"--user-data-dir={Path(__file__).parent.parent}/chrome/")
    options.add_argument('--profile-directory=Profile 1')
    driver = webdriver.Chrome(options=options)

    driver.get(f'https://twitter.com/{username}')


def get_last_n_tweets(n=10) -> list:
    global driver
    tweets = []
    first_tweet = 'section > div > div > div:nth-child(1)'

    try:
        WebDriverWait(driver, 30).until(lambda _driver: _driver.find_element_by_css_selector(first_tweet))
    except Exception as e:
        print(f'Error occurred: {e}')
    return tweets
