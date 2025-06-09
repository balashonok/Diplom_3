import allure

from pages.personal_account_page import PersonalAccountPage

@allure.feature('Личный кабинет')
class TestPersonalAccount:

    @allure.title('Проверка перехода по клику на «Личный кабинет»')
    def test_get_personal_account(self, driver, login):
        page = PersonalAccountPage(driver)
        page.click_personal_account()
        assert page.profile_is_displayed()

    @allure.title('Проверка перехода в раздел «История заказов»')
    def test_get_history_of_orders(self, driver, login):
        page = PersonalAccountPage(driver)
        page.click_personal_account()
        page.click_history_of_orders()
        assert page.list_of_orders_is_displayed()

    @allure.title('Проверка выхода из аккаунта')
    def test_logout(self, driver, login):
        page = PersonalAccountPage(driver)
        page.click_personal_account()
        page.click_logout()
        assert page.login_is_displayed()
