import time
import json

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def init_driver():
    # пользовательский интерфейс
    options = Options()
    options.add_argument("user-data-dir=/home/sasha_pavlov/.config/google-chrome/Profile 1")

    driver = webdriver.Chrome(executable_path="/home/sasha_pavlov/drivers/chrome_selenium_driver/chromedriver",
                              chrome_options=options
                              )
    driver.maximize_window()
    driver.wait = WebDriverWait(driver, 2)
    return driver


def send_invitation(driver, tag: str, first_name: str):
    search = driver.find_element_by_class_name("input-search")
    print("Element is visible? " + str(search.is_displayed()))
    #search.send_keys("hi")


def lookup(driver, query):
    # стартовая страничка
    driver.get("https://web.telegram.org/z/")

    # проходимся по списку пользователей и отправляем каждому приглашение
    with open("data/invite_users.json", mode="r", encoding="utf-8") as file:
        invite_users = json.load(file)

    for tag, first_name in invite_users.items():
        send_invitation(driver, tag, first_name)


def send_main():
    driver = init_driver()
    lookup(driver, "Selenium")
    time.sleep(5)
    driver.quit()
