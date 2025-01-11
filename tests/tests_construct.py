import pytest
from locators import MainPageLocators
class TestConctruct:
    def test_construct_move_to_bun_success(self):
        # Переходим на главную страницу
        self.driver.get("https://stellarburgers.nomoreparties.site")
        # Перехожу к разделу соусов, чтобы потом проверить переход к булкам
        self.driver.find_element(*MainPageLocators.SAUCES_SPAN).click()
        self.driver.find_element(*MainPageLocators.BUN_SPAN).click()
        assert self.driver.find_element(*MainPageLocators.BUN_SPAN).is_enabled()
    def test_construct_move_to_sauces_success(self):
        # Переходим на главную страницу
        self.driver.get("https://stellarburgers.nomoreparties.site")
        # Перехожу к разделу соусов
        self.driver.find_element(*MainPageLocators.SAUCES_SPAN).click()
        assert self.driver.find_element(*MainPageLocators.SAUCES_SPAN).is_enabled()
    def test_construct_move_to_filling_success(self):
        # Переходим на главную страницу
        self.driver.get("https://stellarburgers.nomoreparties.site")
        # Перехожу к разделу начинок
        self.driver.find_element(*MainPageLocators.FILLING_SPAN).click()
        assert self.driver.find_element(*MainPageLocators.FILLING_SPAN).is_enabled()