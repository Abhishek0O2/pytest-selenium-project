from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class MainPage(BasePage):
    HEADING = (By.TAG_NAME,"h2")

    def get_heading_text(self):
        return self.driver.find_element(*self.HEADING).text


