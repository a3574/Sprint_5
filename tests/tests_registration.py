import pytest
from selenium.webdriver.support import expected_conditions
from locators import RegisterPageLocators, LoginPageLocators, ProfilePageLocators, MainPageLocators
from selenium.webdriver.support.wait import WebDriverWait

@pytest.mark.usefixtures("varius_user_data")
class Registration:
    def registered(self, login, email, password):
        # Переходим на форму регистрации
        self.driver.get("https://stellarburgers.nomoreparties.site/register")
        # Заполняем форму регистрации
        self.driver.find_element(*RegisterPageLocators.LOGIN_FIELD).send_keys(login)
        self.driver.find_element(*RegisterPageLocators.EMAIL_FIELD).send_keys(email)
        self.driver.find_element(*RegisterPageLocators.PASSWORD_FIELD).send_keys(password)
        self.driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()
        return self.driver

class TestRegistration(Registration):
    def test_registration_with_password_less_6_char_not_registered(self, varius_user_data):
        self.registered(self.login, self.email, self.password_less_6)
        # Ожидаем переход на форму входа
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(RegisterPageLocators.WRONG_PASSWORD_LABEL))
        assert self.driver.find_element(*RegisterPageLocators.WRONG_PASSWORD_LABEL)

    def test_registration_with_wrong_email_not_registered(self, varius_user_data):
        self.registered(self.login, self.login, self.password)
        # Ожидаем переход на форму входа
        WebDriverWait(self.driver, 3).until(expected_conditions.url_changes("https://stellarburgers.nomoreparties.site/login"))
        assert self.driver.current_url != "https://stellarburgers.nomoreparties.site/login"

    def test_registration_without_login_not_registered(self, varius_user_data):
        self.registered('', self.email, self.password)
        # Ожидаем переход на форму входа
        WebDriverWait(self.driver, 3).until(expected_conditions.url_changes("https://stellarburgers.nomoreparties.site/login"))
        assert self.driver.current_url != "https://stellarburgers.nomoreparties.site/login"

    def test_registration_on_valid_data_succes_registration(self, varius_user_data):
        self.registered(self.login, self.email, self.password)
        # Ожидаем переход на форму входа
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(LoginPageLocators.ENTRY_LABEL))

        # Заполняем форму входа
        self.driver.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys(self.email)
        self.driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(self.password)
        self.driver.find_element(*LoginPageLocators.ENTRY_BUTTON).click()

        # Ожидаем переход на главную страницу, где доступна ссылка на ЛК
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(MainPageLocators.PROFILE_PAGE))

        #Переходим в ЛК
        self.driver.find_element(*MainPageLocators.PROFILE_PAGE).click()

        # Ожидаем переход в ЛК
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(ProfilePageLocators.LOGIN_FIELD))

        #Проверяем, что в ЛК отражен логин по которому мы зашли
        assert self.driver.find_element(*ProfilePageLocators.LOGIN_FIELD).get_attribute("value") == self.login