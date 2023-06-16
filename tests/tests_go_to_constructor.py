from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from test_locators import TestLocators

user_email_in_db = 'chubinskaia_9148@gmail.com'
user_pass_in_db = 'sprint3'


class TestConstructor:

    def test_go_to_constructor_by_button_constructor_true(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/login")

        driver.find_element(*TestLocators.LOGIN_EMAIL_INPUT).send_keys(user_email_in_db)
        driver.find_element(*TestLocators.LOGIN_PASSWORD_INPUT).send_keys(user_pass_in_db)
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.HEADER_MAIN_PAGE))
        driver.find_element(*TestLocators.USER_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.PROFILE_LINK))
        driver.find_element(*TestLocators.CONSTRUCTOR_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.HEADER_MAIN_PAGE))
        header_text1 = driver.find_element(*TestLocators.HEADER_MAIN_PAGE).text
        assert 'Соберите бургер' in header_text1, f'Заголовок "{header_text1}" не совпадает'

    def test_go_to_constructor_by_logo_true(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/login")

        driver.find_element(*TestLocators.LOGIN_EMAIL_INPUT).send_keys(user_email_in_db)
        driver.find_element(*TestLocators.LOGIN_PASSWORD_INPUT).send_keys(user_pass_in_db)
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.HEADER_MAIN_PAGE))
        driver.find_element(*TestLocators.USER_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.PROFILE_LINK))
        driver.find_element(*TestLocators.LOGO).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.HEADER_MAIN_PAGE))
        header_text2 = driver.find_element(*TestLocators.HEADER_MAIN_PAGE).text
        assert 'Соберите бургер' in header_text2, f'Заголовок "{header_text2}" не совпадает'
