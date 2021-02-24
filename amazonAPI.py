import chromeDriver
import time


class PageRefresher:

    url = ""

    def __init__(self, web_page):
        self.driver = chromeDriver.get_chrome_driver()
        self.url = web_page
        self.driver.get(web_page)

    def refresh_page(self):
        self.driver.refresh()

    def reset_url(self, url):
        self.url = url
        self.driver.get(url)

    def test_url(self, id):
        value = self.driver.find_element_by_id(id)
        if value is None:
            return False
        else:
            return True
