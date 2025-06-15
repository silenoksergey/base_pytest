from selenium.webdriver.chrome.webdriver import WebDriver


class BasePage:
    WAIT_TIMEOUT = 10

    def __init__(self, driver):
        self.driver: WebDriver = driver

    def open(self):
        self.driver.get(self.PAGE_URL)
        return self
