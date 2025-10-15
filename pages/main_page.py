from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage(BasePage):
    HEADING = (By.XPATH, "//*[contains(text(), 'how to automate')]")
    MODAL=(By.ID,"myModal")
    OPEN_MODAL_BUTTON = (By.ID, "myBtn")
    TESTING_DAILY_LINK=(By.XPATH,".//div[contains(@class,'modal-header')]//a[contains(.,'Testing Daily')]")

    def get_heading_text(self):
        return self.driver.find_element(*self.HEADING).text

    def open_modal(self):
        btn = self.driver.find_element(*self.OPEN_MODAL_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView(true);",btn)
        self.driver.execute_script("arguments[0].click();",btn)

    def wait_for_modal_visible(self,timeout=10):
        return WebDriverWait(self.driver,timeout).until(EC.visibility_of_element_located(self.MODAL))

    def get_testing_daily_link(self):
        modal= self.wait_for_modal_visible()
        return modal.find_element(*self.TESTING_DAILY_LINK)




