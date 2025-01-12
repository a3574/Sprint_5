import pytest
from selenium import webdriver

@pytest.fixture(autouse = True, scope = "function")
def get_driver(request): #Автоматическое открытие браузера на каждый отдельно взятый тест и закрытие после его проведения.
    driver = webdriver.Chrome()
    request.cls.driver = driver
    yield
    driver.quit()
