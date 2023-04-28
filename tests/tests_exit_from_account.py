from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from test_locators import TestLocators

user_email_in_db = 'chubinskaia_9148@gmail.com'
user_pass_in_db = 'sprint3'


class TestExitFromAccount:

    def test_exit_from_user_account_true(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/login")

        driver.find_element(*TestLocators.LOGIN_EMAIL_INPUT).send_keys(user_email_in_db)
        driver.find_element(*TestLocators.LOGIN_PASSWORD_INPUT).send_keys(user_pass_in_db)
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.HEADER_MAIN_PAGE))
        driver.find_element(*TestLocators.USER_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.PROFILE_LINK))
        driver.find_element(*TestLocators.PROFILE_QUIT_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.LOGIN_HEADER))
        assert '/login' in driver.current_url, f'Не совпадает с текущим URL - "{driver.current_url}"'
