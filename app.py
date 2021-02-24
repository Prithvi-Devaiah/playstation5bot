import telegramAPI as Tele
import chromeDriver
import time
import os

update = True
url = "https:/www.youtube.com"

while True:
    command = Tele.get_last_message()

    if update:
        chromeDriver.change_webpage(url)
        update = False

    if not command == Tele.end_command:

        # check to see if amazonURL needs to be changed
        if command.find(Tele.reset_amazonURL_command) >= 0:
            tele_command, new_amazon_url = command.split(' ')
            url = new_amazon_url

        if command == Tele.test_command:
            result = str(chromeDriver.check_webpage("logo-icon"))
            print(result)
