# Sprint_5


# Структура файлов:
#   папка tests, в ней находятся все тесты. Отельный файл на функциональность.
#   папка locators, в ней находятся все локаторы. Отдельный локатор на каждую страницу магазина.
#   в файле conftest все фикстуры

# Список тестов:
#   tests_registration - тесты регистрации
#       test_registration_on_valid_data_succes_registration - Тест для проверки успешной регистриции при заполненном login и пароле больше 6 символов. За успехом считаю дальнейший успешный вход на сайт и отображение корректного логина в ЛК.
#       test_registration_without_login_not_registered - Тест для проверки того, что не удастся зарегистрировать пользователя без логина
#       test_registration_with_wrong_email_not_registered - Тест для проверки того, что не удастся зарегистрировать с некорректной почтой
#       test_registration_with_password_less_6_char_not_registered - Тест для проверки того, что не удастся зарегистрировать с паролем меньше минимальной длины в 6 символов

#   tests_entrance - тесты на проверку входа в аккаунт
#       test_entrance_with_incorrect_password_not_entrance - Тест для проверки входа с неверным паролем
#       test_entrance_from_main_page_successful_entrance - Тест на вход через кнопку «Войти в аккаунт» на главной
#       test_entrance_from_profile_page_successful_entrance - Тест на вход через кнопку «Войти» на странице «Личный кабинет»
#       test_entrance_from_registration_page_successful_entrance - Тест на вход через форму регистрации,
#       test_entrance_from_forgot_password_page_successful_entrance - Тест на  вход через кнопку в форме восстановления пароля.

#   tests_transition_to_account - тесты на переход в личный кабинет
#       test_transition_to_account_from_main_success - тест на переход в личный кабинет с главной страницы

#   tests_transition_from_account_to_construct - тесты на переход из личного кабинета в конструктор бургеров
#       test_transition_from_account_to_construct_success

#   tests_logout - тесты выхода из аккаунта
#       test_logout_from_profile_page_success - Тест на удачный выход из аккаунта со страницы ЛК

#   tests_construct - тесты конструктора бургеров
#       test_construct_move_to_bun_success - Тест на переход к разделу Булки
#       test_construct_move_to_sauces_success - Тест на переход к разделу Соусы
#       test_construct_move_to_filling_success - Тест на переход к разделу Начинки