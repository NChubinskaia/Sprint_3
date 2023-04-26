import pytest

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from test_locators import TestLocators


@pytest.mark.usefixtures("random_email_password", "get_driver")
class TestRegistration:

    def test_registration_true(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/register")

        self.driver.find_element(*TestLocators.REG_NAME_INPUT).send_keys('Nat')
        self.driver.find_element(*TestLocators.REG_EMAIL_INPUT).send_keys(self.user_email)
        self.driver.find_element(*TestLocators.REG_PASSWORD_INPUT).send_keys(self.user_password)
        self.driver.find_element(*TestLocators.REGISTER_BUTTON).click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.LOGIN_HEADER))
        assert '/login' in self.driver.current_url

    def test_registration_wrong_password_shows_error(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/register")

        self.driver.find_element(*TestLocators.REG_NAME_INPUT).send_keys('Nat')
        self.driver.find_element(*TestLocators.REG_EMAIL_INPUT).send_keys(self.user_email)
        self.driver.find_element(*TestLocators.REG_PASSWORD_INPUT).send_keys('555')
        self.driver.find_element(*TestLocators.REGISTER_BUTTON).click()
        error_text = self.driver.find_element(*TestLocators.REG_PASSWORD_ERROR).text
        assert 'Некорректный пароль' in error_text
