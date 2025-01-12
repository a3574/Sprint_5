from selenium.webdriver.common.by import By
class RegisterPageLocators:
    LOGIN_FIELD = (By.XPATH, ".//label[text()='Имя']/following-sibling::input")
    EMAIL_FIELD = (By.XPATH, ".//label[text()='Email']/following-sibling::input")
    PASSWORD_FIELD = (By.XPATH, ".//label[text()='Пароль']/following-sibling::input")
    REGISTER_BUTTON = (By.XPATH, ".//button[text()='Зарегистрироваться']")
    WRONG_PASSWORD_LABEL = (By.XPATH, ".//*[text()='Некорректный пароль']")
    ENTRY_LABEL = (By.XPATH, ".//*[text()='Войти']")

class LoginPageLocators:
    ENTRY_LABEL = (By.XPATH, ".//*[text()='Вход']")
    EMAIL_FIELD = (By.XPATH, ".//label[text()='Email']/following-sibling::input")
    PASSWORD_FIELD = (By.XPATH, ".//label[text()='Пароль']/following-sibling::input")
    ENTRY_BUTTON = (By.XPATH, ".//button[text()='Войти']")
    FORGOT_PASSWORD_LABEL = (By.XPATH, ".//*[text()='Восстановить пароль']")

class ProfilePageLocators:
    LOGIN_FIELD = (By.XPATH, ".//label[text()='Имя']/following-sibling::input")
    EMAIL_FIELD = (By.XPATH, ".//label[text()='Email']/following-sibling::input")
    PASSWORD_FIELD = (By.XPATH, ".//label[text()='Пароль']/following-sibling::input")
    CONSTRUCTOR_LABEL = (By.XPATH, ".//*[text()='Конструктор']")
    EXIT_BUTTON = (By.XPATH, ".//button[text()='Выход']")

class MainPageLocators:
    ENTRY_BUTTON = (By.XPATH, ".//button[text()='Войти в аккаунт']")
    PROFILE_PAGE = (By.XPATH, ".//a[@href = '/account']")
    CONSTRUCTOR_LABEL = (By.XPATH, ".//*[text()='Соберите бургер']")
    BUN_SPAN = (By.XPATH, ".//span[text()='Булки']")
    BUN_DIV = (By.XPATH, ".//span[text()='Булки']/parent::div")
    SAUCES_SPAN = (By.XPATH, ".//span[text()='Соусы']")
    SAUCES_DIV = (By.XPATH, ".//span[text()='Соусы']/parent::div")
    FILLING_SPAN = (By.XPATH, ".//span[text()='Начинки']/parent::div")
    FILLING_DIV = (By.XPATH, ".//span[text()='Начинки']/parent::div")

class ForgotPasswordPageLocators:
    RESTORE_BUTTON = (By.XPATH, ".//button[text()='Восстановить']")
    ENTRY_LABEL = (By.XPATH, ".//*[text()='Войти']")