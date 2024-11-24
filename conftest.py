import pytest

from selene import browser, be, have
from selenium import webdriver

@pytest.fixture()
def browser_config():
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'
    browser.config.window_width = 720
    browser.config.window_height = 1280
    browser.config.timeout = 20
    browser.config.driver_options = driver_options

@pytest.fixture(autouse=True)
def open_browser(browser_config):
    browser.open('https://google.com/ncr')
    yield
    browser.quit()


