from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.search_page import SearchPage


class HomePage(BasePage):
    PAGE_URL = 'https://store.steampowered.com/'
    SEARCH_FIELD = (By.ID, 'store_nav_search_term')
    LANGUAGE_DROPDOWN = (By.ID, 'language_pulldown')

    def search_game(self, game_name):

        search = WebDriverWait(self.driver, self.WAIT_TIMEOUT).until(
            EC.visibility_of_element_located(self.SEARCH_FIELD))
        search.send_keys(game_name + Keys.RETURN)


    def verify_language(self, language):
        """Проверяет, что язык применён, через текст выпадающего списка."""
        dropdown = WebDriverWait(self.driver, self.WAIT_TIMEOUT).until(
            EC.presence_of_element_located(self.LANGUAGE_DROPDOWN)
        )
        displayed = dropdown.text.lower()
        expected = {
            "russian": ["язык"],
            "english": ["language"]
        }
        assert any(lang in displayed for lang in expected[language]), \
            f"Ожидался язык {language}, получен {displayed}"