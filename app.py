from selenium import webdriver
import telegramAPI as Tele
import time
import os

op = webdriver.ChromeOptions()
op.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
op.add_argument("--headless")
op.add_argument("--no-sandbox")
op.add_argument("--disable-dev-sh-usage")

driver = webdriver.Chrome(executable_path = os.environ.get("CHROMEDRIVER_PATH"), chrome_options=op)

while True:
    if not Tele.get_last_message() == Tele.end_command:
        Tele.send_message(Tele.get_chat_id(last_update(Tele.url)), "Testing Telegram Bot")
        time.sleep(3)
