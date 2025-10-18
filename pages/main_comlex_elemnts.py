import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

class MainComplexElemts:
    # SVG & Inputs
    SVG_ICON = (By.CSS_SELECTOR, "svg[iconid='editon']")
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, "input.nameFld[placeholder='First Enter name']")

    # Dropdowns (custom and select tag)
    DROPDOWN_BTN = (By.XPATH, "//button[normalize-space(text())='Checkout here']")
    DROPDOWN_CONTENT = (By.CSS_SELECTOR, ".dropdown-content")
    DROPDOWN_LINKS = (By.CSS_SELECTOR, ".dropdown-content a")
    CAR_SELECT = (By.ID, "cars")

    # Date pickers
    PICK_DATE_INPUT = (By.ID, "datepicker")
    DATE_INPUT = (By.CSS_SELECTOR, "input[type='date'][name='the_date']")

    # File upload
    FILE_INPUT = (By.ID, "myFile")

    # JS Alert/Prompt buttons
    ALERT_BTN = (By.XPATH, "//button[contains(text(),'Click To Open Window Alert')]")
    PROMPT_BTN = (By.XPATH, "//button[contains(text(),'Click To Open Window Prompt Alert')]")

    # Canvas
    CANVAS = (By.ID, "canpro")

    def __init__(self, driver):
        self.driver = driver

    # SVG action
    def enable_name_input(self):
        svg = self.driver.find_element(*self.SVG_ICON)
        # By using *self Python unpacks the tuple into individual arguments: driver.find_element(By.CSS_SELECTOR, "svg[iconid='editon']")
        self.driver.execute_script("""
            var event = new MouseEvent('click', {
                view: window,
                bubbles: true,
                cancelable: true
            });
            arguments[0].dispatchEvent(event);
        """, svg)
        # What it does:
        # SVG stands for Scalable Vector Graphics.
        # We use execute script to create new mouse_event and then dispatch_event
        # Creates an artificial MouseEvent of type "click".        #
        # Sets event properties: view: window (context), bubbles: true (the event bubbles up the DOM), cancelable: true (can be cancelled by handlers).        #
        # Dispatches (fires) that event directly onto your SVG DOM node, as if a real mouse click happened—but bypasses any visual/physical UI restrictions.        #
        # Why it works for SVG:        #
        # Any element in the DOM (HTML, SVG, MathML, etc.) can receive events via dispatchEvent().        #
        # This doesn’t care if the element is visible, covered, or “natively clickable.”        #
        # Any JS code or event handler bound to that SVG’s click event fires as if a real click occurred—so if clicking the SVG enables the input, this will always work, even if the browser’s mouse simulation would fail.

        input_elem = self.driver.find_element(*self.FIRST_NAME_INPUT)
        return input_elem.is_enabled()

    # Dropdown Useful Links for learning
    # Checkout here
    # first aproach
    # def open_dropdown_and_select(self, link_text):
    #     elem = self.driver.find_element(*self.DROPDOWN_BTN)
    #     self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", elem)
    #     try:
    #         WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.DROPDOWN_BTN))
    #           Try physical click
    #         elem.click()
    #     except Exception:
    #           Try javascript click
    #         self.driver.execute_script("arguments[0].click();", elem)
    #     WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.DROPDOWN_CONTENT))
    #     links = self.driver.find_elements(*self.DROPDOWN_LINKS)
    #     for link in links:
    #         if link.text.strip() == link_text:
    #             link.click()
    #             return True
    #     return False
    # aproach 2 trying to hover using Action chain but did no twork
    def open_dropdown_and_select(self, link_text):
        container = self.driver.find_element(By.CSS_SELECTOR, "div.dropdown")

        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", container)
        ActionChains(self.driver).move_to_element(container).perform()
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".dropdown-content"))
        )
        items = self.driver.find_elements(By.CSS_SELECTOR, ".dropdown-content a")
        for a in items:
            if a.text.strip() == link_text:
                a.click()
                return True
        return False

    # Select tag (cars)
    def select_car(self, car_value):
        select = Select(self.driver.find_element(*self.CAR_SELECT))
        select.select_by_value(car_value)
        selected = select.first_selected_option.get_attribute("value")

        return selected == car_value

    # Date picker
    def set_custom_date(self, date_str):
        self.driver.find_element(*self.PICK_DATE_INPUT).clear()
        self.driver.find_element(*self.PICK_DATE_INPUT).send_keys(date_str)
        return self.driver.find_element(*self.PICK_DATE_INPUT).get_attribute("value") == date_str

    # File input
    def upload_file(self, filepath):
        self.driver.find_element(*self.FILE_INPUT).send_keys(filepath)
        return True

    def _robust_click(self, locator):
        elem = self.driver.find_element(*locator)
        # 1) Scroll into view
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", elem)
        # Why it works: calling a JS function from Python (execute_script), The element becomes visible and not hidden by the viewport top/bottom (less chance a sticky header covers it
        # 2) Try native click
        try:
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(locator))
            elem.click()
        #     Python concept: then using an explicit wait (a higher-order function that keeps polling until a condition returns True).
        except Exception:
            # 3) Fallback to JS click if intercepted
            self.driver.execute_script("arguments[0].click();", elem)

    def trigger_alert(self):
        self._robust_click(self.ALERT_BTN)
        alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        text = alert.text
        alert.accept()
        return text

    def trigger_prompt(self, prompt_text="Yes!"):
        self._robust_click(self.PROMPT_BTN)
        alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        alert.send_keys(prompt_text)
        alert.accept()
        # Some prompts don’t show a second alert; just return prompt text for logging
        return prompt_text

    # Canvas
    def get_canvas_size(self):
        canvas = self.driver.find_element(*self.CANVAS)
        width = canvas.get_attribute("width")
        height = canvas.get_attribute("height")
        return width, height




