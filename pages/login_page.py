import allure

from pages.base_page import BasePage
from data.urls import URLs
from data.data import USER_EMAIL, USER_PASSWORD
from locators.general_page_locators import GeneralPageLocators

class LoginPage(BasePage):

    @allure.step('Авторизоваться')
    def user_login(self):
        self.get_url(URLs.LOGIN_PAGE)
        self.add_text_to_element(GeneralPageLocators.EMAIL_INPUT, USER_EMAIL)
        self.add_text_to_element(GeneralPageLocators.PASSWORD_INPUT, USER_PASSWORD)
        self.click_to_element_with_wait(GeneralPageLocators.LOGIN_BUTTON)
