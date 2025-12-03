from base.base_test import BaseTest
from utils.config_reader import ConfigReader

class TestCheckout(BaseTest):
    def test_checkout(self, login_page, inventory_page, cart_page, checkout_page):
        login_page.login(ConfigReader.get_username(), ConfigReader.get_password())
        assert "inventory" in self.driver.current_url, "Login failed"
        print("Login successfully")

        inventory_page.add_to_cart()
        cart_count = inventory_page.get_cart_count()
        assert cart_count == 3, f"Expected 3 items but get {cart_count}"
        print(f"Cart count is correct: {cart_count}")
        inventory_page.click_shopping_cart()
        assert 'cart' in self.driver.current_url, "Failed to navigate to Cart page"
        print("Successfully navigated to Cart page")

        cart_page.click_checkout_btn()
        assert "checkout-step-one" in self.driver.current_url, "Failed to navigate to Checkout page"
        print("Successfully navigated to Checkout page")

        checkout_page.checkout(ConfigReader.get_firstname(), ConfigReader.get_lastname(), ConfigReader.get_zipcode())
        assert checkout_page.verify_checkout() is True, "Checkout failed"
        print("Checkout successfully")





    