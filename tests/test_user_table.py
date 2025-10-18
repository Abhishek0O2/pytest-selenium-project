from selenium.webdriver.common.by import By
from pages.main_table import MainTable
from selenium.webdriver.support.ui import WebDriverWait

def test_table_user_admin(driver):
    driver.get("https://selectorshub.com/xpath-practice-page/")
    page = MainTable(driver)

    # List comprehension to assert all usernames
    usernames = page.get_column_values(2)
    assert "John.Smith" in usernames

    # User role is col_idx = 3
    idx_role = 3
    idx_username = 2
    rows = page.get_table_rows()
    roles = [row.find_elements(By.TAG_NAME, "td")[idx_role - 1].text for row in rows]
    smith_idx = usernames.index("John.Smith")
    assert roles[smith_idx] == "Admin"