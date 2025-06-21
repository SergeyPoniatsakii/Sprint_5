from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import Locators

def test_new_user_registration_successful(driver, main_page_url, rnd_user):
    driver.get(main_page_url)

    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(Locators.PERSONAL_ACCOUNT_BTN)
    ).click()

    WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable(Locators.LOGIN_REGISTRATION_BTN)
    ).click()

    test_user = rnd_user

    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(Locators.REGISTRATION_NAME_FLD)
    ).send_keys(test_user)

    driver.find_element(*Locators.REGISTRATION_EMAIL_FLD).send_keys(test_user)

    driver.find_element(*Locators.REGISTRATION_PASSWORD_FLD).send_keys(test_user)

    # Нажимаем на кнопку "Зарегистрироваться"
    driver.find_element(*Locators.REGISTRATION_SUBMIT_BTN).click()

    WebDriverWait(driver, 5).until(
        EC.url_to_be("https://stellarburgers.nomoreparties.site/login")
    )
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"

    driver.quit()

def test_new_user_registration_invalid_pwd (driver, register_page_url, rnd_user):
    driver.get(register_page_url)

    test_user = rnd_user

    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(Locators.REGISTRATION_NAME_FLD)
    ).send_keys(test_user)

    driver.find_element(*Locators.REGISTRATION_EMAIL_FLD).send_keys(test_user)

    driver.find_element(*Locators.REGISTRATION_PASSWORD_FLD).send_keys('short')

    driver.find_element(*Locators.REGISTRATION_SUBMIT_BTN).click()

    assert driver.find_element(*Locators.UNFORMATTED_PWD).is_displayed()
    driver.quit()

def test_new_user_registration_empty_name (driver, register_page_url, rnd_user):
    driver.get(register_page_url)

    test_user = rnd_user

    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(Locators.REGISTRATION_NAME_FLD)
    ).send_keys('')

    driver.find_element(*Locators.REGISTRATION_EMAIL_FLD).send_keys(test_user)

    driver.find_element(*Locators.REGISTRATION_PASSWORD_FLD).send_keys(test_user)

    driver.find_element(*Locators.REGISTRATION_SUBMIT_BTN).click()

    assert driver.current_url == "https://stellarburgers.nomoreparties.site/register"

def test_new_user_registration_email_unformatted (driver, register_page_url, rnd_user):
    driver.get(register_page_url)

    test_user = rnd_user

    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(Locators.REGISTRATION_NAME_FLD)
    ).send_keys(test_user)

    driver.find_element(*Locators.REGISTRATION_EMAIL_FLD).send_keys(test_user.replace("@", "", 1))

    driver.find_element(*Locators.REGISTRATION_PASSWORD_FLD).send_keys(test_user)

    driver.find_element(*Locators.REGISTRATION_SUBMIT_BTN).click()

    assert driver.current_url == "https://stellarburgers.nomoreparties.site/register"