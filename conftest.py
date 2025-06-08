import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions

from pages.base_page import BasePage
from data.urls import URLs
from data.data import USER_EMAIL, USER_PASSWORD
from locators.general_page_locators import GeneralPageLocators

@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    browser_name = request.param
    if request.param == "chrome":
        options = ChromeOptions()
        options.add_argument('--window-size=1920,1080')
        driver = webdriver.Chrome(options=options)
    else:
        options = FirefoxOptions()
        options.add_argument('--window-size=1920,1080')
        driver = webdriver.Firefox(options=options)

    yield driver
    driver.quit()

@pytest.fixture
def login(driver):
    page = BasePage(driver)
    page.get_url(URLs.LOGIN_PAGE)
    page.add_text_to_element(GeneralPageLocators.EMAIL_INPUT, USER_EMAIL)
    page.add_text_to_element(GeneralPageLocators.PASSWORD_INPUT, USER_PASSWORD)
    page.click_to_element_with_wait(GeneralPageLocators.LOGIN_BUTTON)
