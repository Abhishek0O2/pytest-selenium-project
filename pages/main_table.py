from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainTable(BasePage):
    USER_TABLE=(By.XPATH,"//table[.//th[contains(.,'Username')]]")
    # //table[.//th[contains(.,'Username')]]
    #
    # //table … find any table element in the document (at any depth).
    #
    # [ … ] … a predicate (filter) that keeps only those tables that satisfy the condition inside.
    #
    # .//th … search from the current table (.) for any descendant th elements (header cells).
    #
    # contains(., 'Username') … the th’s text contains the substring “Username”.
    #
    # Together: “Find the table that has a header cell whose text contains ‘Username’.” This is robust when the table doesn’t have a stable ID/class but the visible header is stable.

    def get_table_rows(self):
        # Get all non-header rows (tbody/tr)
        table = self.driver.find_element(*self.USER_TABLE)
        return table.find_elements(By.XPATH, ".//tbody/tr")
    # ".//tbody/tr"
    #
    # .// … search from the current context node (often a table element) for any descendant that matches.
    #
    # tbody/tr … find all tr (rows) inside any tbody elements.
    #
    # If there is no <tbody> in the actual DOM, you could instead use ".//tr[td]" to get data rows (tr that have td cells) regardless of tbody presence.

    def get_all_data(self):
        """
        Returns table rows as list of lists:
        [
          ['Garry.White','ESS','Garry White','Enabled'],
          ...
        ]
        """
        rows = self.get_table_rows()
        return [[td.text for td in row.find_elements(By.TAG_NAME, "td")] for row in rows]

    def get_column_values(self, col_idx):
        # Get all values in specified column index (1-based!)
        rows = self.get_table_rows()
        return [row.find_elements(By.TAG_NAME, "td")[col_idx - 1].text for row in rows]
    # What it produces
    #
    # A list of strings: each item is the text from the col_idx-1 cell in a given table row.
    #
    # If there are N rows, the result list has N strings (one per row).
    #
    # Plain-English logic (what it means)
    #
    # “For every row in rows, find all its <td> cells, select the (col_idx)th one, get its text, and collect those texts into a list.”
    #
    # Python list comprehension structure
    #
    # General form: [ EXPRESSION for VARIABLE in ITERABLE ]
    #
    # In your expression:
    #
    # ITERABLE is rows
    #
    # VARIABLE is row
    #
    # EXPRESSION is row.find_elements(By.TAG_NAME, "td")[col_idx - 1].text


    def find_row_by_username(self, username):
        rows = self.get_table_rows()
        # Return all cell values for the row where Username matches
        for row in rows:
            cells = [td.text for td in row.find_elements(By.TAG_NAME, "td")]
            if cells[0] == username:
                return cells  # [Username, User Role, Employee Name, Status]
        return None
