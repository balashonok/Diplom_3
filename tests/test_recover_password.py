import allure

from pages.recover_password_page import RecoverPasswordPage

class TestRecoverPassword:

    @allure.title('Проверка перехода на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_recover_password(self, driver):
        page = RecoverPasswordPage(driver)
        page.get_login_page()
        page.click_recover_password()
        assert page.recover_password_is_displayed()

    @allure.title('Проверка ввода почты и клик по кнопке «Восстановить»')
    def test_enter_email(self, driver):
        page = RecoverPasswordPage(driver)
        page.get_forgot_password_page()
        page.add_text_to_email()
        page.click_to_recover()
        assert page.field_password_is_displayed()

    @allure.title('Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    def test_click_show_password(self, driver):
        page = RecoverPasswordPage(driver)
        page.get_recover_password_page()
        page.show_password()
        assert page.field_password_is_focused()

