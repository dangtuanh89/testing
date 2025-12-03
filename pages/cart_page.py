from base.base_page import BasePage
from selenium.webdriver.common.by import By

class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.checkout_btn = (By.XPATH, "//button[@id = 'checkout']")

    def click_checkout_btn(self):
        self.get_element(self.checkout_btn).click()