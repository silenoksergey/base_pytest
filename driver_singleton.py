from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class DriverSingleton:
    _instance = None


    def __new__(cls, language="en-US"):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            chrome_options = Options()
            chrome_options.add_experimental_option("prefs", {
                "intl.accept_languages": language
            })
            cls._instance.driver = webdriver.Chrome(options=chrome_options)
            cls._instance.driver.maximize_window()
        return cls._instance



    def get_driver(self):
        return self.driver

    def quit(self):
        if self.driver:
            self.driver.quit()
            self.__class__._instance = None