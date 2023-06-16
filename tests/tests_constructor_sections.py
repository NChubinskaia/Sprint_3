from test_locators import TestLocators


class TestConstructorSections:

    def test_constructor_section_with_buns_true(self, driver):

        driver.find_element(*TestLocators.SAUCE_SECTION).click()
        driver.find_element(*TestLocators.BUNS_SECTION).click()
        text_buns = driver.find_element(*TestLocators.BUNS_HEADER).text
        assert 'Булки' == text_buns, f'Заголовок не совпадает! В переменной text_buns - "{text_buns}"'

    def test_constructor_section_with_sauces_true(self, driver):

        driver.find_element(*TestLocators.SAUCE_SECTION).click()
        text_sauces = driver.find_element(*TestLocators.SAUCE_HEADER).text
        assert 'Соусы' == text_sauces, f'Заголовок не совпадает! В переменной text_sauces - "{text_sauces}"'

    def test_constructor_section_with_fillings_true(self, driver):

        driver.find_element(*TestLocators.FILLING_SECTION).click()
        text_fillings = driver.find_element(*TestLocators.FILLING_HEADER).text
        assert 'Начинки' == text_fillings, f'Заголовок не совпадает! В переменной text_fillings - "{text_fillings}"'
