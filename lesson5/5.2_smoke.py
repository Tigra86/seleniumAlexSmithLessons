from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait


class Start_class():
    def select_product(self):
        driver = webdriver.Chrome()
        wait = WebDriverWait(driver, 30, poll_frequency=1)
        base_url = 'https://www.saucedemo.com/'
        driver.get(base_url)
        driver.maximize_window()
        time.sleep(1)

        print("Start test")

        valid_login = "standard_user"
        valid_password = "secret_sauce"
        user_name_field = ("id", "user-name")
        user_password_field = ("id", "password")
        login_button = ("id", "login-button")
        product_1_add_to_cart_locator = ("id", "add-to-cart-sauce-labs-backpack")
        cart_locator = ("id", "shopping_cart_container")
        your_cart_title_locator = ("xpath", "//span[@class='title']")

        time.sleep(3)
        wait.until(EC.element_to_be_clickable(user_name_field)).send_keys(valid_login)
        print("Enter login")
        wait.until(EC.element_to_be_clickable(user_password_field)).send_keys(valid_password)
        print("Enter password")
        wait.until(EC.element_to_be_clickable(login_button)).click()
        print("Click login button")

        select_product = wait.until(EC.element_to_be_clickable(product_1_add_to_cart_locator))
        select_product.click()
        print("Click Select product")
        enter_shopping_cart = wait.until(EC.element_to_be_clickable(cart_locator))
        enter_shopping_cart.click()
        print("Enter shopping cart")
        time.sleep(3)

        success_test = wait.until(EC.element_to_be_clickable(your_cart_title_locator))
        value_success_test = success_test.text
        assert value_success_test == "Your Cart"
        print("Test success!")
        time.sleep(3)


test = Start_class()
test.select_product()
