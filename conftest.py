import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope="function")
def driver():
    service=Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()

    driver = webdriver.Chrome(service=service,options=options)
    driver.maximize_window()
    driver.implicitly_wait(5)           # Tweak as needed
    yield driver
    driver.quit()
