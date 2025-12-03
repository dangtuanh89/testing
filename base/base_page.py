from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        return element
    
    def get_elements(self, locator):
        elements = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(locator))
        return elements
    
    def type(self, locator, text):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    