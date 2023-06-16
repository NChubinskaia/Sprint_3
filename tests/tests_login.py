from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from test_locators import TestLocators

user_email_in_db = 'chubinskaia_9148@gmail.com'
user_pass_in_db = 'sprint3'


class TestLogin:

    def test_login_by_enter_to_account_button_true(self, driver):

        driver.find_element(*TestLocators.SIGN_IN_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.LOGIN_HEADER))
        driver.find_element(*TestLocators.LOGIN_EMAIL_INPUT).send_keys(user_email_in_db)
        driver.find_element(*TestLocators.LOGIN_PASSWORD_INPUT).send_keys(user_pass_in_db)
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.HEADER_MAIN_PAGE))
        header_text1 = driver.find_element(*TestLocators.HEADER_MAIN_PAGE).text
        assert 'Соберите бургер' in header_text1, f'Заголовок "{header_text1}" не совпадает'

    def test_login_by_user_account_true(self, driver):

        driver.find_element(*TestLocators.USER_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.LOGIN_HEADER))
        driver.find_element(*TestLocators.LOGIN_EMAIL_INPUT).send_keys(user_email_in_db)
        driver.find_element(*TestLocators.LOGIN_PASSWORD_INPUT).send_keys(user_pass_in_db)
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.HEADER_MAIN_PAGE))
        header_text2 = driver.find_element(*TestLocators.HEADER_MAIN_PAGE).text
        assert 'Соберите бургер' in header_text2, f'Заголовок "{header_text2}" не совпадает'

    def test_login_by_registration_form_true(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")

        driver.find_element(*TestLocators.REG_LOGIN).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.LOGIN_HEADER))
        driver.find_element(*TestLocators.LOGIN_EMAIL_INPUT).send_keys(user_email_in_db)
        driver.find_element(*TestLocators.LOGIN_PASSWORD_INPUT).send_keys(user_pass_in_db)
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.HEADER_MAIN_PAGE))
        header_text3 = driver.find_element(*TestLocators.HEADER_MAIN_PAGE).text
        assert 'Соберите бургер' in header_text3, f'Заголовок "{header_text3}" не совпадает'

    def test_login_by_reset_password_true(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/forgot-password")

        driver.find_element(*TestLocators.RESET_PASS_LOGIN).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.LOGIN_HEADER))
        driver.find_element(*TestLocators.LOGIN_EMAIL_INPUT).send_keys(user_email_in_db)
        driver.find_element(*TestLocators.LOGIN_PASSWORD_INPUT).send_keys(user_pass_in_db)
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.HEADER_MAIN_PAGE))
        header_text4 = driver.find_element(*TestLocators.HEADER_MAIN_PAGE).text
        assert 'Соберите бургер' in header_text4, f'Заголовок "{header_text4}" не совпадает'
