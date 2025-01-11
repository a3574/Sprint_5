import pytest
from selenium.webdriver.support import expected_conditions
from locators import RegisterPageLocators, LoginPageLocators, ProfilePageLocators, MainPageLocators, ForgotPasswordPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from tests_registration import Registration
import time
@pytest.mark.usefixtures("varius_user_data")
class Entrance:
    def entrance(self, email, password):
        # Заполняем форму входа
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(LoginPageLocators.ENTRY_BUTTON))
        self.driver.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys(email)
        self.driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(password)
        self.driver.find_element(*LoginPageLocators.ENTRY_BUTTON).click()
        return self.driver

    def check_entrance(self):
        # Ожидаем переход на главную страницу, где доступна ссылка на ЛК
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(MainPageLocators.PROFILE_PAGE))
        # Переходим в ЛК
        self.driver.find_element(*MainPageLocators.PROFILE_PAGE).click()
        # Ожидаем переход в ЛК
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(ProfilePageLocators.LOGIN_FIELD))
        # Возвращаем логин из ЛК
        return self.driver.find_element(*ProfilePageLocators.LOGIN_FIELD).get_attribute("value")

class TestEntrance(Registration, Entrance):

    def test_entrance_with_incorrect_password_not_entrance(self, varius_user_data):
        # Регистрируем нового пользователя
        self.registered(self.login, self.email, self.password)
        # Ожидаем переход на форму входа
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(LoginPageLocators.ENTRY_LABEL))
        self.entrance(self.email, self.incorrect_password)
        time.sleep(1)
        assert self.driver.current_url == "https://stellarburgers.nomoreparties.site/login"
         
    def test_entrance_from_main_page_successful_entrance(self, varius_user_data):
        # Регистрируем нового пользователя
        self.registered(self.login, self.email, self.password)
        # Переходим на главную страницу
        self.driver.get("https://stellarburgers.nomoreparties.site")
        # Ожидаем доступности кнопки "Войти в аккаунт"
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(MainPageLocators.ENTRY_BUTTON))
        self.driver.find_element(*MainPageLocators.ENTRY_BUTTON).click()
        self.entrance(self.email, self.password)
        assert self.check_entrance() == self.login
        
    def test_entrance_from_profile_page_successful_entrance(self, varius_user_data):
        # Регистрируем нового пользователя
        self.registered(self.login, self.email, self.password)
        # Переходим на главную страницу
        self.driver.get("https://stellarburgers.nomoreparties.site")
        # Ожидаем доступности ссылки на ЛК с главной страницы
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(MainPageLocators.PROFILE_PAGE))
        self.driver.find_element(*MainPageLocators.PROFILE_PAGE).click()
        # Ожидаем доступности кнопки "Войти" на странице входа
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(LoginPageLocators.ENTRY_BUTTON))
        self.entrance(self.email, self.password)
        assert self.check_entrance() == self.login

    def test_entrance_from_profile_page_successful_entrance(self, varius_user_data):
        # Регистрируем нового пользователя
        self.registered(self.login, self.email, self.password)
        # Переходим на форму регистрации
        self.driver.get("https://stellarburgers.nomoreparties.site/register")

        # Ожидаем доступности ссылки на ЛК с главной страницы
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(RegisterPageLocators.ENTRY_LABEL))
        self.driver.find_element(*RegisterPageLocators.ENTRY_LABEL).click()

        # Ожидаем доступности кнопки "Войти" на странице входа
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(LoginPageLocators.ENTRY_BUTTON))
        self.entrance(self.email, self.password)
        assert self.check_entrance() == self.login

    def test_entrance_from_forgot_password_page_successful_entrance(self, varius_user_data):
        # Регистрируем нового пользователя
        self.registered(self.login, self.email, self.password)
        # Переходим на форму восстановления пароля
        self.driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
        # Ожидаем доступности кнопки восстановления пароля
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(ForgotPasswordPageLocators.RESTORE_BUTTON))
        # Нажимаем кнопку войти
        self.driver.find_element(*ForgotPasswordPageLocators.ENTRY_LABEL).click()
        # Ожидаем перехода на форму входа
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(LoginPageLocators.ENTRY_LABEL))
        self.entrance(self.email, self.password)
        assert self.check_entrance() == self.login