from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config_reader import ConfigReader


class BasePage:
    WAIT_TIMEOUT = ConfigReader().config["wait_timeout"]

    def __init__(self):
        from driver_singleton import DriverSingleton
        self.driver = DriverSingleton.get_driver()

    def wait_for_open(self):
        WebDriverWait(self.driver, self.WAIT_TIMEOUT).until(EC.presence_of_element_located(self.UNIQUE_ELEMENT))
