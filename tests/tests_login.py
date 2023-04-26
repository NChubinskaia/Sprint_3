import pytest

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from test_locators import TestLocators


@pytest.mark.usefixtures("get_driver", "create_user")
class TestLogin:

    def test_login_by_enter_to_account_button_true(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/")

        self.driver.find_element(*TestLocators.SIGN_IN_BUTTON).click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.LOGIN_HEADER))
        self.driver.find_element(*TestLocators.LOGIN_EMAIL_INPUT).send_keys(self.existing_user_email)
        self.driver.find_element(*TestLocators.LOGIN_PASSWORD_INPUT).send_keys(self.existing_user_pass)
        self.driver.find_element(*TestLocators.LOGIN_BUTTON).click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.HEADER_MAIN_PAGE))
        header_text1 = self.driver.find_element(*TestLocators.HEADER_MAIN_PAGE).text
        assert 'Соберите бургер' in header_text1

    def test_login_by_user_account_true(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/")

        self.driver.find_element(*TestLocators.USER_ACCOUNT_BUTTON).click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.LOGIN_HEADER))
        self.driver.find_element(*TestLocators.LOGIN_EMAIL_INPUT).send_keys(self.existing_user_email)
        self.driver.find_element(*TestLocators.LOGIN_PASSWORD_INPUT).send_keys(self.existing_user_pass)
        self.driver.find_element(*TestLocators.LOGIN_BUTTON).click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.HEADER_MAIN_PAGE))
        header_text2 = self.driver.find_element(*TestLocators.HEADER_MAIN_PAGE).text
        assert 'Соберите бургер' in header_text2

    def test_login_by_registration_form_true(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/register")

        self.driver.find_element(*TestLocators.REG_LOGIN).click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.LOGIN_HEADER))
        self.driver.find_element(*TestLocators.LOGIN_EMAIL_INPUT).send_keys(self.existing_user_email)
        self.driver.find_element(*TestLocators.LOGIN_PASSWORD_INPUT).send_keys(self.existing_user_pass)
        self.driver.find_element(*TestLocators.LOGIN_BUTTON).click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.HEADER_MAIN_PAGE))
        header_text3 = self.driver.find_element(*TestLocators.HEADER_MAIN_PAGE).text
        assert 'Соберите бургер' in header_text3

    def test_login_by_reset_password_true(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/forgot-password")

        self.driver.find_element(*TestLocators.RESET_PASS_LOGIN).click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.LOGIN_HEADER))
        self.driver.find_element(*TestLocators.LOGIN_EMAIL_INPUT).send_keys(self.existing_user_email)
        self.driver.find_element(*TestLocators.LOGIN_PASSWORD_INPUT).send_keys(self.existing_user_pass)
        self.driver.find_element(*TestLocators.LOGIN_BUTTON).click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.HEADER_MAIN_PAGE))
        header_text3 = self.driver.find_element(*TestLocators.HEADER_MAIN_PAGE).text
        assert 'Соберите бургер' in header_text3
