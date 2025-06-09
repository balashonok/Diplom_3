import allure

from pages.order_feed_page import OrderFeedPage

@allure.feature('Раздел «Лента заказов»')
class TestOrderFeed:

    @allure.title('При клике на заказ, открывается всплывающее окно с деталями')
    def test_click_order(self, driver):
        page = OrderFeedPage(driver)
        page.get_order_feed_page()
        page.click_order()
        assert page.order_window_is_displayed()

    @allure.title('Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_order_from_order_history_displaying_in_feed(self, driver, login):
        page = OrderFeedPage(driver)
        order_number = page.create_order_and_get_order_number()
        assert page.find_order_in_feed(order_number)

    @allure.title('При создании нового заказа счётчик «Выполнено за всё время» увеличивается')
    def test_creating_order_increases_counter_of_all_orders(self, driver, login):
        page = OrderFeedPage(driver)
        counter_before = page.get_counter_of_all_orders()
        page.get_main_page()
        page.create_order_and_find_in_feed()
        counter_after = page.get_counter_of_all_orders()
        assert counter_after > counter_before

    @allure.title('При создании нового заказа счётчик «Выполнено за сегодня» увеличивается')
    def test_creating_order_increases_counter_of_today(self, driver, login):
        page = OrderFeedPage(driver)
        counter_before = page.get_counter_of_today_orders()
        page.get_main_page()
        page.create_order_and_find_in_feed()
        counter_after = page.get_counter_of_today_orders()
        assert counter_after > counter_before

    @allure.title('После оформления заказа его номер появляется в разделе «В работе»')
    def test_created_order_displaying_in_work(self, driver, login):
        page = OrderFeedPage(driver)
        order_number = page.create_order_and_get_order_number()
        assert page.find_order_in_work(order_number)