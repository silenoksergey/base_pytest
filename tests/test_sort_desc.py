import pytest
from config_reader import ConfigReader
from pages.home_page import HomePage
from pages.search_page import SearchPage
from utils.price_utils import PriceUtils



@pytest.mark.parametrize("game_name, count", [
    ("The Witcher", 10),
    ("Fallout", 20)
])
class TestSortDesc:
    def test_search_page(self, driver, open_home_page, game_name, count, language):
        home_page = HomePage()
        search_page = SearchPage()
        home_page.wait_for_open()
        home_page.search_game(game_name)
        search_page.sort_by_price_desc()
        search_page.wait_for_open()
        prices = search_page.get_games_prices(count)
        numeric_prices = PriceUtils.parse_prices(prices)
        assert all(numeric_prices[i] >= numeric_prices[i + 1] for i in range(len(numeric_prices) - 1)), \
            f"Цены не отсортированы по убыванию: {numeric_prices}"
