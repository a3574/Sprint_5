import pytest
from selenium.webdriver.support import expected_conditions
from locators import RegisterPageLocators, LoginPageLocators, ProfilePageLocators, MainPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from helpers import UserData

class TestLogout():
    def test_logout_from_profile_page_success(self):
        # Регистрируем нового пользователя
        user_data = UserData.get_user_data()
        # Переходим на форму регистрации
        self.driver.get("https://stellarburgers.nomoreparties.site/register")
        # Заполняем форму регистрации
        self.driver.find_element(*RegisterPageLocators.LOGIN_FIELD).send_keys(user_data['login'])
        self.driver.find_element(*RegisterPageLocators.EMAIL_FIELD).send_keys(user_data['email'])
        self.driver.find_element(*RegisterPageLocators.PASSWORD_FIELD).send_keys(user_data['password'])
        self.driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()

        # Ожидаем переход на форму входа
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(LoginPageLocators.ENTRY_LABEL))

        # Заполняем форму входа
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(LoginPageLocators.ENTRY_BUTTON))
        self.driver.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys(user_data['email'])
        self.driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(user_data['password'])
        self.driver.find_element(*LoginPageLocators.ENTRY_BUTTON).click()

        # Ожидаем переход на главную страницу, где доступна ссылка на ЛК
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(MainPageLocators.PROFILE_PAGE))
        #Переходим в ЛК
        self.driver.find_element(*MainPageLocators.PROFILE_PAGE).click()
        # Ожидаем видимости кнопки Выход
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(ProfilePageLocators.EXIT_BUTTON))
        # Выходим из аккаунта
        self.driver.find_element(*ProfilePageLocators.EXIT_BUTTON).click()
        # Ожидаем перехоод на форму входа
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(LoginPageLocators.ENTRY_LABEL))
        assert self.driver.current_url == "https://stellarburgers.nomoreparties.site/login"