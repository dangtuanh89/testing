from base.base_page import BasePage
from selenium.webdriver.common.by import By

class CheckoutPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.firstname = (By.XPATH, "//input[@placeholder = 'First Name']")
        self.lastname = (By.XPATH, "//input[@placeholder = 'Last Name']")
        self.zipcode = (By.XPATH, "//input[@placeholder = 'Zip/Postal Code']")
        self.continue_btn = (By.XPATH, "//input[@id = 'continue']")
        self.finish_btn = (By.XPATH, "//button[@id = 'finish']")
        self.thank_you = (By.XPATH, "//h2[text() = 'Thank you for your order!']")
        self.complete_text = (By.XPATH, "//div[contains (text(),  'Your order has been dispatched')]")

    def checkout(self, firstname, lastname, zipcode):
        self.type(self.firstname, firstname)
        self.type(self.lastname, lastname)
        self.type(self.zipcode, zipcode)
        self.get_element(self.continue_btn).click()
        self.get_element(self.finish_btn).click()
    
    def verify_checkout(self):
        return self.get_element(self.thank_you).is_displayed() and self.get_element(self.complete_text).is_displayed()


    


    