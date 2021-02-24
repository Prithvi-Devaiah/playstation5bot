import chromeDriver
import time


class PageRefresher:

    url = ""
    element_id = ""
    xml_path = ""
    use_id = True
    pause = False

    def __init__(self, web_page, element_id, use_id):
        self.driver = chromeDriver.get_chrome_driver()
        self.url = web_page
        self.driver.get(web_page)
        if use_id:
            self.element_id = element_id
        else:
            self.xml_path = element_id

    def refresh_page(self):
        self.driver.refresh()

    def reset_url(self, url):
        self.url = url
        self.driver.get(url)

    def check_webpage_element(self):
        if self.use_id:
            value = self.driver.find_element_by_id(self.element_id)
        else:
            value = self.driver.find_element_by_xpath(self.xml_path)
        if value is None:
            return False
        else:
            return True

    def test_url(self, id):
        if self.use_id:
            value = self.driver.find_element_by_id(self.element_id)
        else:
            value = self.driver.find_element_by_xpath(self.xml_path)
        if value is None:
            return False
        else:
            return True
