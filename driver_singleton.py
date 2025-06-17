from selenium import webdriver

class DriverSingleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DriverSingleton, cls).__new__(cls)
            cls._instance.driver = webdriver.Chrome()
            cls._instance.driver.maximize_window()
        return cls._instance

    def get_driver(self):
        return self.driver

    def quit(self):
        if self.driver:
            self.driver.quit()
            self.__class__._instance = None