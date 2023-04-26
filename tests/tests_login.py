import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from test_locators import TestLocators


@pytest.mark.usefixtures("get_driver", "create_user")
class TestLogin:

    def test_login_by_enter_to_account_button_true(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/")

        self.driver.find_element(By.XPATH, TestLocators.sign_in_button).click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, TestLocators.login_header)))
        self.driver.find_element(By.XPATH, TestLocators.login_email_input).send_keys(self.existing_user_email)
        self.driver.find_element(By.XPATH, TestLocators.login_password_input).send_keys(self.existing_user_pass)
        self.driver.find_element(By.XPATH, TestLocators.login_button).click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, TestLocators.header_main_page)))
        header_text1 = self.driver.find_element(By.XPATH, TestLocators.header_main_page).text
        assert 'Соберите бургер' in header_text1

    def test_login_by_user_account_true(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/")

        self.driver.find_element(By.XPATH, TestLocators.user_account_button).click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, TestLocators.login_header)))
        self.driver.find_element(By.XPATH, TestLocators.login_email_input).send_keys(self.existing_user_email)
        self.driver.find_element(By.XPATH, TestLocators.login_password_input).send_keys(self.existing_user_pass)
        self.driver.find_element(By.XPATH, TestLocators.login_button).click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, TestLocators.header_main_page)))
        header_text2 = self.driver.find_element(By.XPATH, TestLocators.header_main_page).text
        assert 'Соберите бургер' in header_text2

    def test_login_by_registration_form_true(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/register")

        self.driver.find_element(By.LINK_TEXT, TestLocators.register_link_login).click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, TestLocators.login_header)))
        self.driver.find_element(By.XPATH, TestLocators.login_email_input).send_keys(self.existing_user_email)
        self.driver.find_element(By.XPATH, TestLocators.login_password_input).send_keys(self.existing_user_pass)
        self.driver.find_element(By.XPATH, TestLocators.login_button).click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH,  TestLocators.header_main_page)))
        header_text3 = self.driver.find_element(By.XPATH, TestLocators.header_main_page).text
        assert 'Соберите бургер' in header_text3

    def test_login_by_reset_password_true(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/forgot-password")

        self.driver.find_element(By.LINK_TEXT, TestLocators.reset_pass_link_login).click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, TestLocators.login_header)))
        self.driver.find_element(By.XPATH, TestLocators.login_email_input).send_keys(self.existing_user_email)
        self.driver.find_element(By.XPATH, TestLocators.login_password_input).send_keys(self.existing_user_pass)
        self.driver.find_element(By.XPATH, TestLocators.login_button).click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, TestLocators.header_main_page)))
        header_text3 = self.driver.find_element(By.XPATH, TestLocators.header_main_page).text
        assert 'Соберите бургер' in header_text3
