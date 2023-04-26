import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from test_locators import TestLocators


@pytest.mark.usefixtures("random_email_password", "get_driver")
class TestRegistration:

    def test_registration_true(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/register")

        self.driver.find_element(By.XPATH, TestLocators.register_name_input).send_keys('Nat')
        self.driver.find_element(By.XPATH, TestLocators.register_email_input).send_keys(self.user_email)
        self.driver.find_element(By.XPATH, TestLocators.register_password_input).send_keys(self.user_password)
        self.driver.find_element(By.XPATH, TestLocators.register_button).click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, TestLocators.login_header)))
        assert '/login' in self.driver.current_url

    def test_registration_wrong_password_shows_error(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/register")

        self.driver.find_element(By.XPATH, TestLocators.register_name_input).send_keys('Nat')
        self.driver.find_element(By.XPATH, TestLocators.register_email_input).send_keys(self.user_email)
        self.driver.find_element(By.XPATH, TestLocators.register_password_input).send_keys('555')
        self.driver.find_element(By.XPATH, TestLocators.register_button).click()
        error_text = self.driver.find_element(By.CSS_SELECTOR, TestLocators.register_password_error).text
        assert 'Некорректный пароль' in error_text
