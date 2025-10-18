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
    # lambda d: …
    # What it is: A lambda is an anonymous (inline) function. It’s just like def, but shorter when the function body is a single expression.
    new_window = next(iter(set(driver.window_handles) - windows_before))
    #  next(iter(...)) # What it is: A way to get the “first” item from an iterator.
    # iter(x) creates an iterator over a container (list, set, dict, etc.).
    driver.switch_to.window(new_window)

    # Assert URL (or title/content of new page as desired)
    assert "testing-daily" in driver.current_url.lower()

    # Optional: close the new tab and return to original
    driver.close()
    driver.switch_to.window(next(iter(windows_before)))

    # Key idea: window handles
    # A window handle is a unique ID (string) for each open browser tab/window that WebDriver can control.
    #
    # driver.window_handles returns a list of all current handles.
    #
    # driver.current_window_handle is the handle of the tab/window you’re currently focused on.
    #
    # To interact with a different tab, you must switch_to.window(<handle>).
    #
    # Line-by-line explanation
    # windows_before = set(driver.window_handles)
    #
    # We take a snapshot of all currently open tabs before clicking the link.
    #
    # Using a set makes it easy to compute differences later.
    #
    # Purpose: so we can detect which new handle appears after the click.
    #
    # link.click()
    #
    # Clicks the link inside the modal.
    #
    # The site behavior (by design) opens a new tab, creating a brand-new window handle.
    #
    # WebDriverWait(driver, 10).until(lambda d: len(set(d.window_handles) - windows_before) == 1)
    #
    # We wait until exactly ONE new handle appears when compared to the snapshot.
    #
    # set(d.window_handles) - windows_before computes the set difference: all handles that are present now but weren’t present before the click.
    #
    # When the new tab is fully registered, the difference will be size 1.
    #
    # This explicit wait makes the test stable against timing/animation delays.
    #
    # new_window = next(iter(set(driver.window_handles) - windows_before))
    #
    # We compute the difference again and extract that single new handle.
    #
    # next(iter(...)) is a safe way to get the only element from the set.
    #
    # Now we know the exact handle of the just-opened tab.
    #
    # driver.switch_to.window(new_window)
    #
    # Switch WebDriver’s context to the new tab using its handle.
    #
    # After this, all driver operations (URL checks, finding elements) happen in the new tab.
    #
    # assert "testing-daily" in driver.current_url.lower()
    #
    # We verify navigation in the new tab by checking the URL.
    #
    # This confirms the click produced the intended result.
    #
    # driver.close()
    #
    # Closes the current tab (the new tab we switched into).
    #
    # Important: this does not quit the whole browser; it only closes the active window.
    #
    # driver.switch_to.window(next(iter(windows_before)))
    #
    # Switch back to one of the original handles from the snapshot (usually the test’s primary tab).
    #
    # This restores your test context so subsequent steps continue on the original page.
    #
    # Why this pattern is robust
    # Works whether the site opens a new tab or sometimes delays tab creation.
    #
    # Avoids guessing indexes or sleeping; we detect the tab by handle difference.
    #
    # Makes it explicit which tab to close and which one to return to.