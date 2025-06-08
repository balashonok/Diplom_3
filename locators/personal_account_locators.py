from selenium.webdriver.common.by import By

class PersonalAccountLocators:
    PROFILE = (By.XPATH, "//a[text()='Профиль']")  # Элемент 'Профиль' на странице личного кабинета
    HISTORY_OF_ORDERS = (By.XPATH, "//a[text()='История заказов']")
    LIST_OF_ORDERS = (By.XPATH, "//*[contains(@class, 'OrderHistory_orderHistory__qy1VB')]")
    LOG_OUT = (By.XPATH, "//button[text()='Выход']")  # Кнопка 'Выход'
