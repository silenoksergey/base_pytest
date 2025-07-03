from enum import StrEnum

import pytest
from driver_singleton import DriverSingleton
from config_reader import ConfigReader


class Language(StrEnum):
    RUSSIAN = "russian"
    ENGLISH = "english"


@pytest.fixture(params=[Language.RUSSIAN, Language.ENGLISH])
def language(request):
    return request.param


@pytest.fixture(scope="function")
def driver(language):
    config = ConfigReader()
    lang_map = config["lang_map"]
    DriverSingleton.get_driver(language=lang_map[language])
    yield DriverSingleton.get_driver()
    DriverSingleton.quit()

@pytest.fixture(scope="function")
def open_home_page(driver):
    config = ConfigReader()
    driver.get(config["home_page_url"])