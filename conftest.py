import pytest
import string
from random import choices
from selenium import webdriver


@pytest.fixture
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--window-size=1280,720')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://stellarburgers.nomoreparties.site/")
    yield driver
    driver.quit()


@pytest.fixture
def random_email_password():
    user_password = choices(string.ascii_lowercase, k=7)
    number = 0
    with open("user_number_for_register", "r") as file:
        for line in file:
            number = int(line)
    user_email = 'nchubinskaia9' + str(number) + "@gmail.com"
    number += 1
    with open("user_number_for_register", "w") as file:
        file.write(str(number))
    return user_password, user_email
