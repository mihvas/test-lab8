import allure
import pytest

from utils.driver_factory import create_driver


@pytest.fixture()
def driver():

    driver = create_driver()

    yield driver

    if hasattr(pytest, "rep_call") and pytest.rep_call.failed:
        allure.attach(
            driver.get_screenshot_as_png(),
            name="Screenshot",
            attachment_type=allure.attachment_type.PNG
        )

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield

    rep = outcome.get_result()

    setattr(pytest, "rep_" + rep.when, rep)