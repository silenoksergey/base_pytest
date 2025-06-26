import re
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage


class SearchPage(BasePage):
    SORT_DROPDOWN = (By.ID, "sort_by_trigger")
    SORT_DROPDOWN_DESC = (By.ID, "Price_DESC")
    GAME_PRICES = (By.XPATH, "//*[contains(@class, 'discount_final_price')]")
    UNIQ_ELEMENT = (By.XPATH, '//*[contains(@class, "sortbox")]')


    def sort_by_price_desc(self):
        dropdown = (WebDriverWait(self.driver, self.wait_timeout).until(
            EC.element_to_be_clickable(self.SORT_DROPDOWN)))
        dropdown.click()
        old_prices = [elem.text for elem in WebDriverWait(self.driver, self.wait_timeout).until(
            EC.presence_of_all_elements_located(self.GAME_PRICES))]
        sorted_by_desc = (WebDriverWait(self.driver, self.wait_timeout).until(
            EC.element_to_be_clickable(self.SORT_DROPDOWN_DESC)))
        sorted_by_desc.click()

        def prices_updated(driver):
            new_prices = [elem.text for elem in WebDriverWait(driver, self.wait_timeout).until(
                EC.visibility_of_all_elements_located(self.GAME_PRICES))]
            return new_prices != old_prices

        WebDriverWait(self.driver, self.wait_timeout).until(prices_updated)
        return self

    def get_games_prices(self, count):
        games = (WebDriverWait(self.driver, self.wait_timeout).until(
            EC.presence_of_all_elements_located(self.GAME_PRICES)))[:count]
        return [price.text for price in games]


