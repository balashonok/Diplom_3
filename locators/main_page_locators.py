from selenium.webdriver.common.by import By

class MainPageLocators:
    CONSTRUCTOR = (By.XPATH, "//p[text()='Конструктор']")  # Кнопка 'Конструктор'
    MAKE_BURGER_HEADER = (
    By.XPATH, "//h1[text() = 'Соберите бургер']")  # Заголовок 'Соберите бургер' на главно странице
    ORDER_FEED_HEADER = (
        By.XPATH, "//h1[text() = 'Лента заказов']")  # Заголовок 'Лента заказов'
    INGREDIENT_DETAILS = (By.XPATH, "//h2[text() = 'Детали ингредиента']") # Модальное окно с деталями ингредиента
    CLOSE_INGREDIENT = (By.CLASS_NAME, 'Modal_modal__close_modified__3V5XS') # Крестик в окне ингредиента
    COUNTER = (By.CLASS_NAME, 'counter_counter__num__3nue1')



