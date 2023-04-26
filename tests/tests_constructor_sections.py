import pytest

from selenium.webdriver.common.by import By
from test_locators import TestLocators


@pytest.mark.usefixtures("get_driver")
class TestConstructorSections:

    def test_constructor_section_with_buns_true(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/")

        self.driver.find_element(By.XPATH, TestLocators.sauce_section).click()
        self.driver.find_element(By.XPATH, TestLocators.buns_section).click()
        text_buns = self.driver.find_element(By.XPATH, TestLocators.buns_header).text
        assert 'Булки' == text_buns

    def test_constructor_section_with_sauces_true(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/")

        self.driver.find_element(By.XPATH, TestLocators.sauce_section).click()
        text_sauces = self.driver.find_element(By.XPATH, TestLocators.sauce_header).text
        assert 'Соусы' == text_sauces

    def test_constructor_section_with_fillings_true(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/")

        self.driver.find_element(By.XPATH, TestLocators.filling_section).click()
        text_fillings = self.driver.find_element(By.XPATH, TestLocators.filling_header).text
        assert 'Начинки' == text_fillings
