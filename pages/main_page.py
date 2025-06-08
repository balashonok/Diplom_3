import allure
from pages.base_page import BasePage
from data.urls import URLs
from locators.main_page_locators import MainPageLocators
from locators.general_page_locators import GeneralPageLocators

class MainPage(BasePage):

    @allure.step('Перейти на главную страницу')
    def get_main_page(self):
        self.get_url(URLs.MAIN_PAGE)

    @allure.step('Перейти на страницу авторизации')
    def get_login_page(self):
        self.get_url(URLs.LOGIN_PAGE)

    @allure.step('Кликнуть на элемент «Конструктор»')
    def click_constructor(self):
        self.click_to_element_with_wait(MainPageLocators.CONSTRUCTOR)

    @allure.step('Кликнуть на элемент «Лента заказов»')
    def click_order_feed(self):
        self.click_to_element_with_wait(GeneralPageLocators.ORDER_FEED_BUTTON)

    @allure.step('Кликнуть на ингредиент')
    def click_ingredient(self):
        self.click_to_element_with_wait(GeneralPageLocators.INGREDIENT)

    @allure.step('Закрыть окно ингредиента')
    def close_ingredient(self):
        self.click_to_element_with_wait(MainPageLocators.CLOSE_INGREDIENT)

    @allure.step('Проверить, что произошёл переход в «Конструктор»')
    def constructor_is_displayed(self):
        return self.is_displayed(MainPageLocators.MAKE_BURGER_HEADER)

    @allure.step('Проверить, что произошёл переход в «Лента заказов»')
    def order_feed_is_displayed(self):
        return self.is_displayed(MainPageLocators.ORDER_FEED_HEADER)

    @allure.step('Проверить, что открыто модальное окно «Детали ингредиента»')
    def ingredient_details_is_displayed(self):
        return self.is_displayed(MainPageLocators.INGREDIENT_DETAILS)

    @allure.step('Проверить, что перестало отображаться модальное окно «Детали ингредиента»')
    def ingredient_details_is_closed(self):
        return self.wait_for_invisibility_of_element(MainPageLocators.INGREDIENT_DETAILS)

    @allure.step('Проверить, что отображена кнопка «Оформить заказ»')
    def create_order_button_is_displayed(self):
        return self.is_displayed(GeneralPageLocators.CREATE_ORDER_BUTTON)

    @allure.step('Добавить ингредиент')
    def add_ingredient(self):
        self.drag_and_drop_element(GeneralPageLocators.INGREDIENT, GeneralPageLocators.BASKET)

    @allure.step('Получить значение счетчика для ингредиента')
    def get_counter(self):
        return self.get_text_from_element(MainPageLocators.COUNTER)