# APIs for anything to do with selenium and its functions.

from selenium import webdriver
import os

using_heroku = True

op = webdriver.ChromeOptions()
op.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
op.add_argument("--headless")
op.add_argument("--no-sandbox")
op.add_argument("--disable-dev-shm-usage")
op.add_argument("--disable-gpu")


def get_chrome_driver():
    if using_heroku:
        return webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=op)
    else:
        return webdriver.Chrome(executable_path='C:\\Program Files (x86)\\chromedriver', keep_alive=True)


def change_webpage(driver, url):
    driver.get(url)


def check_webpage(driver, web_element_id):
    return driver.find_element_by_id(web_element_id).is_displayed()


def close_webpage(driver):
    driver.close()

