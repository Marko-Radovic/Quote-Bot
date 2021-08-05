from dotenv import load_dotenv
import os
from selenium import webdriver
import time as t
from quotes import author,quote

load_dotenv()

BOT_EMAIL = os.environ.get("INSPIRATIONAL_BOT_EMAIL")
BOT_PASSWORD = os.environ.get("INSPIRATIONAL_BOT_PASSWORD")
CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)


class Login:
    def __init__(self):

        driver.get("https://twitter.com/")
        t.sleep(1)
        driver.maximize_window()
        t.sleep(1)

        log_in = driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[3]/div[3]/span/span')
        log_in.click()
        t.sleep(1)
        log_in_with_email = driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[3]/a/div/span/span')
        log_in_with_email.click()
        t.sleep(1)
        username_input = driver.find_element_by_name("session[username_or_email]")
        username_input.send_keys(BOT_EMAIL)
        t.sleep(0.7)
        password_input = driver.find_element_by_name("session[password]")
        password_input.send_keys(BOT_PASSWORD)
        t.sleep(0.5)
        login_button = driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div/span/span')
        login_button.click()
        t.sleep(2)
        message = driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
        message.send_keys(f"@PENTA_LOL1 {quote} - {author}")

