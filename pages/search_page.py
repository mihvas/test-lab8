from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.product_page import ProductPage


class SearchPage(BasePage):

    RESULTS = (
        By.CSS_SELECTOR,
        "a.list_product_a"
    )

    FIRST_PRODUCT = (
        By.CSS_SELECTOR,
        "a.list_product_a"
    )

    NO_RESULTS = (
        By.XPATH,
        "//*[contains(., 'No products')]"
    )


    def has_results(self):
        return len(self.elements(self.RESULTS)) > 0

    def open_first_product(self):
        first = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.FIRST_PRODUCT)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            first
        )

        first.click()

        return ProductPage(self.driver)

    def has_no_results(self):
        return self.is_visible(self.NO_RESULTS)

    def products_count(self):
        return len(self.elements(self.RESULTS))
