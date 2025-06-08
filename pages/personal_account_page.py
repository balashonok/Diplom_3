import allure
from pages.base_page import BasePage
from locators.personal_account_locators import PersonalAccountLocators
from locators.general_page_locators import GeneralPageLocators

class PersonalAccountPage(BasePage):

    @allure.step('Кликнуть на «Личный кабинет»')
    def click_personal_account(self):
        self.click_to_element_with_wait(GeneralPageLocators.PERSONAL_ACCOUNT)

    @allure.step('Кликнуть на «История заказов»')
    def click_history_of_orders(self):
        self.click_to_element_with_wait(PersonalAccountLocators.HISTORY_OF_ORDERS)

    @allure.step('Кликнуть на «Выход»')
    def click_logout(self):
        self.click_to_element_with_wait(PersonalAccountLocators.LOG_OUT)

    @allure.step('Проверить, что произошёл переход в личный кабинет')
    def profile_is_displayed(self):
        return self.is_displayed(PersonalAccountLocators.PROFILE)

    @allure.step('Проверить, что произошёл переход в «История заказов»')
    def list_of_orders_is_displayed(self):
        return self.is_displayed(PersonalAccountLocators.LIST_OF_ORDERS)

    @allure.step('Проверить, что произошёл выход из аккаунта')
    def login_is_displayed(self):
        return self.is_displayed(GeneralPageLocators.LOGIN_BUTTON)