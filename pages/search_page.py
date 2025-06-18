import re
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage


class SearchPage(BasePage):
    PAGE_URL = "https://store.steampowered.com/search/"
    SORT_DROPDOWN = (By.ID, "sort_by_trigger")
    SORT_DROPDOWN_DESC = (By.ID, "Price_DESC")
    GAME_PRICES = (By.XPATH, "//*[contains(@class, 'discount_final_price')]")
    WAIT_TIMEOUT = 10
    PRICE_PATTERN = (r'(\d{1,3}(?:[,.]\d{3})*(?:[,.]\d{1,2})?(?:\s*'
                     r'(?:руб|[a-zA-Z]{1,5}|[$€£¥₽]))|\b(?:Бесплатно|Free|Gratis)\b)')

    def sort_by_price_desc(self):
        dropdown = (WebDriverWait(self.driver, self.WAIT_TIMEOUT).until(
            EC.element_to_be_clickable(self.SORT_DROPDOWN)))
        dropdown.click()
        old_prices = [elem.text for elem in WebDriverWait(self.driver, self.WAIT_TIMEOUT).until(
            EC.presence_of_all_elements_located(self.GAME_PRICES))]
        sorted_by_desc = (WebDriverWait(self.driver, self.WAIT_TIMEOUT).until(
            EC.element_to_be_clickable(self.SORT_DROPDOWN_DESC)))
        sorted_by_desc.click()

        def prices_updated(driver):
            new_prices = [elem.text for elem in WebDriverWait(driver, self.WAIT_TIMEOUT).until(
                EC.visibility_of_all_elements_located(self.GAME_PRICES))]
            return new_prices != old_prices

        WebDriverWait(self.driver, self.WAIT_TIMEOUT).until(prices_updated)
        return self

    def get_games_prices(self, count):
        games = (WebDriverWait(self.driver, self.WAIT_TIMEOUT).until(
            EC.presence_of_all_elements_located(self.GAME_PRICES)))[:count]
        return [price.text for price in games]

    def checking_sort_price_desc(self, count):
        prices = self.get_games_prices(count)
        extracted_prices = []
        for price in prices:
            found_prices = re.findall(self.PRICE_PATTERN, price)
            extracted_prices.append(found_prices[-1] if found_prices else None)

        def convert_price_to_float(price):
            if price in ("Бесплатно", "Free", "Gratis", None):
                return 0.0
            numeric_part = re.match(r'\d{1,3}(?:[,.]\d{3})*(?:[,.]\d{1,2})?', price)
            if numeric_part:
                num_str = numeric_part.group().replace(',', '.')
                dot_count = num_str.count('.')
                if dot_count > 1:
                    parts = num_str.rsplit('.', 1)
                    num_str = parts[0].replace('.', '') + '.' + parts[1]
                return float(num_str)
            return 0.0

        numeric_prices = [convert_price_to_float(price) for price in extracted_prices]

        if len(numeric_prices) <= 1:
            return True

        for i in range(len(numeric_prices) - 1):
            if numeric_prices[i] < numeric_prices[i + 1]:
                return False

        return True
