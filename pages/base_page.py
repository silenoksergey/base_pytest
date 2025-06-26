from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config_reader import ConfigReader
from selenium.webdriver.common.by import By


class BasePage:
    LANGUAGE_DROPDOWN = (By.ID, 'language_pulldown')

    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.config = ConfigReader()
        self.wait_timeout = self.config.get_wait_timeout()

    def is_unique_element_visible(self):
        return WebDriverWait(self.driver, self.wait_timeout).until(EC.presence_of_element_located(self.UNIQ_ELEMENT))

    def get_displayed_language(self):
        dropdown = WebDriverWait(self.driver, self.wait_timeout).until(
            EC.presence_of_element_located(self.LANGUAGE_DROPDOWN)
        )
        displayed = dropdown.text.lower()
        return displayed
