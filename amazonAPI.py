import chromeDriver
import selenium
import time


class PageRefresher:

    url = ""
    element_id = ""
    xml_path = ""
    mode = ""
    pause = False

    def __init__(self, web_page, element_id, use_id):
        self.driver = chromeDriver.get_chrome_driver()
        self.url = web_page
        self.driver.get(web_page)
        self.mode = use_id
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
                return False
        else:
            try:
                value = self.driver.find_element_by_xpath(self.xml_path)
                return True
            except selenium.common.exceptions.NoSuchElementException:
                return False

    def test_url(self):
        if self.mode == 'ID':
            value = self.driver.find_element_by_id(self.element_id)
        else:
            value = self.driver.find_element_by_xpath(self.xml_path)
        if value is None:
            return False
        else:
            return True
