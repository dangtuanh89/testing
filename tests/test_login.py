from base.base_test import BaseTest
from pages.login_page import LoginPage
from utils.config_reader import ConfigReader

class TestLogin(BaseTest):
    def test_login(self, login_page):
        login_page.login(ConfigReader.get_username(), ConfigReader.get_password())
        assert "inventory" in self.driver.current_url, "Login failed"
        print("Login successfully")
