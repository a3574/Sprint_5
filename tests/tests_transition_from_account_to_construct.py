import pytest
from selenium.webdriver.support import expected_conditions
from locators import RegisterPageLocators, LoginPageLocators, ProfilePageLocators, MainPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from helpers import UserData

class TestTransitionFromAccountToConstructSuccess():
    def test_transition_from_account_to_construct_success(self):
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
        # Ожидаем видимости ссылки на конструктор
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(ProfilePageLocators.CONSTRUCTOR_LABEL))
        # Переход в конструктор
        self.driver.find_element(*ProfilePageLocators.CONSTRUCTOR_LABEL).click()
        # Ожидаем видимости ссылки на конструктор
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(MainPageLocators.CONSTRUCTOR_LABEL))
        assert self.driver.current_url == "https://stellarburgers.nomoreparties.site/"
