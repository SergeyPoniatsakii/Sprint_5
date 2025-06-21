import random
import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import Locators

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture()
def main_page_url():
    return "https://stellarburgers.nomoreparties.site/"

@pytest.fixture()
def register_page_url():
    return "https://stellarburgers.nomoreparties.site/register"

@pytest.fixture()
def login_page_url():
    return "https://stellarburgers.nomoreparties.site/login"

@pytest.fixture()
def account_page_url():
    return "https://stellarburgers.nomoreparties.site/account"

@pytest.fixture()
def forgot_pwd_page_url():
    return "https://stellarburgers.nomoreparties.site/forgot-password"

@pytest.fixture()
def user():
    email = 'SergeiPoniatskii_2425@ya.ru'
    password = 'strongpwd'
    return email, password

@pytest.fixture()
def rnd_user():
    new_user = f"Бургер{random.randint(100, 999)}@ya{random.randint(100, 999)}.ru"
    return new_user

@pytest.fixture()
def log_in(request, driver, user, main_page_url):
    driver.get(main_page_url)
    email, password = user

    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(Locators.LOGIN_ACC_BTN)
    ).click()

    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(Locators.LOGIN_EMAIL_FLD)
    ).send_keys(email)

    driver.find_element(*Locators.LOGIN_PASSWORD_FLD).send_keys(password)

    driver.find_element(*Locators.LOGIN_BTN).click()

    WebDriverWait(driver, 5).until(
        EC.url_to_be("https://stellarburgers.nomoreparties.site/")
    )