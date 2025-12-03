from selenium.webdriver.common.by import By
from base.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.username_field = (By.XPATH, "//input[@id = 'user-name']")
        self.password_field = (By.XPATH, "//input[@id = 'password']")
        self.login_btn = (By.XPATH, "//input[@id = 'login-button']")

    def login(self, username, password):
        self.type(self.username_field, username)
        self.type(self.password_field, password)
        self.get_element(self.login_btn).click()
     


