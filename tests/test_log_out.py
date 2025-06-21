from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import Locators

def test_log_out_successful(driver, log_in):

    driver.find_element(*Locators.PERSONAL_ACCOUNT_BTN).click()

    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(Locators.ACCOUNT_LOGOUT_BTN)
    ).click()

    WebDriverWait(driver, 5).until(
        EC.url_to_be("https://stellarburgers.nomoreparties.site/login")
    )

    assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"