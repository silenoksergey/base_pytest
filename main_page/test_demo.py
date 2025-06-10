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


@pytest.mark.parametrize("username, password", [
    (fake.user_name(), fake.password()),
])
def test_open_main_page(driver, username, password):
    driver.get(STORE_MAIN_PAGE)

    WebDriverWait(driver, WAIT_TIMEOUT).until(
        EC.visibility_of_element_located(HOME_FEATURED_AND_RECOMMENDED))

    login_button = WebDriverWait(driver, WAIT_TIMEOUT).until(
        EC.element_to_be_clickable(LOGIN_BUTTON))
    login_button.click()

    WebDriverWait(driver, WAIT_TIMEOUT).until(
        EC.visibility_of_element_located(AUTH_FORM))

    username_field = WebDriverWait(driver, WAIT_TIMEOUT).until(
        EC.visibility_of_element_located(USERNAME_FIELD))
    username_field.send_keys(username)

    password_field = WebDriverWait(driver, WAIT_TIMEOUT).until(
        EC.visibility_of_element_located(PASSWORD_FIELD))
    password_field.send_keys(password)

    auth_button = WebDriverWait(driver, WAIT_TIMEOUT).until(
        EC.visibility_of_element_located(SUBMIT_BUTTON))
    auth_button.click()

    WebDriverWait(driver, WAIT_TIMEOUT).until(
        EC.visibility_of_element_located(AUTH_BUTTON_PRELOADER))

    WebDriverWait(driver, WAIT_TIMEOUT).until_not(
        EC.visibility_of_element_located(AUTH_BUTTON_PRELOADER))

    WebDriverWait(driver, WAIT_TIMEOUT).until(
        EC.visibility_of_element_located(AUTH_ERROR_TEXT))

    assert True  # if we are here - test passed