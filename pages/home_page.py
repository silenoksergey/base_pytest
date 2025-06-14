from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.search_page import SearchPage


class HomePage:
    SEARCH_FIELD = (By.ID, 'store_nav_search_term')
    WAIT_TIMEOUT = 10
    HOME_PAGE_URL = 'https://store.steampowered.com/'

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.HOME_PAGE_URL)
        return self

    def search_game(self, game_name):
        search = WebDriverWait(self.driver, self.WAIT_TIMEOUT).until(
            EC.presence_of_element_located(self.SEARCH_FIELD))
        search.send_keys(game_name + Keys.RETURN)
        return SearchPage(self.driver)
