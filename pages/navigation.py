class Navigation:

    def __init__(self, driver, config):
        self.driver = driver
        self.home_page_url = config.get_home_page_url()

    def open_home_page(self):
        self.driver.get(self.home_page_url)
