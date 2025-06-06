from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
import pytest

STORE_MAIN_PAGE = "https://store.steampowered.com/"
WAIT_TIMEOUT = 10
HOME_FEATURED_AND_RECOMMENDED = (By.ID, 'home_featured_and_recommended')
LOGIN_BUTTON = (By.XPATH, '//*[contains(@class, "global_action_link")]')
AUTH_FORM = (By.XPATH, '//*[@data-featuretarget="login"]')
USERNAME_FIELD = (By.XPATH, '//*[@data-featuretarget="login"]//*[contains(@type, "text")]')
PASSWORD_FIELD = (By.XPATH, '//*[@data-featuretarget="login"]//*[contains(@type, "password")]')
SUBMIT_BUTTON = (By.XPATH, '//*[@data-featuretarget="login"]//*[contains(@type, "submit")]')
AUTH_BUTTON_PRELOADER = (By.XPATH, '//*[@data-featuretarget="login"]//*[contains(@type, "submit")]//div//div')
AUTH_ERROR_TEXT = (By.XPATH, '//*[contains(@class, "tool-tip-source")]//following-sibling::div[2]')

fake = Faker()


def wait_visibility_element(driver, locator, timeout=WAIT_TIMEOUT):
    return WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator))


def wait_invisibility_element(driver, locator, timeout=WAIT_TIMEOUT):
    return WebDriverWait(driver, timeout).until_not(EC.visibility_of_element_located(locator))


def wait_clickable_element(driver, locator, timeout=WAIT_TIMEOUT):
    return WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(locator))


@pytest.mark.parametrize("username, password", [
    (fake.user_name(), fake.password()),
])
def test_open_main_page(driver, username, password):
    driver.get(STORE_MAIN_PAGE)

    assert wait_visibility_element(driver, locator=HOME_FEATURED_AND_RECOMMENDED), \
        "Не найден элемент рекомендаций на главной странице"

    login_button = wait_clickable_element(driver, locator=LOGIN_BUTTON)
    assert login_button is not None, "Не найдена кнопка 'Вход' на главной странице"
    login_button.click()

    assert wait_visibility_element(driver, locator=AUTH_FORM), "Не найдена форма авторизации"

    username_field = wait_visibility_element(driver, locator=USERNAME_FIELD)
    assert username_field is not None, "Не найдено поле ввода имени пользователя"
    username_field.send_keys(username)

    password_field = wait_visibility_element(driver, locator=PASSWORD_FIELD)
    assert password_field is not None, "Не найдено поле ввода пароля пользователя"
    password_field.send_keys(password)

    auth_button = wait_visibility_element(driver, locator=SUBMIT_BUTTON)
    assert auth_button is not None, "Не найдена кнопка 'Вход' в форме авторизации"
    auth_button.click()

    assert wait_visibility_element(driver, locator=AUTH_BUTTON_PRELOADER), \
        "Не найден прелоадер у кнопки 'Вход' в форме авторизации"

    assert wait_invisibility_element(driver, locator=AUTH_BUTTON_PRELOADER), \
        "Прелоадер кнопки 'Вход' в форме авторизации не исчез"

    assert wait_visibility_element(driver, locator=AUTH_ERROR_TEXT), \
        "Не найден текст ошибки при авторизации"
