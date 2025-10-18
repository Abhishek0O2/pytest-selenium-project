from selenium.webdriver.common.by import By
from pages.main_comlex_elemnts import MainComplexElemts

def test_select_dropdown_link(driver):
    driver.get("https://selectorshub.com/xpath-practice-page/")
    page = MainComplexElemts(driver)
    assert page.open_dropdown_and_select("SHub Youtube Channel")


def test_select_car_option(driver):
    driver.get("https://selectorshub.com/xpath-practice-page/")
    page = MainComplexElemts(driver)
    assert page.select_car("volvo")
    assert page.select_car("audi")

def test_date_picker(driver):
    driver.get("https://selectorshub.com/xpath-practice-page/")
    page = MainComplexElemts(driver)
    assert page.set_custom_date("2025-12-31")
