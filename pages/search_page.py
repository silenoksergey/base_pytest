from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage


class SearchPage(BasePage):
    SORT_DROPDOWN = (By.ID, "sort_by_trigger")
    SORT_DROPDOWN_DESC = (By.ID, "Price_DESC")
    GAME_PRICES = (By.XPATH, "//*[contains(@class, 'discount_final_price')]")
    UNIQUE_ELEMENT = (By.XPATH, '//*[contains(@class, "sortbox")]')
    LOADER_SEARCH_CONTAINER = (By.XPATH, '//*[contains(@style, "opacity") and contains(@style, "0.5")]')

    def __init__(self):
        super().__init__()
        self.wait = WebDriverWait(self.driver, self.WAIT_TIMEOUT)
        self.wait_poll = WebDriverWait(self.driver, self.WAIT_TIMEOUT, poll_frequency=0.1)

    def sort_by_price_desc(self):
        dropdown = self.wait.until(
            EC.element_to_be_clickable(self.SORT_DROPDOWN))
        dropdown.click()
        sorted_by_desc = self.wait.until(
            EC.element_to_be_clickable(self.SORT_DROPDOWN_DESC))
        sorted_by_desc.click()

        self.wait_poll.until(
            EC.presence_of_element_located(self.LOADER_SEARCH_CONTAINER))
        self.wait_poll.until_not(
            EC.presence_of_element_located(self.LOADER_SEARCH_CONTAINER))
        new_prices = [elem.text for elem in self.wait.until(
            EC.visibility_of_all_elements_located(self.GAME_PRICES))]
        return new_prices

    def get_games_prices(self, count):
        games = self.wait.until(
            EC.presence_of_all_elements_located(self.GAME_PRICES))[:count]
        return [price.text for price in games]
