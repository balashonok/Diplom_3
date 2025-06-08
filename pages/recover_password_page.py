import allure
from pages.base_page import BasePage
from data.urls import URLs
from data.data import USER_EMAIL
from locators.recover_password_locators import RecoverPasswordLocators

class RecoverPasswordPage(BasePage):

    @allure.step('Перейти на страницу авторизации')
    def get_login_page(self):
        self.get_url(URLs.LOGIN_PAGE)
        self.wait_overlaying_element_disappeared()

    @allure.step('Перейти на страницу восстановления пароля')
    def get_forgot_password_page(self):
        self.get_url(URLs.FORGOT_PASSWORD_PAGE)
        self.wait_overlaying_element_disappeared()

    @allure.step('Перейти на страницу ввода пароля для восстановления')
    def get_recover_password_page(self):
        self.get_forgot_password_page()
        self.wait_overlaying_element_disappeared()
        self.add_text_to_email()
        self.wait_overlaying_element_disappeared()
        self.click_to_recover()

    @allure.step('Кликнуть на ссылку "Восстановить пароль"')
    def click_recover_password(self):
        self.wait_overlaying_element_disappeared()
        self.click_to_element_with_wait(RecoverPasswordLocators.RECOVER_PASSWORD_LINK)

    @allure.step('Проверить, что отображен заголовок "Восстановление пароля"')
    def recover_password_is_displayed(self):
        return self.is_displayed(RecoverPasswordLocators.RECOVER_PASSWORD_HEAD)

    @allure.step('Заполнить поле Email')
    def add_text_to_email(self):
        self.add_text_to_element(RecoverPasswordLocators.EMAIL_FIELD, USER_EMAIL)

    @allure.step('Кликнуть на кнопку "Восстановить"')
    def click_to_recover(self):
        self.click_to_element_with_wait(RecoverPasswordLocators.RECOVER_PASSWORD_BUTTON)

    @allure.step('Проверить, что отображено поле "Пароль"')
    def field_password_is_displayed(self):
        return self.is_displayed(RecoverPasswordLocators.PASSWORD_FIELD)

    @allure.step('Кликнуть по элементу "Показать пароль"')
    def show_password(self):
        self.wait_overlaying_element_disappeared()
        self.click_to_element_with_wait(RecoverPasswordLocators.SHOW_PASSWORD_ICON)

    @allure.step('Проверить, что поле "Пароль" активно')
    def field_password_is_focused(self):
        return self.is_displayed(RecoverPasswordLocators.PASSWORD_FIELD_IS_FOCUSED)