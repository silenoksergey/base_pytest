import pytest
from pages.home_page import HomePage
from pages.search_page import SearchPage


@pytest.mark.parametrize("game_name, count", [
    ("The Witcher", 10),
    ("Fallout", 20)
])
def test_open_main_page(driver, game_name, count):
    home_page = HomePage(driver).open()
    assert driver.current_url == HomePage.HOME_PAGE_URL, "Домашняя страница не открыта"
    search_page = home_page.search_game(game_name)
    search_page.sort_by_price_desc()
    assert SearchPage.SEARCH_PAGE_URL in driver.current_url, "Страница поиска не открыта"
    search_page.checking_sort_price_desc(count)
    assert search_page.checking_sort_price_desc(count), "Игры не отсортированы по убыванию цены"
