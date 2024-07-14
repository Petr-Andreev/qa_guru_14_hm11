import pytest
from selenium import webdriver
from selene import browser
from selenium.webdriver.chrome import options


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    options.page_load_strategy = 'eager'

    yield
    browser.quit()
