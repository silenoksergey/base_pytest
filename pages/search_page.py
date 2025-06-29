from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage


class SearchPage(BasePage):
    SORT_DROPDOWN = (By.ID, "sort_by_trigger")
    SORT_DROPDOWN_DESC = (By.ID, "Price_DESC")
    GAME_PRICES = (By.XPATH, "//*[contains(@class, 'discount_final_price')]")
    PRICE_PATTERN = (r'(\d{1,3}(?:[,.]\d{3})*(?:[,.]\d{1,2})?(?:\s*'
                     r'(?:руб|[a-zA-Z]{1,5}|[$€£¥₽]))|\b(?:Бесплатно|Free|Gratis)\b)')
    UNIQUE_ELEMENT = (By.XPATH, '//*[contains(@class, "sortbox")]')
    LOADER_SEARCH_CONTAINER = (By.XPATH, '//*[contains(@style, "opacity") and contains(@style, "0.5")]')

    def sort_by_price_desc(self):
        dropdown = (WebDriverWait(self.driver, self.wait_timeout).until(
            EC.element_to_be_clickable(self.SORT_DROPDOWN)))
        dropdown.click()
        sorted_by_desc = WebDriverWait(self.driver, self.wait_timeout).until(
            EC.element_to_be_clickable(self.SORT_DROPDOWN_DESC))
        sorted_by_desc.click()

        WebDriverWait(self.driver, self.wait_timeout, poll_frequency=0.1).until(
            EC.presence_of_element_located(self.LOADER_SEARCH_CONTAINER))
        WebDriverWait(self.driver, self.wait_timeout, poll_frequency=0.1).until_not(
            EC.presence_of_element_located(self.LOADER_SEARCH_CONTAINER))
        new_prices = [elem.text for elem in WebDriverWait(self.driver, self.wait_timeout).until(
            EC.visibility_of_all_elements_located(self.GAME_PRICES))]
        return new_prices

    def get_games_prices(self, count):
        games = (WebDriverWait(self.driver, self.wait_timeout).until(
            EC.presence_of_all_elements_located(self.GAME_PRICES)))[:count]
        return [price.text for price in games]
