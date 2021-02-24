import telegramAPI as Tele
import chromeDriver
import time
import os


while True:
    command = Tele.get_last_message()
    if not command == Tele.end_command:

        # check to see if amazonURL needs to be changed
        if command.find(Tele.reset_amazonURL_command) >= 0:
            tele_command, new_amazon_url = command.split(' ')

        if command == Tele.test_command:
            result = str(chromeDriver.check_webpage("https:/www.youtube.com", "logo-icon"))
            print(result)
