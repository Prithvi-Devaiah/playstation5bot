from selenium import webdriver
import telegramAPI as Tele
import time
import os

op = webdriver.ChromeOptions()
op.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
op.add_argument("--headless")
op.add_argument("--no-sandbox")
op.add_argument("--disable-dev-sh-usage")

driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=op)

while True:
    command = Tele.get_last_message()
    if not command == Tele.end_command:
        # Tele.send_message("Testing Telegram Bot")
        time.sleep(3)
        if command.find('Hello') >= 0:
            Tele.send_message("Hello.")
            if Tele.get_user_name().find('Manav') >= 0 or Tele.get_user_name().find('manav') >= 0:
                Tele.send_message("Wassup bitch boi Manav. Shappa teriyakka open madde bot na?")
            elif Tele.get_user_name().find('Sankalp') >= 0 or Tele.get_user_name().find('sankalp') >= 0:
                Tele.send_message("Yeno lowde.. shaa teriyakka bot open madde?")
            elif Tele.get_user_name().find('Kabaab') >= 0:
                Tele.send_message("Alright alright alright!!")
        if command.find('Bye') >= 0:
            Tele.send_message("See ya later, alligator.")
