import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from faker import Faker


@pytest.fixture(scope="session")
def driver():
    browser = webdriver.Chrome()
    browser.maximize_window()
    yield browser

@pytest.fixture()
def fake_auth_data():
    fake = Faker()
    return {
        "username": fake.user_name(),
        "password": fake.password()
    }


def test_open_main_page(driver):
    driver.get("https://store.steampowered.com/")
    popular_bar = driver.find_element(By.ID, 'home_featured_and_recommended')
    popular_bar.is_enabled()


def test_open_login_page(driver):
    burger_menu = driver.find_element(By.XPATH, '//*[@class="global_action_link"]')
    burger_menu.is_enabled()
    burger_menu.click()
    time.sleep(2)
    login_label = driver.find_element(By.XPATH, '//*[contains(@class, "ZrHHmwLEugLjLI")]')
    login_label.is_displayed()

def test_input_login_data(driver, fake_auth_data):
    username_field = driver.find_element(By.XPATH, '(//*[contains(@class, "_2GBWeup5cttgbTw8FM3tfx")])[1]')
    password_field = driver.find_element(By.XPATH,'(//*[contains(@class, "_2GBWeup5cttgbTw8FM3tfx")])[2]')
    username_field.is_enabled()
    password_field.is_enabled()
    username_field.send_keys(fake_auth_data["username"])
    password_field.send_keys(fake_auth_data["password"])

def test_click_login_button(driver):
    login_button = driver.find_element(By.XPATH, '//*[contains(@class, "DjSvCZoKKfoNSmarsEcTS")]')
    login_button.click()
