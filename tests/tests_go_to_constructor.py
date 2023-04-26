import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from test_locators import TestLocators


@pytest.mark.usefixtures("get_driver", "create_user")
class TestConstructor:

    def test_go_to_constructor_by_button_constructor_true(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/login")

        self.driver.find_element(By.XPATH, TestLocators.login_email_input).send_keys(self.existing_user_email)
        self.driver.find_element(By.XPATH, TestLocators.login_password_input).send_keys(self.existing_user_pass)
        self.driver.find_element(By.XPATH, TestLocators.login_button).click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, TestLocators.header_main_page)))
        self.driver.find_element(By.XPATH, TestLocators.user_account_button).click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, TestLocators.profile_save_button)))
        self.driver.find_element(By.XPATH, TestLocators.constructor_button).click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, TestLocators.header_main_page)))
        header_text1 = self.driver.find_element(By.XPATH, TestLocators.header_main_page).text
        assert 'Соберите бургер' in header_text1

    def test_go_to_constructor_by_logo_true(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/login")

        self.driver.find_element(By.XPATH, TestLocators.login_email_input).send_keys(self.existing_user_email)
        self.driver.find_element(By.XPATH, TestLocators.login_password_input).send_keys(self.existing_user_pass)
        self.driver.find_element(By.XPATH, TestLocators.login_button).click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, TestLocators.header_main_page)))
        self.driver.find_element(By.XPATH, TestLocators.user_account_button).click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, TestLocators.profile_save_button)))
        self.driver.find_element(By.XPATH, TestLocators.logo).click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, TestLocators.header_main_page)))
        header_text2 = self.driver.find_element(By.XPATH, TestLocators.header_main_page).text
        assert 'Соберите бургер' in header_text2
