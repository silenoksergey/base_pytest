import pytest
from driver_singleton import DriverSingleton


@pytest.fixture(scope="session")
def driver():
    driver = DriverSingleton()
    yield driver.get_driver()
    driver.quit()

