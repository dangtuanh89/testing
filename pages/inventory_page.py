from base.base_page import BasePage
from selenium.webdriver.common.by import By

class InventoryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.add_to_cart_btns = [
        (By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']"),
        (By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']"),
        (By.XPATH, "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']")
        ]
        self.shopping_cart = (By.XPATH, "//a[@data-test='shopping-cart-link']")
        self.cart_badge = (By.XPATH, "//span[@class='shopping_cart_badge']")

    def add_to_cart(self):
        for locator in self.add_to_cart_btns:
            self.get_element(locator).click()
        
    def get_cart_count(self):
        return int(self.get_element(self.cart_badge).text)
    
    def click_shopping_cart(self):
        self.get_element(self.shopping_cart).click()
        

    