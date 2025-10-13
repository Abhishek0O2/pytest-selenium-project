from pages.main_page import MainPage

def test_open_xpath_practice_page(driver):
    driver.get("https://selectorshub.com/xpath-practice-page/")
    page= MainPage(driver)
    heading = page.get_heading_text()
    print(f"Extracted heading: '{heading}'")
    assert "Find Out How To Automate " in heading
