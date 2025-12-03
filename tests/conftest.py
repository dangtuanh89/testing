from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
import pytest

@pytest.fixture(scope= 'class')
def login_page(request):
    login_page = LoginPage(request.cls.driver)
    return login_page

@pytest.fixture(scope= 'class')
def inventory_page(request):
    inventory_page = InventoryPage(request.cls.driver)
    return inventory_page

@pytest.fixture(scope= 'class')
def cart_page(request):
    cart_page = CartPage(request.cls.driver)
    return cart_page

@pytest.fixture(scope= 'class')
def checkout_page(request):
    checkout_page = CheckoutPage(request.cls.driver)
    return checkout_page
 