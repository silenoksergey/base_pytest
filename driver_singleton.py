from config_reader import ConfigReader


class DriverSingleton:
    _instance = None
    _driver = None

    @staticmethod
    def get_driver(language="en-US"):
        if DriverSingleton._instance is None:
            from selenium import webdriver
            from selenium.webdriver.chrome.options import Options
            chrome_options = Options()
            config = ConfigReader()

            if config.get_headless():
                chrome_options.add_argument("--headless")

            chrome_options.add_experimental_option("prefs", {
                "intl.accept_languages": language
            })
            DriverSingleton._driver = webdriver.Chrome(options=chrome_options)
            if config.get_maximize():
                DriverSingleton._driver.maximize_window()

            DriverSingleton._instance = True
        return DriverSingleton._driver

    @staticmethod
    def quit():
        if DriverSingleton._driver:
            DriverSingleton._driver.quit()
            DriverSingleton._instance = None
            DriverSingleton._driver = None
