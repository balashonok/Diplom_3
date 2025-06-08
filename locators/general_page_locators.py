from selenium.webdriver.common.by import By

class GeneralPageLocators:
    OVERLAY = By.XPATH, '//*[contains(@class,  "Modal_modal__loading")]/following::div[@class="Modal_modal_overlay__x2ZCr"]' # перекрывающее окно
    REGISTER_LINK = (By.LINK_TEXT, "Зарегистрироваться")  # Окно входа с полями майл и пароль, ссылка "Зарегистрироваться"
    NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input[@name='name']")  # Окно регистрации, поле 'Имя'
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']") # Окно регистрации, кнопка 'Зарегистрироваться'
    ERROR_INCORRECT_PASSWORD = (By.XPATH, "//p[text()='Некорректный пароль']") # Ошибка 'Некорректный пароль'
    PERSONAL_ACCOUNT = (By.XPATH, "//p[text()='Личный Кабинет']") # Кнопка 'Личный Кабинет'
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']") # Ссылка 'Войти' на странице регистрации
    CREATE_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']") # Кнопка 'Оформить заказ'
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input[@name='name']")  # Поле 'Email'
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")  # Поле 'Пароль'
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")  # Кнопка 'Войти'
    INGREDIENT = (By.CLASS_NAME, 'BurgerIngredient_ingredient__1TVf6') # Ингредиент на главной странице
    BASKET = (By.CLASS_NAME, 'BurgerConstructor_basket__29Cd7')
    ORDER_FEED_BUTTON = (By.XPATH, "//p[text() = 'Лента Заказов']")  # Кнопка 'Лента заказов'