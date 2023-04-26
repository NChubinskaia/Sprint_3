import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from test_locators import TestLocators


@pytest.mark.usefixtures("get_driver", "create_user")
class TestExitFromAccount:

    def test_exit_from_user_account_true(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/login")

        self.driver.find_element(By.XPATH, TestLocators.login_email_input).send_keys(self.existing_user_email)
        self.driver.find_element(By.XPATH, TestLocators.login_password_input).send_keys(self.existing_user_pass)
        self.driver.find_element(By.XPATH, TestLocators.login_button).click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, TestLocators.header_main_page)))
        self.driver.find_element(By.XPATH, TestLocators.user_account_button).click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, TestLocators.profile_save_button)))
        self.driver.find_element(By.XPATH, TestLocators.profile_quit_button).click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, TestLocators.login_header)))
        assert '/login' in self.driver.current_url
