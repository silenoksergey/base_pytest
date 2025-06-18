import pytest
from pages.home_page import HomePage
from pages.search_page import SearchPage

@pytest.mark.parametrize("language", ["russian", "english"])
@pytest.mark.parametrize("game_name, count", [
    ("The Witcher", 10),
    ("Fallout", 20)
])
class TestSortDesc:
    def test_search_page(self, driver, game_name, count, language):
        home_page = HomePage(driver)
        search_page = SearchPage(driver)
        home_page.open(language=language)
        assert driver.current_url == home_page.PAGE_URL, "Домашняя страница не открыта"
        home_page.verify_language(language)
        search_game = home_page.search_game(game_name)
        search_game.sort_by_price_desc()
        assert search_page.PAGE_URL in driver.current_url, "Страница поиска не открыта"
        search_game.checking_sort_price_desc(count)
        assert search_game.checking_sort_price_desc(count), "Игры не отсортированы по убыванию цены"
