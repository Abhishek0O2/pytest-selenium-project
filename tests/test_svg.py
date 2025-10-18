from selenium.webdriver.common.by import By
from pages.main_comlex_elemnts import MainComplexElemts

def test_svg_enables_name_input(driver):
    driver.get("https://selectorshub.com/xpath-practice-page/")
    page = MainComplexElemts(driver)
    assert not page.driver.find_element(*page.FIRST_NAME_INPUT).is_enabled()
    assert page.enable_name_input()

# What is SVG?
# SVG stands for Scalable Vector Graphics.
#
# It’s an XML-based markup for describing two-dimensional graphics, shapes, and icons on web pages.
#
# Examples: icons, logos, graphs, custom buttons—all often rendered as <svg> elements with <path>, <rect>, <circle>, etc. SVGs are NOT traditional HTML elements like <button> or <div>.
#
# SVGs are part of the DOM and can respond to JavaScript events (click, hover), but they don’t always behave exactly like regular HTML elements in the browser’s event system.

# SVGs may:# Have “no clickable area” from the browser’s perspective.
# Be visually covered, not visually at those coordinates.
# Lack a .click() method (it might not be a standard function for certain SVG DOM nodes).
# You will get  ElementClickInterceptedException or JS “not a function”–because:
# Either something was visually overlayed, or The element didn’t implement .click() as a method.


