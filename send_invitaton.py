import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException


def init_driver():
    # пользовательский интерфейс
    options = Options()
    options.add_argument("user-data-dir=/home/sasha_pavlov/.config/google-chrome/Profile 1")

    driver = webdriver.Chrome(executable_path="/home/sasha_pavlov/drivers/chrome_selenium_driver/chromedriver",
                              chrome_options=options
                              )
    driver.wait = WebDriverWait(driver, 2)
    return driver


def lookup(driver, query):
    driver.get("https://web.telegram.org/z/")


def send_main():
    driver = init_driver()
    lookup(driver, "Selenium")
    time.sleep(15)
    driver.quit()
