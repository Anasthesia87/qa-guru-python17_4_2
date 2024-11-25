import pytest
from selene import browser


@pytest.fixture(scope="function", autouse=True)
def settings_browser():
    browser.config.base_url = 'https://demoqa.com'
    #browser.config.driver_name = 'edge'
    browser.config.driver.maximize_window()

    yield

    browser.quit()

