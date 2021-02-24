# APIs for anything to do with selenium and its functions.

from selenium import webdriver

op = webdriver.ChromeOptions()
op.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
op.add_argument("--headless")
op.add_argument("--no-sandbox")
op.add_argument("--disable-dev-sh-usage")

driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=op)


def check_webpage(url, web_element_id):
    driver.get(url)
    return driver.find_elements_by_id(web_element_id).is_displayed()


def close_webpage():
    driver.close()

