import allure

from pages.home_page import HomePage


@allure.feature("Product")
class TestProduct:

    @allure.story("TC-05 Open product page")
    def test_open_product(self, driver):

        home = HomePage(driver)

        with allure.step("Open Home Page"):
            home.open_page()

        with allure.step("Search Nutella"):
            search = home.search("Nutella")

        with allure.step("Open first product"):
            product = search.open_first_product()

        with allure.step("Verify title"):
            assert product.title_contains("Nutella")

    @allure.story("TC-06 Product image")
    def test_product_image(self, driver):

        home = HomePage(driver)

        home.open_page()

        search = home.search("Nutella")

        product = search.open_first_product()

        with allure.step("Verify image"):
            assert product.image_displayed()

    @allure.story("TC-07 NutriScore")
    def test_nutriscore(self, driver):

        home = HomePage(driver)

        home.open_page()

        search = home.search("Nutella")

        product = search.open_first_product()

        with allure.step("Verify NutriScore"):
            assert product.has_nutriscore()

    @allure.story("TC-08 Ingredients")
    def test_ingredients(self, driver):

        home = HomePage(driver)

        home.open_page()

        search = home.search("Nutella")

        product = search.open_first_product()

        with allure.step("Verify ingredients"):
            assert product.has_ingredients()