from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ProductPage(BasePage):
    PRODUCT_TITLE = (
        By.CSS_SELECTOR,
        "h1"
    )

    PRODUCT_IMAGE = (
        By.CSS_SELECTOR,
        "#og_image img"
    )

    NUTRISCORE = (
        By.XPATH,
        "//img[contains(@src,'nutriscore')]"
    )

    INGREDIENTS = (
        By.ID,
        "ingredients"
    )

    LOGO = (
        By.CSS_SELECTOR,
        "a[href='/'] img"
    )

    def title_contains(self, text):
        return text.lower() in self.find(self.PRODUCT_TITLE).text.lower()

    def image_displayed(self):
        return self.find(self.PRODUCT_IMAGE).is_displayed()

    def has_nutriscore(self):
        return self.is_visible(self.NUTRISCORE)

    def has_ingredients(self):
        self.scroll_to(self.INGREDIENTS)

        return self.find(self.INGREDIENTS).is_displayed()

    def click_logo(self):
        self.click(self.LOGO)
