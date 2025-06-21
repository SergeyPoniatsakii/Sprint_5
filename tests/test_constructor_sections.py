from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import Locators

def test_goto_bake_successful(driver, main_page_url):
    driver.get(main_page_url)

    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(Locators.CONSTRUCTOR_SOUS_BTN)
    ).click()

    driver.find_element(*Locators.CONSTRUCTOR_BAKE_BTN).click()

    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(Locators.R2_D2)
    )
    assert driver.find_element(*Locators.CONSTRUCTOR_BAKE_BTN_ACT).is_displayed()

def test_goto_sous_successful(driver, main_page_url):
    driver.get(main_page_url)

    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(Locators.CONSTRUCTOR_SOUS_BTN)
    ).click()

    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(Locators.SPICY_X)
    )
    assert driver.find_element(*Locators.CONSTRUCTOR_SOUS_BTN_ACT).is_displayed()

def test_goto_toppings_successful(driver, main_page_url):
    driver.get(main_page_url)

    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(Locators.CONSTRUCTOR_TOPPINGS_BTN)
    ).click()

    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(Locators.PROTOSTOMIA)
    )
    assert driver.find_element(*Locators.CONSTRUCTOR_TOPPINGS_BTN_ACT).is_displayed()
