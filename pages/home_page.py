from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.search_page import SearchPage


class HomePage(BasePage):
    URL = "https://world.openfoodfacts.org"

    SEARCH_INPUT = (
        By.CSS_SELECTOR,
        "input[name='search_terms']"
    )

    SEARCH_BUTTON = (
        By.CSS_SELECTOR,
        "form button[type='submit']"
    )

    LOGO = (
        By.XPATH,
        "//img[@id='logo']/parent::a"
    )

    def open_page(self):
        self.open(self.URL)

    def search(self, text):
        self.type(self.SEARCH_INPUT, text)

        self.click(self.SEARCH_BUTTON)

        return SearchPage(self.driver)

    def search_empty(self):
        self.click(self.SEARCH_BUTTON)

        return SearchPage(self.driver)

    def click_logo(self):
        self.click(self.LOGO)

    def is_open(self):
        return self.current_url().startswith(self.URL)
