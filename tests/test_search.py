import allure

from pages.home_page import HomePage


@allure.feature("Search")
class TestSearch:

    @allure.story("TC-01 Search existing product")
    def test_search_existing_product(self, driver):

        home = HomePage(driver)

        with allure.step("Open OpenFoodFacts"):
            home.open_page()

        with allure.step("Search Nutella"):
            results = home.search("Nutella")

        with allure.step("Verify results exist"):
            assert results.has_results()

    @allure.story("TC-02 Search nonexistent product")
    def test_search_nonexistent_product(self, driver):

        home = HomePage(driver)

        with allure.step("Open Home Page"):
            home.open_page()

        with allure.step("Search fake product"):
            results = home.search("asdfghqwerty123456")

        with allure.step("Verify no results message"):
            assert results.has_no_results()

    @allure.story("TC-03 Empty search")
    def test_empty_search(self, driver):

        home = HomePage(driver)

        with allure.step("Open Home Page"):
            home.open_page()

        with allure.step("Click Search without text"):
            page = home.search_empty()

        with allure.step("Verify page opened"):
            assert page.current_url() != ""

    @allure.story("TC-04 Partial search")
    def test_partial_search(self, driver):

        home = HomePage(driver)

        with allure.step("Open Home Page"):
            home.open_page()

        with allure.step("Search Nut"):
            results = home.search("Nut")

        with allure.step("Verify results"):
            assert results.products_count() > 0