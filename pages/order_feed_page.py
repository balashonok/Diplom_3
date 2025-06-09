import allure
from pages.base_page import BasePage
from data.urls import URLs
from locators.order_feed_locators import OrderFeedLocators
from locators.general_page_locators import GeneralPageLocators

class OrderFeedPage(BasePage):

    @allure.step('Перейти на страницу ленты заказов')
    def get_order_feed_page(self):
        self.get_url(URLs.ORDER_FEED_PAGE)

    @allure.step('Перейти на главную страницу')
    def get_main_page(self):
        self.get_url(URLs.MAIN_PAGE)

    @allure.step('Кликнуть на заказ')
    def click_order(self):
        self.click_to_element_with_wait(OrderFeedLocators.ORDER)

    @allure.step('Проверить, что появилось всплывающее окно с деталями заказа')
    def order_window_is_displayed(self):
        return self.is_displayed(OrderFeedLocators.ORDER_WINDOW)

    @allure.step('Создать заказ')
    def create_order(self):
        self.drag_and_drop_element(GeneralPageLocators.INGREDIENT, GeneralPageLocators.BASKET)
        self.click_to_element_with_wait(OrderFeedLocators.CREATE_ORDER)

    @allure.step('Создать и получить номер заказа')
    def create_order_and_get_order_number(self):
        self.create_order()
        self.wait_for_invisibility_of_element(OrderFeedLocators.ORDER_NUMBER_9999)
        return self.get_text_from_element(OrderFeedLocators.ORDER_NUMBER)

    @allure.step('Найти заказ в ленте заказов')
    def find_order_in_feed(self, order_number):
        self.get_order_feed_page()
        locator_formatted = self.format_locators(OrderFeedLocators.ORDER_IN_FEED, order_number)
        return self.find_element_with_wait(locator_formatted)

    @allure.step('Создать заказ и найти его в ленте заказов')
    def create_order_and_find_in_feed(self):
        self.find_order_in_feed(self.create_order_and_get_order_number())

    @allure.step('Получить общее количество заказов')
    def get_counter_of_all_orders(self):
        self.click_to_element_with_wait(GeneralPageLocators.ORDER_FEED_BUTTON)
        return self.get_text_from_element(OrderFeedLocators.COUNTER_OF_ALL_ORDERS)

    @allure.step('Получить количество заказов за сегодня')
    def get_counter_of_today_orders(self):
        self.click_to_element_with_wait(GeneralPageLocators.ORDER_FEED_BUTTON)
        self.wait_and_scroll_to_element(OrderFeedLocators.COUNTER_OF_TODAY_ORDERS)
        return self.get_text_from_element(OrderFeedLocators.COUNTER_OF_TODAY_ORDERS)

    @allure.step('Найти заказ в разделе «В работе»')
    def find_order_in_work(self, order_number):
        order_number_str = str(order_number)
        self.get_order_feed_page()
        locator_formatted = self.format_locators(OrderFeedLocators.ORDER_IN_WORK, order_number_str)
        return self.find_element_with_wait(locator_formatted)
