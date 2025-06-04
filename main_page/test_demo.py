from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
import pytest
from faker import Faker
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="session")
def driver():
    browser = webdriver.Chrome()
    browser.maximize_window()
    yield browser


@pytest.fixture
def fake_auth_data():
    fake = Faker()
    return {
        "username": fake.user_name(),
        "password": fake.password()
    }


def test_open_main_page(driver):
    driver.get("https://store.steampowered.com/")
    try:
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'home_featured_and_recommended')))
    except TimeoutException:
        pytest.fail("Элемент 'Популярное и рекомендуемое' не найден на главной странице")


def test_open_login_page(driver):
    try:
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@class="global_action_link"]')))
        login_button.click()
    except TimeoutException:
        pytest.fail("Кнопка 'войти' не найдена на главной странице")
    try:
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[contains(@class, "ZrHHmwLEugLjLI")]')))
    except TimeoutException:
        pytest.fail("Лейбл 'Вход' не найден на странице авторизации")


def test_input_login_data(driver, fake_auth_data):
    try:
        username_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '(//*[contains(@class, "FM3tfx")])[1]')))
        username_field.send_keys(fake_auth_data["username"])
    except TimeoutException:
        pytest.fail("Не найдено поле ввода имени пользователя")
    try:
        password_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '(//*[contains(@class, "FM3tfx")])[2]')))
        password_field.send_keys(fake_auth_data["password"])
    except TimeoutException:
        pytest.fail("Не найдено поле ввода пароля")


def test_show_preload_login_button(driver):
    try:
        auth_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[contains(@class, "DjSvCZo")]')))
        auth_button.click()
    except TimeoutException:
        pytest.fail("Не найдена кнопка 'Войти'")
    try:
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[contains(@class,"WYrJyNEV")]')))
    except TimeoutException:
        pytest.fail("Не найден прелоадер у кнопки 'Войти'")
    try:
        WebDriverWait(driver, 10).until(
            EC.invisibility_of_element_located((By.XPATH, '//*[contains(@class,"WYrJyNEV")]')))
    except TimeoutException:
        pytest.fail("Не исчез прелоадер у кнопки 'Войти'")


def test_show_auth_text_error(driver):
    try:
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[contains(@class, "N_0fGZ")]')))
    except TimeoutException:
        pytest.fail("Не найден текст ошибки под кнопкой 'Войти'")

