from config_reader import ConfigReader


class DriverSingleton:
    _driver = None

    @staticmethod
    def get_driver(language="en-US"):
        if DriverSingleton._driver is None:
            from selenium import webdriver
            from selenium.webdriver.chrome.options import Options
            chrome_options = Options()
            config = ConfigReader()

            if config["browser"]["headless"]:
                chrome_options.add_argument("--headless")

            chrome_options.add_argument(f"--lang={language}")
            DriverSingleton._driver = webdriver.Chrome(options=chrome_options)
            if config["browser"]["maximize"]:
                DriverSingleton._driver.maximize_window()

        return DriverSingleton._driver

    @staticmethod
    def quit():
        if DriverSingleton._driver:
            DriverSingleton._driver.quit()
            DriverSingleton._driver = None
