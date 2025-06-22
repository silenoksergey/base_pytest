import pytest
from driver_singleton import DriverSingleton


@pytest.fixture(scope="function")
def driver(request, language):
    lang_map = {"russian": "ru-RU", "english": "en-US"}
    singleton = DriverSingleton(language=lang_map[language])
    yield singleton.get_driver()
    singleton.quit()

