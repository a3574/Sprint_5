import random
import time
class UserData:
    @staticmethod
    def get_user_data(): # Генерация пользовательских данные для входа, для использования в тестах, где нужно проверять функциональность авторизации\аутентификации. Логин собирается из моей фамилии и когорты и метки времени. Пароль собирается рандомно из списка разрешенных символов внутри функции и ограничен размерностью от 6и до 16 символов. Возвращает логин и пароль.
        digits = '0123456789'
        uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        lowercase = 'abcdefghijklmnopqrstuvwxyz'
        punctuation = '!#$%&*+-=?@^_'

        user_data = {'login': f"orechov17_{time.time()}", 'email': f"orechov17_{time.time()}@anypost.org", 'password': '', 'password_less_6': '', 'incorrect_password': ''}
        # Генерация пароля аккаунта
        for i in range(random.randrange(6, 16)):
            user_data['password'] += random.choice(digits + uppercase + lowercase + punctuation)

        # Генерация пароля аккаунта меньше 6 символов
        for i in range(random.randrange(1, 5)):
            user_data['password_less_6'] += random.choice(digits + uppercase + lowercase + punctuation)

        # Генерация неправильного пароля аккаунта
        for i in range(random.randrange(6, 16)):
            user_data['incorrect_password'] += random.choice(digits + uppercase + lowercase + punctuation)
        if user_data['incorrect_password'] == user_data['password']:
            user_data['incorrect_password'] += '1'

        return user_data
