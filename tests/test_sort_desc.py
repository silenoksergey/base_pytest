import pytest
from config_reader import ConfigReader
from pages.home_page import HomePage
from pages.search_page import SearchPage
from utils.price_utils import PriceUtils
from pages.navigation import Navigation


@pytest.fixture(params=["russian", "english"])
def language(request):
    return request.param


@pytest.mark.parametrize("game_name, count", [
    ("The Witcher", 10),
    ("Fallout", 20)
])
class TestSortDesc:
    def test_search_page(self, driver, game_name, count, language):
        home_page = HomePage(driver)
        search_page = SearchPage(driver)
        price_utils = PriceUtils()
        config = ConfigReader()
        navigation = Navigation(driver, config)
        navigation.open_home_page()
        assert home_page.is_unique_element_visible(), "Домашняя страница не открыта"
        displayed_language = home_page.get_displayed_language()
        if language == "russian":
            assert displayed_language.lower() == "язык", f"Ожидалось значение 'Язык', получен {displayed_language}"
        if language == "english":
            assert displayed_language.lower() == "language", f"Ожидалось значение 'language', получен {displayed_language}"
        home_page.search_game(game_name)
        search_page.sort_by_price_desc()
        assert search_page.is_unique_element_visible(), "Страница поиска не открыта"
        prices = search_page.get_games_prices(count)
        numeric_prices = price_utils.parse_prices(prices)
        assert all(numeric_prices[i] >= numeric_prices[i + 1] for i in range(len(numeric_prices) - 1)), \
            f"Цены не отсортированы по убыванию: {numeric_prices}"
