from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import Locators

def test_open_account_successful(driver, log_in):

    driver.find_element(*Locators.PERSONAL_ACCOUNT_BTN).click()

    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(Locators.ACCOUNT_LOGOUT_BTN)
    )

    assert driver.current_url == "https://stellarburgers.nomoreparties.site/account/profile"

def test_click_constructor_successful(driver, log_in):

    driver.find_element(*Locators.PERSONAL_ACCOUNT_BTN).click()

    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(Locators.ACCOUNT_LOGOUT_BTN)
    )

    driver.find_element(*Locators.ACCOUNT_CONSTRUCTOR_BTN).click()

    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(Locators.CONSTRUCTOR_BAKE_BTN)
    )

    assert driver.find_element(*Locators.ASSEMBLE_A_BURGER).is_displayed()


def test_click_logo_successful(driver, log_in):
    driver.find_element(*Locators.PERSONAL_ACCOUNT_BTN).click()

    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(Locators.ACCOUNT_LOGOUT_BTN)
    )

    driver.find_element(*Locators.ACCOUNT_LOGO_BTN).click()

    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(Locators.CONSTRUCTOR_BAKE_BTN)
    )

    assert driver.find_element(*Locators.ASSEMBLE_A_BURGER).is_displayed()