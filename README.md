# Проект автоматизации тестирования сервиса Stellar Burgers

*Stellar Burgers - сервис для сбора и заказа космических булочек*</br>
*Основа для написания автотестов — фреймворк pytest*</br>
*Команда для запуска — pytest -v*



## Описание тестов

1. Файл tests_registration.py
+ **Class TestRegistration** - содержит тесты для проверки регистрации пользователя </br>
  - test_registration_true - проверка успешной авторизации
  - test_registration_wrong_password_shows_error - проверка вывода ошибки при невалидном пароле
2. Файл tests_login.py
+ **Class TestLogin** - содержит тесты для проверки авторизации пользователя </br>
  - test_login_by_enter_to_account_button_true - вход через кнопку "Войти в аккаунт"
  - test_login_by_user_account_true - вход через Личный кабинет
  - test_login_by_registration_form_true - вход через кнопку в форме регистрации
  - test_login_by_reset_password_true - вход через кнопку в разделе Восстановления пароля
3. Файл tests_user_account.py
+ **Class TestUserAccount** - содержит тесты для перехода в Личный кабинет конктретного юзера </br>
  - test_go_to_user_account_true - переход в Личный кабинет
4. Файл tests_go_to_constructor.py
+ **Сlass TestConstructor** - содержит тесты для перехода к конструктору </br>
  - test_go_to_constructor_by_button_constructor_true - переход в конструктор через кнопку "Конструктор"
  - test_go_to_constructor_by_logo_true - переход в конструктор через логотип
5. Файл tests_exit_from_account.py
+ **Class TestExitFromAccount** - содержит тесты для выхода из аккаунта </br>
  - test_exit_from_user_account_true - выход из аккаунта
6. Файл tests_constructor_sections.py
+ **Class TestConstructorSections** - содержит тесты для переходок разделам конструктора </br>
   - test_constructor_section_with_buns_true - проверка перехода к разделу с булками
   - test_constructor_section_with_sauces_true - проверка перехода к разделу с соусами
   - test_constructor_section_with_fillings_true - проверка перехода к разделу с начинками

## Дополнительные файлы

1. Файл conftest.py - содержит следующие фикстуры:
   - **get_driver** - для открытия/инициализации/закрытия браузера
   - **random_email_password** - для создания уникального email и рандомного пароля при регистрации (используются 4 цифры, так как с 3 уже много паролей занято)


2. Файл test_locators.py - содержит локаторы, которые использовались в автотестах. 
Локаторы разделены на блоки для удобства


3. Файл user_number_for_register.txt - файл для сохранения состояния, 
чтобы при каждом следующем прогоне теста с регистрацией создавался уникальный логин, которого еще точно нет в базе. Уникальными будут 4 цифры после номера когорты 
