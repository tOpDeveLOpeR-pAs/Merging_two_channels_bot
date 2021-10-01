import time
import json

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
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
    driver.wait = WebDriverWait(driver, 5)
    return driver


def send_invitation(driver, tag: str, first_name: str):
    # находим поле для поиска пользователя
    search = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "telegram-search-input"))
    )
    search.clear()
    search.send_keys(tag)

    time.sleep(3)

    # находим кнопку для перехода в чат с данным пользователем
    """Ошибка: такая кнопка не находится, либо скрыта, либо просто не всегда"""
    
    button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "ListItem-button"))
    )


def lookup(driver, query):
    # стартовая страничка
    driver.get("https://web.telegram.org/z/")

    # проходимся по списку пользователей и отправляем каждому приглашение
    with open("data/invite_users.json", mode="r", encoding="utf-8") as file:
        invite_users = json.load(file)

    for tag, first_name in invite_users.items():
        time.sleep(3)
        send_invitation(driver, tag, first_name)


def send_main():
    driver = init_driver()
    lookup(driver, "Selenium")
    time.sleep(5)
    driver.quit()
