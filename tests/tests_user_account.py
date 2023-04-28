from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from test_locators import TestLocators

user_email_in_db = 'chubinskaia_9148@gmail.com'
user_pass_in_db = 'sprint3'


class TestUserAccount:

    def test_go_to_user_account_true(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/login")

        driver.find_element(*TestLocators.LOGIN_EMAIL_INPUT).send_keys(user_email_in_db)
        driver.find_element(*TestLocators.LOGIN_PASSWORD_INPUT).send_keys(user_pass_in_db)
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.HEADER_MAIN_PAGE))
        driver.find_element(*TestLocators.USER_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.PROFILE_LINK))
        user_name = driver.find_element(*TestLocators.PROFILE_NAME_INPUT).get_attribute('value')
        user_email = driver.find_element(*TestLocators.PROFILE_EMAIL_INPUT).get_attribute('value')
        assert '/profile' in driver.current_url and user_name == 'Nat' and user_email == user_email_in_db
