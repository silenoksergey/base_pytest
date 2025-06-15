from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.search_page import SearchPage


class HomePage(BasePage):
    PAGE_URL = 'https://store.steampowered.com/'
    SEARCH_FIELD = (By.ID, 'store_nav_search_term')

    def search_game(self, game_name):

        search = WebDriverWait(self.driver, self.WAIT_TIMEOUT).until(
            EC.presence_of_element_located(self.SEARCH_FIELD))
        search.send_keys(game_name + Keys.RETURN)
        return SearchPage(self.driver)
