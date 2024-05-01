import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from loginpage import LoginPage


class StartClass:
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

        product_1_add_to_cart_locator = ("id", "add-to-cart-sauce-labs-backpack")
        cart_locator = ("id", "shopping_cart_container")
        your_cart_title_locator = ("xpath", "//span[@class='title']")
        time.sleep(3)

        login = LoginPage(driver=driver)
        login.authorization(login=valid_login, password=valid_password)

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


test = StartClass()
test.select_product()
