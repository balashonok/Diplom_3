from selenium.webdriver.common.by import By

class RecoverPasswordLocators:
    RECOVER_PASSWORD_LINK = (By.LINK_TEXT, 'Восстановить пароль')
    RECOVER_PASSWORD_HEAD = (By.XPATH, "//h2[text()='Восстановление пароля']")
    EMAIL_FIELD = (By.CLASS_NAME, "input__textfield")
    RECOVER_PASSWORD_BUTTON = (By.XPATH, '//button[text()="Восстановить"]')
    PASSWORD_FIELD = (By.XPATH, "//label[text()='Пароль']")
    SHOW_PASSWORD_ICON = (By.CLASS_NAME, "input__icon-action")
    PASSWORD_FIELD_IS_FOCUSED = (By.CLASS_NAME, "input__placeholder-focused")