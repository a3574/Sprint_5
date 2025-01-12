import pytest
from selenium.webdriver.support import expected_conditions
from locators import RegisterPageLocators, LoginPageLocators, ProfilePageLocators, MainPageLocators, ForgotPasswordPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from helpers import UserData

class TestEntrance():
    def test_entrance_with_incorrect_password_not_entrance(self):
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
        self.driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(user_data['incorrect_password'])
        self.driver.find_element(*LoginPageLocators.ENTRY_BUTTON).click()

        assert self.driver.current_url == "https://stellarburgers.nomoreparties.site/login"


    def test_entrance_from_registration_page_successful_entrance(self):

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
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.PROFILE_PAGE))
        # Переходим в ЛК
        self.driver.find_element(*MainPageLocators.PROFILE_PAGE).click()
        # Ожидаем переход в ЛК
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(ProfilePageLocators.LOGIN_FIELD))

        assert self.driver.find_element(*ProfilePageLocators.LOGIN_FIELD).get_attribute("value")
         
    def test_entrance_from_main_page_successful_entrance(self):
        # Регистрируем нового пользователя
        user_data = UserData.get_user_data()
        # Переходим на форму регистрации
        self.driver.get("https://stellarburgers.nomoreparties.site/register")
        # Заполняем форму регистрации
        self.driver.find_element(*RegisterPageLocators.LOGIN_FIELD).send_keys(user_data['login'])
        self.driver.find_element(*RegisterPageLocators.EMAIL_FIELD).send_keys(user_data['email'])
        self.driver.find_element(*RegisterPageLocators.PASSWORD_FIELD).send_keys(user_data['password'])
        self.driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()

        # Переходим на главную страницу
        self.driver.get("https://stellarburgers.nomoreparties.site")
        # Ожидаем доступности кнопки "Войти в аккаунт"
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(MainPageLocators.ENTRY_BUTTON))
        self.driver.find_element(*MainPageLocators.ENTRY_BUTTON).click()

        # Заполняем форму входа
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(LoginPageLocators.ENTRY_BUTTON))
        self.driver.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys(user_data['email'])
        self.driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(user_data['password'])
        self.driver.find_element(*LoginPageLocators.ENTRY_BUTTON).click()

        # Ожидаем переход на главную страницу, где доступна ссылка на ЛК
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.PROFILE_PAGE))
        # Переходим в ЛК
        self.driver.find_element(*MainPageLocators.PROFILE_PAGE).click()
        # Ожидаем переход в ЛК
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(ProfilePageLocators.LOGIN_FIELD))

        assert self.driver.find_element(*ProfilePageLocators.LOGIN_FIELD).get_attribute("value")

    def test_entrance_from_profile_page_successful_entrance(self):
        # Регистрируем нового пользователя
        user_data = UserData.get_user_data()
        # Переходим на форму регистрации
        self.driver.get("https://stellarburgers.nomoreparties.site/register")
        # Заполняем форму регистрации
        self.driver.find_element(*RegisterPageLocators.LOGIN_FIELD).send_keys(user_data['login'])
        self.driver.find_element(*RegisterPageLocators.EMAIL_FIELD).send_keys(user_data['email'])
        self.driver.find_element(*RegisterPageLocators.PASSWORD_FIELD).send_keys(user_data['password'])
        self.driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()

        # Переходим на главную страницу
        self.driver.get("https://stellarburgers.nomoreparties.site")
        # Ожидаем доступности ссылки на ЛК с главной страницы
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(MainPageLocators.PROFILE_PAGE))
        self.driver.find_element(*MainPageLocators.PROFILE_PAGE).click()
        # Ожидаем доступности кнопки "Войти" на странице входа
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(LoginPageLocators.ENTRY_BUTTON))

        # Заполняем форму входа
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(LoginPageLocators.ENTRY_BUTTON))
        self.driver.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys(user_data['email'])
        self.driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(user_data['password'])
        self.driver.find_element(*LoginPageLocators.ENTRY_BUTTON).click()

        # Ожидаем переход на главную страницу, где доступна ссылка на ЛК
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.PROFILE_PAGE))
        # Переходим в ЛК
        self.driver.find_element(*MainPageLocators.PROFILE_PAGE).click()
        # Ожидаем переход в ЛК
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(ProfilePageLocators.LOGIN_FIELD))

        assert self.driver.find_element(*ProfilePageLocators.LOGIN_FIELD).get_attribute("value")
    def test_entrance_from_forgot_password_page_successful_entrance(self):
        # Регистрируем нового пользователя
        user_data = UserData.get_user_data()
        # Переходим на форму регистрации
        self.driver.get("https://stellarburgers.nomoreparties.site/register")
        # Заполняем форму регистрации
        self.driver.find_element(*RegisterPageLocators.LOGIN_FIELD).send_keys(user_data['login'])
        self.driver.find_element(*RegisterPageLocators.EMAIL_FIELD).send_keys(user_data['email'])
        self.driver.find_element(*RegisterPageLocators.PASSWORD_FIELD).send_keys(user_data['password'])
        self.driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()

        # Переходим на форму восстановления пароля
        self.driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
        # Ожидаем доступности кнопки восстановления пароля
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(ForgotPasswordPageLocators.RESTORE_BUTTON))
        # Нажимаем кнопку войти
        self.driver.find_element(*ForgotPasswordPageLocators.ENTRY_LABEL).click()
        # Ожидаем перехода на форму входа
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(LoginPageLocators.ENTRY_LABEL))

        # Заполняем форму входа
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(LoginPageLocators.ENTRY_BUTTON))
        self.driver.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys(user_data['email'])
        self.driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(user_data['password'])
        self.driver.find_element(*LoginPageLocators.ENTRY_BUTTON).click()

        # Ожидаем переход на главную страницу, где доступна ссылка на ЛК
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.PROFILE_PAGE))
        # Переходим в ЛК
        self.driver.find_element(*MainPageLocators.PROFILE_PAGE).click()
        # Ожидаем переход в ЛК
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(ProfilePageLocators.LOGIN_FIELD))

        assert self.driver.find_element(*ProfilePageLocators.LOGIN_FIELD).get_attribute("value")