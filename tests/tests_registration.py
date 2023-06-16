from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from test_locators import TestLocators


class TestRegistration:

    def test_registration_true(self, driver, random_email_password):
        driver.get("https://stellarburgers.nomoreparties.site/register")

        driver.find_element(*TestLocators.REG_NAME_INPUT).send_keys('Nat')
        driver.find_element(*TestLocators.REG_EMAIL_INPUT).send_keys(random_email_password[1])
        driver.find_element(*TestLocators.REG_PASSWORD_INPUT).send_keys(random_email_password[0])
        driver.find_element(*TestLocators.REGISTER_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.LOGIN_HEADER))
        assert '/login' in driver.current_url, f'Не совпадает с текущим URL - "{driver.current_url}"'

    def test_registration_wrong_password_shows_error(self, driver, random_email_password):
        driver.get("https://stellarburgers.nomoreparties.site/register")

        driver.find_element(*TestLocators.REG_NAME_INPUT).send_keys('Nat')
        driver.find_element(*TestLocators.REG_EMAIL_INPUT).send_keys(random_email_password[1])
        driver.find_element(*TestLocators.REG_PASSWORD_INPUT).send_keys('555')
        driver.find_element(*TestLocators.REGISTER_BUTTON).click()
        error_text = driver.find_element(*TestLocators.REG_PASSWORD_ERROR).text
        assert 'Некорректный пароль' in error_text, f'Error_text "{error_text}" не совпадает'
