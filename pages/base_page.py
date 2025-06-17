from selenium.webdriver.chrome.webdriver import WebDriver


class BasePage:
    WAIT_TIMEOUT = 10

    def __init__(self, driver):
        self.driver: WebDriver = driver

    def open(self, language="english"):
        self.driver.delete_all_cookies()
        language_code = "russian" if language == "russian" else "english"
        self.driver.get(self.PAGE_URL)
        self.driver.add_cookie({
            'name': 'Steam_Language',
            'value': language_code,
            'domain': 'store.steampowered.com',
            'path': '/'
        })
        print(f"Установлена cookie Steam_Language={language_code}")

        self.driver.refresh()
        return self