from pages.main_page import MainPage
from selenium.webdriver.support.ui import WebDriverWait

def test_open_modal_button_and_assert_text(driver):
    driver.get("https://selectorshub.com/xpath-practice-page/")

# Open the modal robustly
    page_obj=MainPage(driver)
    page_obj.open_modal()
    link=page_obj.get_testing_daily_link()

    # Store all window handles before click
    windows_before = set(driver.window_handles)

    # Click link (opens new tab)
    link.click()

    # Wait for a new window handle to appear
    WebDriverWait(driver, 10).until(
        lambda d: len(set(d.window_handles) - windows_before) == 1
    )
    new_window = next(iter(set(driver.window_handles) - windows_before))
    driver.switch_to.window(new_window)

    # Assert URL (or title/content of new page as desired)
    assert "testing-daily" in driver.current_url.lower()

    # Optional: close the new tab and return to original
    driver.close()
    driver.switch_to.window(next(iter(windows_before)))