class TestLocators:

    # Хэдер

    logo = '//div[@class = "AppHeader_header__logo__2D0X2"]'            # логотип с бургером
    user_account_button = '//p[text() = "Личный Кабинет"]'              # кнопка "Личный кабинет"
    constructor_button = '//p[text() = "Конструктор"]'                  # ссылка-кнопка "Конструктор"

    # Главная страница с конструктором

    header_main_page = '//h1[text() = "Соберите бургер"]'               # заголовок "Соберите бургер"
    sign_in_button = '//button[text() = "Войти в аккаунт"]'             # кнопка "Войти в аккаунт"
    buns_header = '//h2[text() = "Булки"]'                              # заголовок для раздела с булками
    buns_section = '//span[text() = "Булки"]/parent::div'               # кнопка для перехода к разделу с булками
    sauce_header = '//h2[text() = "Соусы"]'                             # заголовок для раздела с соусами
    sauce_section = '//span[text() = "Соусы"]/parent::div'              # кнопка для перехода к разделу с соусами
    filling_header = '//h2[text() = "Начинки"]'                         # заголовок для раздела с начинками
    filling_section = '//span[text() = "Начинки"]/parent::div'          # кнопка для перехода к разделу с начинками

    # Страница регистрации /register

    register_name_input = '//fieldset[1]//input[@name="name"]'          # поле "Имя" в форме регистрации
    register_email_input = '//fieldset[2]//input[@name="name"]'         # поле "Email" в форме регистрации
    register_password_input = '//fieldset[3]//input[@type="password"]'  # поле "Пароль" в форме регистрации
    register_button = '//button[text() = "Зарегистрироваться"]'         # кнопка "Зарегистрироваться"
    register_password_error = '.input__error'                           # выводимая ошибка при невалидном пароле
    register_link_login = 'Войти'                                       # ссылка-кнопка "Войти"

    # Страница входа /login

    login_header = '//h2[text() = "Вход"]'                              # заголовок "Вход" на странице /login
    login_email_input = '//fieldset[1]//input[@name="name"]'            # поле для ввода логина на странице /login
    login_password_input = '//fieldset[2]//input[@type="password"]'     # поле для ввода пароля на странице /login
    login_button = '//button[text() = "Войти"]'                         # кнопка "Войти" на странице /login

    # Страница восстановления пароля /reset-password

    reset_pass_header = '//h2[text() = "Восстановление пароля"]'        # Заголовок "Восстановление пароля"
    reset_pass_link_login = 'Войти'                                     # ссылка-кнопка "Войти" для перехода в /login

    # Профиль клиента /profile

    profile_name_input = "//ul/li[1]//input"                            # поле с именем пользователя в профиле
    profile_email_input = "//ul/li[2]//input"                           # поле с email пользователя в профиле
    profile_save_button = "//button[text() = 'Сохранить']"              # кнопка "Сохранить" в профиле
    profile_quit_button = '//button[text() = "Выход"]'                  # кнопка "Выход" в профиле
