import pytest

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from test_locators import TestLocators


@pytest.mark.usefixtures("get_driver", "create_user")
class TestUserAccount:

    def test_go_to_user_account_true(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/login")

        self.driver.find_element(*TestLocators.LOGIN_EMAIL_INPUT).send_keys(self.existing_user_email)
        self.driver.find_element(*TestLocators.LOGIN_PASSWORD_INPUT).send_keys(self.existing_user_pass)
        self.driver.find_element(*TestLocators.LOGIN_BUTTON).click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.HEADER_MAIN_PAGE))
        self.driver.find_element(*TestLocators.USER_ACCOUNT_BUTTON).click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.PROFILE_LINK))
        user_name = self.driver.find_element(*TestLocators.PROFILE_NAME_INPUT).get_attribute('value')
        user_email = self.driver.find_element(*TestLocators.PROFILE_EMAIL_INPUT).get_attribute('value')
        test_email = self.existing_user_email
        assert '/profile' in self.driver.current_url and user_name == 'Nat' and user_email == test_email
