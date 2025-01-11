import pytest
from selenium import webdriver
import random
import time
@pytest.fixture(autouse = True, scope = "function")
def get_driver(request): #Автоматическое открытие браузера на каждый отдельно взятый тест и закрытие после его проведения.
    driver = webdriver.Chrome()
    request.cls.driver = driver
    yield
    driver.quit()

@pytest.fixture
def varius_user_data(request): # Генерация пользовательских данные для входа, для использования в тестах, где нужно проверять функциональность авторизации\аутентификации. Логин собирается из моей фамилии и когорты и метки времени. Пароль собирается рандомно из списка разрешенных символов внутри функции и ограничен размерностью от 6и до 16 символов. Возвращает логин и пароль.
    digits = '0123456789'
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    punctuation = '!#$%&*+-=?@^_'

    varius_password = ''
    for i in range(random.randrange(6, 16)):
        varius_password += random.choice(digits + uppercase + lowercase + punctuation)

    varius_password_less_6 = ''
    for i in range(random.randrange(1, 5)):
        varius_password_less_6 += random.choice(digits + uppercase + lowercase + punctuation)

    varius_incorrect_password = ''
    for i in range(random.randrange(6, 16)):
        varius_incorrect_password += random.choice(digits + uppercase + lowercase + punctuation)

    request.cls.login = f"orechov17_{time.time()}"
    request.cls.email = f"orechov17_{time.time()}@anypost.org"
    request.cls.password = varius_password
    request.cls.password_less_6 = varius_password_less_6
    request.cls.incorrect_password = varius_incorrect_password if varius_password != varius_incorrect_password else varius_incorrect_password + '1'
