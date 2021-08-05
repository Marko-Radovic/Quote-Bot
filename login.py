from dotenv import load_dotenv
import os
from selenium import webdriver
import time as t
from quotes import author,quote

load_dotenv()

BOT_EMAIL = os.environ.get("INSPIRATIONAL_BOT_EMAIL")
BOT_PASSWORD = os.environ.get("INSPIRATIONAL_BOT_PASSWORD")




class Login:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)
    def login(self):
        self.driver.get("https://twitter.com/")
        t.sleep(1)
        self.driver.maximize_window()
        t.sleep(1)

        log_in = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[3]/div[3]/span/span')
        log_in.click()
        t.sleep(1)
        log_in_with_email = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[3]/a/div/span/span')
        log_in_with_email.click()
        t.sleep(1)
        username_input = self.driver.find_element_by_name("session[username_or_email]")
        username_input.send_keys(BOT_EMAIL)
        t.sleep(0.7)
        password_input = self.driver.find_element_by_name("session[password]")
        password_input.send_keys(BOT_PASSWORD)
        t.sleep(0.5)
        login_button = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div/span/span')
        login_button.click()
        t.sleep(2)

    def get_message(self):
        message = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
        message.send_keys(f"@PENTA_LOL1 {quote} - {author}")

