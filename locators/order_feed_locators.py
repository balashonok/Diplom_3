from selenium.webdriver.common.by import By

class OrderFeedLocators:
    ORDER = (By.CLASS_NAME, 'OrderHistory_link__1iNby')
    ORDER_WINDOW = (By.CLASS_NAME, 'Modal_orderBox__1xWdi')
    CREATE_ORDER = (By.XPATH, '//button[text()="Оформить заказ"]')
    ORDER_NUMBER_9999 = (By.XPATH, '//h2[text()="9999"]')
    ORDER_NUMBER = (By.CLASS_NAME, 'Modal_modal__title_shadow__3ikwq')
    ORDER_IN_FEED = (By.XPATH, '//p[text()="#0{}"]')
    COUNTER_OF_ALL_ORDERS = (By.CLASS_NAME, 'OrderFeed_number__2MbrQ')
    COUNTER_OF_TODAY_ORDERS = (By.XPATH, '//p[text()="Выполнено за сегодня:"]/following-sibling::p[contains(@class, "OrderFeed_number__2MbrQ")]')
    ORDER_IN_WORK = (By.XPATH, '//li[text()="{}"]')
