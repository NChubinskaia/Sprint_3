from selenium.webdriver.common.by import By


class TestLocators:

    # Хэдер

    LOGO = By.XPATH, '//div[@class = "AppHeader_header__logo__2D0X2"]'                              # логотип с бургером
    USER_ACCOUNT_BUTTON = By.XPATH, '//p[text() = "Личный Кабинет"]'                           # кнопка "Личный кабинет"
    CONSTRUCTOR_BUTTON = By.XPATH, '//p[text() = "Конструктор"]'                           # ссылка-кнопка "Конструктор"

    # Главная страница с конструктором

    HEADER_MAIN_PAGE = By.XPATH, '//h1[text() = "Соберите бургер"]'                        # заголовок "Соберите бургер"
    SIGN_IN_BUTTON = By.XPATH, '//button[text() = "Войти в аккаунт"]'                         # кнопка "Войти в аккаунт"
    BUNS_HEADER = By.XPATH, '//h2[text() = "Булки"]'                                   # заголовок для раздела с булками
    BUNS_SECTION = By.XPATH, '//span[text() = "Булки"]/parent::div'            # кнопка для перехода к разделу с булками
    SAUCE_HEADER = By.XPATH, '//h2[text() = "Соусы"]'                                  # заголовок для раздела с соусами
    SAUCE_SECTION = By.XPATH, '//span[text() = "Соусы"]/parent::div'           # кнопка для перехода к разделу с соусами
    FILLING_HEADER = By.XPATH, '//h2[text() = "Начинки"]'                            # заголовок для раздела с начинками
    FILLING_SECTION = By.XPATH, '//span[text() = "Начинки"]/parent::div'     # кнопка для перехода к разделу с начинками

    # Страница регистрации /register

    REG_NAME_INPUT = By.XPATH, '//label[text() = "Имя"]/following-sibling::input'                 # поле "Имя" /register
    REG_EMAIL_INPUT = By.XPATH, '//label[text() = "Email"]/following-sibling::input'            # поле "Email" /register
    REG_PASSWORD_INPUT = By.XPATH, '//label[text() = "Пароль"]/following-sibling::input'       # поле "Пароль" /register
    REGISTER_BUTTON = By.XPATH, '//button[text() = "Зарегистрироваться"]'                  # кнопка "Зарегистрироваться"
    REG_PASSWORD_ERROR = By.CSS_SELECTOR, '.input__error'                                 # ошибка при невалидном пароле
    REG_LOGIN = By.XPATH, '//p[text() = "Уже зарегистрированы?"]/a[text() = "Войти"]'         # ссылка "Войти" -> /login

    # Страница входа /login

    LOGIN_HEADER = By.XPATH, '//h2[text() = "Вход"]'                                           # заголовок "Вход" /login
    LOGIN_EMAIL_INPUT = By.XPATH, '//label[text() = "Email"]/following-sibling::input'          # поле для логина /login
    LOGIN_PASSWORD_INPUT = By.XPATH, '//label[text() = "Пароль"]/following-sibling::input'      # поле для пароля /login
    LOGIN_BUTTON = By.XPATH, '//button[text() = "Войти"]'                                        # кнопка "Войти" /login

    # Страница восстановления пароля /reset-password

    RESET_PASS_HEADER = By.XPATH, '//h2[text() = "Восстановление пароля"]'           # заголовок "Восстановление пароля"
    RESET_PASS_LOGIN = By.XPATH, '//p[text() = "Вспомнили пароль?"]/a[text() = "Войти"]'      # ссылка "Войти" -> /login

    # Профиль клиента /profile

    PROFILE_NAME_INPUT = By.XPATH, '//label[text() = "Имя"]/following-sibling::input'          # поле с именем в профиле
    PROFILE_EMAIL_INPUT = By.XPATH, '//label[text() = "Логин"]/following-sibling::input'        # поле с email в профиле
    PROFILE_LINK = By.XPATH, '//a[text() = "Профиль"]'                                                # ссылка "Профиль"
    PROFILE_QUIT_BUTTON = By.XPATH, '//button[text() = "Выход"]'                              # кнопка "Выход" в профиле
