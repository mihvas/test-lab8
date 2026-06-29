import allure

from pages.home_page import HomePage


@allure.feature("Navigation")
class TestNavigation:

    @allure.story("TC-09 Logo navigation")
    def test_logo_navigation(self, driver):
        home = HomePage(driver)

        with allure.step("Open Home Page"):
            home.open_page()

        with allure.step("Search product"):
            search = home.search("Nutella")

        with allure.step("Open first product"):
            product = search.open_first_product()

        with allure.step("Click logo"):
            product.click_logo()

        with allure.step("Verify Home Page"):
            assert home.is_open()

    @allure.story("TC-10 Barcode search")
    def test_search_barcode(self, driver):
        home = HomePage(driver)

        with allure.step("Open Home Page"):
            home.open_page()

        with allure.step("Search barcode"):
            search = home.search("3017620422003")

        with allure.step("Open product"):
            product = search.open_first_product()

        with allure.step("Verify Nutella"):
            assert product.title_contains("Nutella")
