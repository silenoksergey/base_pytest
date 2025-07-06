import pytest
from driver_singleton import DriverSingleton
from config_reader import ConfigReader
from pages.home_page import HomePage
from enum_language import Language


@pytest.fixture(params=[Language.RUSSIAN, Language.ENGLISH])
def language(request):
    return request.param


@pytest.fixture(scope="function")
def driver(language):
    DriverSingleton.get_driver(language=language)
    yield DriverSingleton.get_driver()
    DriverSingleton.quit()


@pytest.fixture(scope="function")
def open_home_page(driver):
    config = ConfigReader()
    home_page = HomePage()
    driver.get(config.config["home_page_url"])
    home_page.wait_for_open()
