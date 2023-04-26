import pytest

from test_locators import TestLocators


@pytest.mark.usefixtures("get_driver")
class TestConstructorSections:

    def test_constructor_section_with_buns_true(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/")

        self.driver.find_element(*TestLocators.SAUCE_SECTION).click()
        self.driver.find_element(*TestLocators.BUNS_SECTION).click()
        text_buns = self.driver.find_element(*TestLocators.BUNS_HEADER).text
        assert 'Булки' == text_buns

    def test_constructor_section_with_sauces_true(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/")

        self.driver.find_element(*TestLocators.SAUCE_SECTION).click()
        text_sauces = self.driver.find_element(*TestLocators.SAUCE_HEADER).text
        assert 'Соусы' == text_sauces

    def test_constructor_section_with_fillings_true(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/")

        self.driver.find_element(*TestLocators.FILLING_SECTION).click()
        text_fillings = self.driver.find_element(*TestLocators.FILLING_HEADER).text
        assert 'Начинки' == text_fillings
