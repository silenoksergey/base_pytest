from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class HomePage(BasePage):
    SEARCH_FIELD = (By.ID, 'store_nav_search_term')
    UNIQUE_ELEMENT = (By.ID, 'home_video_desktop')

    def search_game(self, game_name):
        search = WebDriverWait(self.driver, self.WAIT_TIMEOUT).until(
            EC.visibility_of_element_located(self.SEARCH_FIELD))
        search.send_keys(game_name + Keys.RETURN)
