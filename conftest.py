import string

import pytest

from selenium import webdriver
from random import choice


@pytest.fixture
def get_driver(request):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--window-size=1280,720')
    driver = webdriver.Chrome(options=chrome_options)
    request.cls.driver = driver
    yield
    driver.quit()


@pytest.fixture
def random_email_password(request):
    request.cls.user_password = ''.join(choice(string.ascii_lowercase) for i in range(7))
    number = 0
    with open("user_number_for_register", "r") as file:
        for line in file:
            number = int(line)
    request.cls.user_email = 'nchubinskaia9' + str(number) + "@gmail.com"
    number += 1
    with open("user_number_for_register", "w") as file:
        file.write(str(number))


@pytest.fixture
def create_user(request):
    request.cls.existing_user_email = 'chubinskaia_9148@gmail.com'
    request.cls.existing_user_pass = 'sprint3'
