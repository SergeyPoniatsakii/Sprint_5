from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import Locators

def test_login_from_main_successful(driver, main_page_url, user):
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

    assert driver.current_url == "https://stellarburgers.nomoreparties.site/"

def test_login_from_personal_account_successful(driver, account_page_url, user):
    driver.get(account_page_url)
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

    assert driver.current_url == "https://stellarburgers.nomoreparties.site/"

def test_login_from_registration_successful(driver, register_page_url, user):
    driver.get(register_page_url)
    email, password = user

    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(Locators.LOGIN_LOGIN_BTN)
    ).click()

    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(Locators.LOGIN_EMAIL_FLD)
    ).send_keys(email)

    driver.find_element(*Locators.LOGIN_PASSWORD_FLD).send_keys(password)

    driver.find_element(*Locators.LOGIN_BTN).click()

    WebDriverWait(driver, 5).until(
        EC.url_to_be("https://stellarburgers.nomoreparties.site/")
    )

    assert driver.current_url == "https://stellarburgers.nomoreparties.site/"

def test_login_from_forgot_pwd_successful(driver, forgot_pwd_page_url, user):
    driver.get(forgot_pwd_page_url)
    email, password = user

    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(Locators.FORGOT_LOGIN_BTN)
    ).click()

    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(Locators.LOGIN_EMAIL_FLD)
    ).send_keys(email)

    driver.find_element(*Locators.LOGIN_PASSWORD_FLD).send_keys(password)

    driver.find_element(*Locators.LOGIN_BTN).click()

    WebDriverWait(driver, 5).until(
        EC.url_to_be("https://stellarburgers.nomoreparties.site/")
    )

    assert driver.current_url == "https://stellarburgers.nomoreparties.site/"

