

import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from test_locators import TestLocators


@pytest.mark.usefixtures("get_driver", "create_user")
class TestUserAccount:

    def test_go_to_user_account_true(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/login")

        self.driver.find_element(By.XPATH, TestLocators.login_email_input).send_keys(self.existing_user_email)
        self.driver.find_element(By.XPATH, TestLocators.login_password_input).send_keys(self.existing_user_pass)
        self.driver.find_element(By.XPATH, TestLocators.login_button).click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, TestLocators.header_main_page)))
        self.driver.find_element(By.XPATH, TestLocators.user_account_button).click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, TestLocators.profile_save_button)))
        user_name = self.driver.find_element(By.XPATH, TestLocators.profile_name_input).get_attribute('value')
        user_email = self.driver.find_element(By.XPATH, TestLocators.profile_email_input).get_attribute('value')
        test_email = self.existing_user_email
        assert '/profile' in self.driver.current_url and user_name == 'Nat' and user_email == test_email
