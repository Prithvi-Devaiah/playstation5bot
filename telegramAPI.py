import requests as requests
import random
import credentials

url = credentials.telegramURL

start_command = '/start'
end_command = '/stop'
reset_amazonURL_command = '/resetAmazonURL'
test_command = '/runTest'
add_new_refresher = '/addNewRefresher'
pause_refresher = '/pause'
resume_refresher = '/resume'

valid_commands = ['/start', '/stop', '/resetAmazonURL:']  # list of valid commands that the bot recognises


# create func that get chat id
def get_chat_id(update):
    chat_id = update['message']["chat"]["id"]
    return chat_id


# create function that get message text
def get_message_text(update):
    message_text = update["message"]["text"]
    return message_text


# get user name of the bot
def get_user_name():
    update = last_update(url)
    user_name = update["message"]["from"]["first_name"]
    return user_name


# create function that get last_update
def last_update(req):
    response = requests.get(req + "getUpdates")
    response = response.json()
    result = response["result"]
    total_updates = len(result) - 1
    return result[total_updates]  # get last record message update


# create function that let bot send message to user
def send_message(message_text):
    chat_id = get_chat_id(last_update(url))
    params = {"chat_id": chat_id, "text": message_text}
    response = requests.post(url + "sendMessage", data=params)
    return response


def is_valid_text(update):
    message = get_message_text(update)
    if message not in valid_commands:
        return False
    return True


def get_last_message():
    return get_message_text(last_update(url))


def get_last_message_id():
    return last_update(url)["update_id"]


'''
def main():
    while True:
        while get_message_text(last_update(url)) == start_command:
            update_id = last_update(url)["update_id"]
            update = last_update(url)
            # end the script when the user types /stop
            if get_message_text(update) == "/stop":
                break
            if update_id == update["update_id"]:
                send_message("Testing Telegram Bot")
                update_id += 1
#main()
'''

