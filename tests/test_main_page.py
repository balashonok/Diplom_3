import allure

from pages.main_page import MainPage

class TestMainPage:

    @allure.title('Переход по клику на «Конструктор»')
    def test_get_constructor(self, driver):
        page = MainPage(driver)
        page.get_login_page()
        page.click_constructor()
        assert page.constructor_is_displayed

    @allure.title('Переход по клику на «Лента заказов»')
    def test_get_constructor(self, driver):
        page = MainPage(driver)
        page.get_main_page()
        page.click_order_feed()
        assert page.order_feed_is_displayed()

    @allure.title('При клике на ингредиент появится всплывающее окно с деталями')
    def test_get_ingredient(self, driver):
        page = MainPage(driver)
        page.get_main_page()
        page.click_ingredient()
        assert page.ingredient_details_is_displayed()

    @allure.title('Всплывающее окно закрывается кликом по крестику')
    def test_close_ingredient(self, driver):
        page = MainPage(driver)
        page.get_main_page()
        page.click_ingredient()
        page.close_ingredient()
        assert page.ingredient_details_is_closed()

    @allure.title('При добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента')
    def test_add_ingredient(self, driver):
        page = MainPage(driver)
        page.get_main_page()
        page.add_ingredient()
        assert page.get_counter() == '2'

    @allure.title('Залогиненный пользователь может оформить заказ')
    def test_create_order(self, driver, login):
        page = MainPage(driver)
        page.add_ingredient()
        assert page.create_order_button_is_displayed()
