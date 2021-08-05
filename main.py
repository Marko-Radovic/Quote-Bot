from dotenv import load_dotenv
import os
from selenium import webdriver
from login import Login

import time as t
load_dotenv()

BOT_EMAIL = os.environ.get("INSPIRATIONAL_BOT_EMAIL")
BOT_PASSWORD = os.environ.get("INSPIRATIONAL_BOT_PASSWORD")
CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"

bot = Login(CHROME_DRIVER_PATH)
bot.login()
bot.get_message()


