import pytest
from driver_singleton import DriverSingleton
from config_reader import ConfigReader


@pytest.fixture(scope="function")
def driver(language):
    config = ConfigReader()
    lang_map = config.get_lang_map()
    DriverSingleton.get_driver(language=lang_map[language])
    yield DriverSingleton.get_driver()
    DriverSingleton.quit()
