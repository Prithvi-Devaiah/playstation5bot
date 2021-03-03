import chromeDriver
import selenium
import time


class PageRefresher:

    url = ""
    element_id = ""
    buy_now_button = ""
    xml_path = ""
    mode = ""
    pause = False
    has_buy_now_button = "false"

    def __init__(self, web_page, element_id, buy_now_button, use_id, has_buy_now_button):
        self.driver = chromeDriver.get_chrome_driver()
        self.url = web_page
        self.driver.get(web_page)
        self.buy_now_button = buy_now_button
        self.mode = use_id
        self.has_buy_now_button = has_buy_now_button
        if use_id == 'ID':
            self.element_id = element_id
        else:
            self.xml_path = element_id

    def refresh_page(self):
        self.driver.refresh()

    def reset_url(self, url):
        self.url = url
        self.driver.get(url)

    def check_webpage_element(self):
        if self.mode == 'ID':
            try:
                value = self.driver.find_element_by_id(self.element_id)
                return True
            except selenium.common.exceptions.NoSuchElementException:
                try:
                    self.driver.find_element_by_id(self.buy_now_button)
                    return False
                except selenium.common.exceptions.NoSuchElementException:
                    return True
        else:
            try:
                value = self.driver.find_element_by_xpath(self.xml_path)
                return True
            except selenium.common.exceptions.NoSuchElementException:
                if self.has_buy_now_button.find:
                    try:
                        self.driver.find_element_by_xpath(self.buy_now_button)
                        return True
                    except selenium.common.exceptions.NoSuchElementException:
                        return False
                else:
                    return False

    def test_url(self):
        if self.mode == 'ID':
            try:
                value = self.driver.find_element_by_id(self.element_id)
                return True
            except selenium.common.exceptions.NoSuchElementException:
                try:
                    self.driver.find_element_by_id(self.buy_now_button)
                    return False
                except selenium.common.exceptions.NoSuchElementException:
                    return True
        else:
            try:
                value = self.driver.find_element_by_xpath(self.xml_path)
                return True
            except selenium.common.exceptions.NoSuchElementException:
                if self.has_buy_now_button:
                    try:
                        self.driver.find_element_by_xpath(self.buy_now_button)
                        return True
                    except selenium.common.exceptions.NoSuchElementException:
                        return False
                else:
                    return False
