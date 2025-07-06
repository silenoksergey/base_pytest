from config_reader import ConfigReader
from enum_language import Language
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class DriverSingleton:
    _driver = None

    @staticmethod
    def get_driver(language=Language.DEFAULT_LANGUAGE):
        if DriverSingleton._driver is None:
            chrome_options = Options()
            config = ConfigReader()
            option_list = config.config["browser"]
            for opt in option_list:
                chrome_options.add_argument(opt)
            chrome_options.add_argument(f"--lang={language}")
            DriverSingleton._driver = webdriver.Chrome(options=chrome_options)

        return DriverSingleton._driver

    @staticmethod
    def quit():
        if DriverSingleton._driver:
            DriverSingleton._driver.quit()
            DriverSingleton._driver = None
