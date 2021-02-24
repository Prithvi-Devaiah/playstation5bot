import telegramAPI as Tele
import chromeDriver
import amazonAPI
import time
import os


refreshers = {}

last_update_id = 00000


def create_new_refresher(refresher_id_, page_url, element_id_to_use):
    new_refresher = amazonAPI.PageRefresher(page_url, element_id_to_use)
    if refresher_id_ in refreshers:
        return None
    refreshers[refresher_id_] = new_refresher
    return refreshers[refresher_id_]


while True:
    time.sleep(3)
    while last_update_id != Tele.get_last_message_id():

        last_update_id = Tele.get_last_message_id()

        command = Tele.get_last_message()

        if not command == Tele.end_command:

            # check to see if amazonURL needs to be changed
            if command.find(Tele.reset_amazonURL_command) >= 0:
                tele_command, new_amazon_url = command.split(' ')
                url = new_amazon_url

            if command == Tele.test_command:
                result = str(chromeDriver.check_webpage("logo-icon"))
                print(result)

            if command.find(Tele.add_new_refresher) >= 0:
                command_temp = command.split(' ')
                if len(command_temp) <= 0:
                    Tele.send_message('Add the name of the refresher in the command. Format of the command is '
                                      '/addNewRefresher [id_of_the_refresher] [url] [element_id]')
                elif len(command_temp) > 4:
                    Tele.send_message('Format of the command is '
                                      '/addNewRefresher [id_of_the_refresher] [url] [element_id]')
                else:
                    refresher_temp = create_new_refresher(command_temp[1], command_temp[2], command_temp[3])
                    if refresher_temp is None:
                        Tele.send_message('Could not create the refresher. Provide a valid URL or a unique id for the '
                                          'refresher')
                    else:
                        Tele.send_message('Successfully created a new refresher.')

            if command.find(Tele.test_command) >= 0:
                command_temp = command.split(' ')
                if len(command_temp) <= 0:
                    Tele.send_message('Add the id of the refresher in the command. Format of the command is '
                                      '/runTest [id_of_the_refresher] [id_of_a_webpage_element]')

                elif len(command_temp) > 3:
                    Tele.send_message('Format of the command is /runTest [id_of_the_refresher] ['
                                      'id_of_a_webpage_element]')

                else:
                    if command_temp[1] in refreshers:
                        current_refresher = refreshers[command_temp[1]]
                        if current_refresher.test_url(command_temp[2]):
                            Tele.send_message('Site working fine.')
                        else:
                            Tele.send_message('Could not find the element or the site isn\'t working properly.')
                    else:
                        Tele.send_message('Could not find a refresher by the provided ID. Try a valid ID.')
            if command.find(Tele.pause_refresher) >= 0:
                command_temp = command.split(' ')
                if len(command_temp) <= 0:
                    Tele.send_message('Add the name of the refresher in the command. Format of the command is '
                                      '/pause [id_of_the_refresher]')
                elif len(command_temp) > 2:
                    Tele.send_message('Format of the command is '
                                      '/pause [id_of_the_refresher]')
                else:
                    if command_temp[1] in refreshers:
                        current_refresher = refreshers[command_temp[1]]
                        current_refresher.pause = True
                        message = 'Paused the ' + command_temp[1] + '. Use /resume ' + command_temp[1] + 'to resume ' \
                                                                                                         'checking. '
                        Tele.send_message(message)
                    else:
                        Tele.send_message('Could not find the refresher by the provided ID. Try a valid ID.')

            if command.find(Tele.resume_refresher) >= 0:
                command_temp = command.split(' ')
                if len(command_temp) <= 0:
                    Tele.send_message('Add the name of the refresher in the command. Format of the command is '
                                      '/resume [id_of_the_refresher]')
                elif len(command_temp) > 2:
                    Tele.send_message('Format of the command is '
                                      '/resume [id_of_the_refresher]')
                else:
                    if command_temp[1] in refreshers:
                        current_refresher = refreshers[command_temp[1]]
                        current_refresher.pause = False
                        message = 'Resumed the ' + command_temp[1] + '. Use /pause ' + command_temp[1] + 'to pause ' \
                                                                                                         'checking. '
                        Tele.send_message(message)
                    else:
                        Tele.send_message('Could not find the refresher by the provided ID. Try a valid ID.')

    for refresher_id in refreshers:
        refresher_object = refreshers[refresher_id]
        if not refresher_object.pause:
            if not refresher_object.check_webpage_element():
                message = "Found an anomaly in " + refresher_id + " " + refresher_object.url + ". Check immediately. " \
                                                                                              "Enter /pause " + \
                          refresher_id + "to pause it. "
                Tele.send_message(message)
            refresher_object.refresh()

