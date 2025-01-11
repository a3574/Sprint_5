import pytest
from selenium.webdriver.support import expected_conditions
from locators import LoginPageLocators, ProfilePageLocators, MainPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from tests_registration import Registration
from tests_entrance import Entrance
import time

@pytest.mark.usefixtures("varius_user_data")
class TestTransitionToAccount(Registration, Entrance):
    def test_transition_to_account_from_main_success(self, varius_user_data):
        # Регистрируем нового пользователя
        self.registered(self.login, self.email, self.password)
        # Ждем доступности формы входа
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(LoginPageLocators.ENTRY_LABEL))
        # Выполняем вход
        self.entrance(self.email, self.password)
        # Ожидаем переход на главную страницу, где доступна ссылка на ЛК
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(MainPageLocators.PROFILE_PAGE))
        #Переходим в ЛК
        self.driver.find_element(*MainPageLocators.PROFILE_PAGE).click()
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(ProfilePageLocators.LOGIN_FIELD))
        assert self.driver.current_url == "https://stellarburgers.nomoreparties.site/account/profile"
